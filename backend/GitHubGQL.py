class GitHubGQL():

    @staticmethod
    def relatedRepos():
        return """
            query relatedRepos($name: String!) {
                rateLimit {
                    limit
                    cost
                    remaining
                    resetAt
                }
                organization(login: $name) {
                    repositories(first: 100, orderBy: {field: STARGAZERS, direction: DESC}, ownerAffiliations: OWNER, privacy: PUBLIC) {
                        nodes {
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
                    avatarUrl
                    description
                    membersWithRole(first: 20) {
                    totalCount
                    nodes {
                        id
                        company
                        name
                        login
                        repositories(first: 20, privacy: PUBLIC, orderBy: {field: STARGAZERS, direction: DESC}) {
                        totalCount
                        nodes {
                            description
                            name
                            owner {
                                avatarUrl
                                login
                                url
                            }
                            url
                            stargazerCount
                            watchers {
                                totalCount
                            }
                        }
                        }
                        watching(first: 20, privacy: PUBLIC, orderBy: {field: STARGAZERS, direction: DESC}) {
                        totalCount
                        nodes {
                            description
                            name
                            owner {
                                login
                                avatarUrl
                                url
                            }
                            url
                            stargazerCount
                            watchers {
                                totalCount
                            }
                        }
                        }
                    }
                    }
                }
            }
            """
    
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
