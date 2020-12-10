from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from GitHubGQL import GitHubGQL

class GitHubAPI():

    def __init__(self, key):
        self.GITHUB_SECRET_KEY = key
        self.gql = GitHubGQL

        self.__headers = {
            "Authorization": "bearer " + self.GITHUB_SECRET_KEY
        }
        self.__transport = AIOHTTPTransport(
            url="https://api.github.com/graphql",
            headers=self.__headers
            )

    async def filteredRelatedRepos(self, name):
        query = self.gql.relatedRepos()
        related = await self.queryAPI(query, name)
        #repos = self.extractNodeLists(await self.getOwned(name))
        repos = self.extractNodeLists(related)
        repoJson = {}
        repoJson["repositories"] = repos
        return repoJson
    
    @staticmethod
    def extractNodeLists(dictNode):
        # alternative merge extractions TODO work on
        # repoOrg = related["organization"]["repositories"]["nodes"]
        # repoMember = repoList["organization"]["membersWithRole"]["nodes"]["repositories"]["nodes"]
        # repoMemberWatch = repoList["organization"]["membersWithRole"]["nodes"]["watching"]["nodes"]

        # https://stackoverflow.com/a/26853961
        #repoMerge = {**repoOrg, **repoMember, **repoMemberWatch}

        lists = []
        for node in dictNode["organization"]["repositories"]["nodes"]:
            out = GitHubAPI.mapRepoData(node)
            lists.append(out)
        for node in dictNode["organization"]["membersWithRole"]["nodes"]:
            for innerNode in node["repositories"]["nodes"]:
                out = GitHubAPI.mapRepoData(innerNode)
                if out not in lists:
                    lists.append(out)
            for innerNode in node["watching"]["nodes"]:
                out = GitHubAPI.mapRepoData(innerNode)
                if out not in lists:
                    lists.append(out)
        return lists

    
    @staticmethod
    def mapRepoData(repo):
        out = {}
        out["name"] = repo["name"]
        out["description"] = repo["description"]
        out["owner"] = repo["owner"]["login"]
        out["owner_avatar_url"] = repo["owner"]["avatarUrl"]
        out["url"] = repo["url"]
        out["stargazers_count"] = repo["stargazerCount"]
        out["watchers_count"] = repo["watchers"]["totalCount"]
        return out
    
    async def queryAPI(self, queryString, arg_org):
        # Using `async with` on the client will start a connection on the transport
        # and provide a `session` variable to execute queries on this connection
        async with Client(
                transport=self.__transport, fetch_schema_from_transport=True,
        ) as session:

            # Execute single query
            query = gql(queryString)
            params = {
                "name": arg_org
            }
            result = await session.execute(query, params)
            return result


    async def filteredRepo(self, org, repo):
        await self.getRepo(org, repo)
        return self.filterRepo()
        # detail = self.filterRepo()
        # repoJson = {}
        # repoJson["repository"] = detail
        # return repoJson

    async def getRepo(self, arg_org, arg_repo):

        # Using `async with` on the client will start a connection on the transport
        # and provide a `session` variable to execute queries on this connection
        async with Client(
                transport=self.__transport, fetch_schema_from_transport=True,
        ) as session:

            # Execute single query
            query = gql(self.gql.repoDetails())
            params = {
                "name": arg_org,
                "repo": arg_repo
            }
            result = await session.execute(query, params)
            self.repo = result

    def filterRepo(self):
        node = self.repo["repository"]
        out = {}
        out["name"] = node["name"]
        out["description"] = node["description"]
        out["owner"] = node["owner"]["login"]
        out["owner_avatar_url"] = node["owner"]["avatarUrl"]
        out["url"] = node["url"]
        out["stargazers_count"] = node["stargazerCount"]
        out["watchers_count"] = node["watchers"]["totalCount"]
        return out

    @staticmethod
    def filterResponse(repoList):
        repoListed = []
        #repoEdges = self.repos["organization"]["repositories"]["edges"]
        #repoEdges = self.repos["organization"]["repositories"]["nodes"]

        for node in repoList:
            out = {}
            out["name"] = node["name"]
            out["description"] = node["description"]
            out["owner"] = node["owner"]["login"]
            out["owner_avatar_url"] = node["owner"]["avatarUrl"]
            out["url"] = node["url"]
            out["stargazers_count"] = node["stargazerCount"]
            out["watchers_count"] = node["watchers"]["totalCount"]
            repoListed.append(out)
        return repoListed
