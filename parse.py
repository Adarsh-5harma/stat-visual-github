# json gives everything in one ugly blob
import requests

response = requests.get("https://api.github.com/users/Adarsh-5harma")
# print(response.status_code)

data = response.json()

# only get the data we want and put it in a dictionary
profile_data = {
    "username": data.get("login"),
    "name": data.get("name"),
    "bio": data.get("bio"),
    "location": data.get("location"),
    "public_repos": data.get("public_repos"),
    "followers": data.get("followers"),
    "following": data.get("following"),
    "created_at": data.get("created_at"),
    'updated_at': data.get("updated_at"),
    "repos_url": data.get("repos_url"),
}

# print(profile_data)


repos_response = requests.get(profile_data["repos_url"])
# print(repos_response.status_code)

repos_data = repos_response.json()
print(len(repos_data))
print(f"\nThis is the first data of repo:\n {repos_data[0]}")  # print the first repo's data