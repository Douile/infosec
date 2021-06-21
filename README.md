# Infosec scripts

## [hak.sh](./hak.sh)
A shell source file with some useful aliases for ctfs

```bash
. ./hak.sh
```

| Alias    | ...                                                                |
| :------: | :----------------------------------------------------------------- |
| `_VPN`   | Variable specifying what device your VPN binds on (default `tun0`) |
| `tunip`  | Print out bound ip on your vpn, any arguments are echoed when no connection found |
| `rev`    | Start a [pwncat][0] reverse shell, specify port with first argument (default `1337`) |
| `scan`   | Scan a target with [rustscan][1], ip as first argument, addtional arguments are passed through |
| `ferox`  | Scan a web server with [feroxbuster][2], url as first argument, optional wordlist as second (default `/usr/share/seclists/Discovery/Web-Content/common.txt`), any additional arguments can be added after the second |

Outputs for all scanning commands are saved to file called "${name of command}-$(date +%F-%T)"

### Deps
[pwncat][0], [rustscan][1], [feroxbuster][2], [seclists][3]

Install (arch): `paru -S pwncat rustscan feroxbuster-git seclists`

Install (kali): 
```bash
apt-get install -y pwncat feroxbuster seclists
curl -O https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb && dpkg -i ./rustscan_2.0.1_amd64.deb
```

[0]: https://github.com/cytopia/pwncat
[1]: https://github.com/RustScan/RustScan
[2]: https://github.com/epi052/feroxbuster
[3]: https://github.com/danielmiessler/SecLists
