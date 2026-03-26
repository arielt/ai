# Debian

Spinning up a backend stack on Debian.

## Hetzner

Create a new server: https://console.hetzner.com/projects/1279557/servers/create
  - Debian 13
  - Will need a public IP
  - Private network in eu-central

## Docker

```
apt update

install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/debian
Suites: $(. /etc/os-release && echo "$VERSION_CODENAME")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

apt update

apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
systemctl status docker
```

## Letsencrypt

```
apt install certbot
systemctl status certbot
```

## Git
```
apt install git
```

## Network
Docker compose:
```
networks:
  frontend:
    # default bridge network, allows external access
  backend:
    driver: bridge
    internal: true # prevents containers on this network from having outgoing internet access
```
## Postgres

The default Postgres image is Debian. No ports to be open. 
Docker compose:
```
  db:
    image: postgresql:latest
    restart: unless-stopped
    volumes:
      - ./volumes/db:/var/lib/postgresql/data
    driver: "json-file"
    options:
      max-file: 5
      max-size: 10m
    env_file:
      - .env
    networks:
      - backend
```
