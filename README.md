# https://emwj.dev/

This is the repo for https://emwj.dev/.

## Setup
- Clone this repo
- Copy `docker-compose.yml` to `docker-compose-prod.yml` and configure environment variables
  - Set `SECRET_KEY` to a long, random string
  - Set `ALLOWED_HOSTS` to a comma seperated list of domains you want to connect.
- Run `make up`
