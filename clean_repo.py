from parse import repos_data
import pandas as pd

clean_repos = []

for repo in repos_data:
 clean_repo = {
    "name": repo["name"],
    "language": repo.get("language"),
    "stars": repo["stargazers_count"],
    "fork": repo["forks_count"],
    "created_at" : repo["created_at"],
    "updated_at" : repo["updated_at"],
    "is_fork" : repo["fork"],
 }
 clean_repos.append(clean_repo)
# print(f"\nThe Clean repo starts here :\n{clean_repo}")

df = pd.DataFrame(clean_repos)
print(df)

df.to_csv("clean_repos.csv", index=False)
print("\nCleaned repo data has been saved to 'clean_repos.csv'")