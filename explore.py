import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("GITHUB_TOKEN")

query = """
{
  search(query: "topic:astronomy stars:>50", type: REPOSITORY, first: 10) {
    repositoryCount
    nodes {
      ... on Repository {
        name
        stargazerCount
        forkCount
        description
        createdAt
        pushedAt
        primaryLanguage { name }
        languages(first: 5) {
          nodes { name }
        }
        openIssues: issues(states: OPEN) { totalCount }
        closedIssues: issues(states: CLOSED) { totalCount }
        pullRequests(states: OPEN) { totalCount }
        watchers { totalCount }
        repositoryTopics(first: 5) {
          nodes {
            topic { name }
          }
        }
      }
    }
  }
}
"""

response = requests.post(
    "https://api.github.com/graphql",
    json={"query": query},
    headers={"Authorization": f"Bearer {TOKEN}"}
)

print(json.dumps(response.json(), indent=2))