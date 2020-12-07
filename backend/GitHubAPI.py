from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

class GitHubAPI():

    def __init__(self, key):
        self.GITHUB_SECRET_KEY = key

        self.__headers = {
            "Authorization": "bearer " + self.GITHUB_SECRET_KEY
        }
        self.__transport = AIOHTTPTransport(
            url="https://api.github.com/graphql",
            headers=self.__headers
            )

    async def filteredOwned(self, name):
        await self.getOwned(name)
        repo = self.filterResponse()
        repoJson = {}
        repoJson["repositories"] = repo
        return repoJson

    async def getOwned(self, arg_org):

        # Using `async with` on the client will start a connection on the transport
        # and provide a `session` variable to execute queries on this connection
        async with Client(
                transport=self.__transport, fetch_schema_from_transport=True,
        ) as session:

            # Execute single query
            query = gql(
                """
                query relatedRepos {
                rateLimit {
                    limit
                    cost
                    remaining
                    resetAt
                }
                organization(login: "%s") {
                    repositories(affiliations: OWNER, first: 10, orderBy: {field: STARGAZERS, direction: DESC}) {
                    edges {
                        node {
                        id
                        name
                        url
                        description
                        forkCount
                        stargazerCount
                        watchers {
                            totalCount
                        }
                        owner {
                            avatarUrl
                            login
                            url
                        }
                        }
                    }
                    }
                    avatarUrl
                    description
                }
                }
            """ % (
                    arg_org,
                )
            )
            result = await session.execute(query)
            self.repos = result
            #return result#["organization"]["repositories"]["edges"]

    def filterResponse(self):
        repoList = []
        repoEdges = self.repos["organization"]["repositories"]["edges"]
        for node in repoEdges:
            out = {}
            out["name"] = node["node"]["name"]
            out["description"] = node["node"]["description"]
            out["owner"] = node["node"]["owner"]["login"]
            out["owner_avatar_url"] = node["node"]["owner"]["avatarUrl"]
            out["url"] = node["node"]["url"]
            out["stargazers_count"] = node["node"]["stargazerCount"]
            out["watchers_count"] = node["node"]["watchers"]["totalCount"]
            repoList.append(out)
        return repoList