# Python backend API server
Displays GitHub repositories related to an organization

Python requirements:

* [aiohttp](https://docs.aiohttp.org/en/stable/)
* [gql>=3.0](https://github.com/graphql-python/gql)

## Environment variables
GITHUB_ACCESS_TOKEN=`YOUR_TOKEN`

## RUN Dev environment
1. Build backend `docker build -t backend .`
2. Start server `docker run --env-file .env -it --rm -p:8000:8000 --name apiServer backend`

## Usage
`GET /relatedRepositories/:organization`