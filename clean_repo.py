from parse import repos_data

repo = repos_data[0]

clean_repo = {
    "name": repo["name"],
    "language": repo.get("language"),
    "stars": repo["stargazers_count"],
    "fork": repo["forks_count"],
    "created_at" : repo["created_at"],
    "updated_at" : repo["updated_at"],
    "is_fork" : repo["fork"],
}

print(f"\nThe Clean repo starts here :\n{clean_repo}")