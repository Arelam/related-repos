import argparse
import asyncio
import os
from aiohttp import web
from GitHubAPI import GitHubAPI
import aiohttp_cors

routes = web.RouteTableDef()

@routes.get('/')
@routes.get('/relatedRepositories/')
async def hello(request):
    text = "USAGE: GET /relatedRepositories/:organization"
    return web.Response(text=text)

@routes.get('/relatedRepositories/{name}')
async def handle(request):
    name = request.match_info.get('name')
    repos = await api.filteredOwned(name)
    return web.json_response(repos, status=200)

@routes.get('/relatedRepositories/{name}/{repo}')
async def details(request):
    name = request.match_info.get('name')
    repoName = request.match_info.get('repo')
    repo = await api.filteredRepo(name, repoName)
    return web.json_response(repo, status=200)

#https://docs.aiohttp.org/en/stable/deployment.html
parser = argparse.ArgumentParser(description="aiohttp server test")
parser.add_argument('--port')

if __name__ == '__main__':
    GITHUB_SECRET_ACCESS_KEY = os.getenv('GITHUB_ACCESS_TOKEN')
    api = GitHubAPI(GITHUB_SECRET_ACCESS_KEY)
    
    app = web.Application()
    app.add_routes(routes)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
                expose_headers="*",
                allow_headers="*",
        )
    })

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)
    #web.run_app(app)
    args = parser.parse_args()
    web.run_app(app, port=args.port)