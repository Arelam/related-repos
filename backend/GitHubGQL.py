class GitHubGQL():

    @staticmethod
    def relatedRepos():
        owned = """
            query relatedRepos($name: String!) {
                rateLimit {
                    limit
                    cost
                    remaining
                    resetAt
                }
                organization(login: $name) {
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
            """
        return owned
    
    @staticmethod
    def repoDetails():
        repo = """
            query repo($name:String!, $repo:String!) {
                rateLimit {
                    limit
                    cost
                    remaining
                    resetAt
                }
                repository(name: $repo, owner: $name) {
                    description
                    descriptionHTML
                    name
                    owner {
                        avatarUrl
                        login
                    }
                    projectsUrl
                    url
                    stargazerCount
                    watchers {
                        totalCount
                    }
                    releases(first: 10) {
                        totalCount
                        nodes {
                            publishedAt
                        }
                    }
                }
            }
            """
        return repo
