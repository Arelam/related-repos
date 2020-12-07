import argparse
import asyncio
import os
from aiohttp import web
from GitHubAPI import GitHubAPI

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
    return web.json_response(repos)

#https://docs.aiohttp.org/en/stable/deployment.html
parser = argparse.ArgumentParser(description="aiohttp server test")
parser.add_argument('--port')

if __name__ == '__main__':
    GITHUB_SECRET_ACCESS_KEY = os.getenv('GITHUB_ACCESS_TOKEN')
    api = GitHubAPI(GITHUB_SECRET_ACCESS_KEY)
    
    app = web.Application()
    app.add_routes(routes)
    #web.run_app(app)
    args = parser.parse_args()
    web.run_app(app, port=args.port)