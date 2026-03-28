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

## Hugo

Dockerfile

```
# build image
FROM debian:trixie-slim AS build
RUN apt-get update && apt-get install -y \
    curl \
    git \
    ca-certificates \
    --no-install-recommends

# get latest Hugo release (extended version for SASS support)
RUN HUGO_VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep tag_name | cut -d '"' -f 4 | sed 's/v//') && \
    curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb" -o /tmp/hugo.deb && \
    apt-get install -y /tmp/hugo.deb

# build site
WORKDIR /src
COPY . .
RUN hugo version
RUN hugo

# production image
FROM nginx:latest
COPY --from=build /src/public /usr/share/nginx/html
EXPOSE 80/tcp
CMD ["nginx", "-g", "daemon off;"]
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
    image: postgres:latest
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
