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
# run on port 8888 dispatched by haproxy
certbot certonly --standalone -d example.com --non-interactive --force-renewal --http-01-port=8888
certbot certificates
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

## HAProxy

HAProxy to terminate SSL connections and distribute traffic between containers.
```
apt install haproxy
systemctl status haproxy

# check configuration
haproxy -c -f /etc/haproxy/haproxy.cfg
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
    image: postgres:18
    restart: unless-stopped
    volumes:
      - ./volumes/data:/var/lib/postgresql
    driver: "json-file"
    options:
      max-file: 5
      max-size: 10m
    env_file:
      - .env
    networks:
      - backend
```

DB operations
```
# install postgres client on the host
apt update
apt install ca-certificates
curl -fSsL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /usr/share/keyrings/pgdg.gpg

tee /etc/apt/sources.list.d/pgdg.sources <<EOF
Types: deb
URIs: https://apt.postgresql.org/pub/repos/apt/
Suites: trixie-pgdg
Components: main
Signed-By: /usr/share/keyrings/pgdg.gpg
EOF

apt update
apt install postgresql-client

# create app user
createuser --createdb --pwprompt $DB_USER -h localhost -U postgres
createdb -O $DB_USER $DB_DB -h localhost -U postgres

# CLI
# superuser
PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U postgres
# app user
PGPASSWORD=$DB_PWD psql -h localhost -U $DB_USER -d $DB_DB

# Backup
PGPASSWORD=$DB_PWD pg_dump -h localhost -U $DB_USER -d $DB_DB > dump.sql

# Restore
more dump.sql | PGPASSWORD=$DB_PWD psql -h localhost -U $DB_USER -d $DB_DB
```
