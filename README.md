# Test Application

Requirements
------------

```bash
$ docker -v \ Docker version 20.10.17, build *
$ docker-compose -v \ docker-compose version 1.29.2, build *
```

Installation
------------

### Deploy project
```bash
$ cp .env .env.example
$ cp docker-compose.override.yml.dist docker-compose.override.yml
$ docker-compose up -d --build
```