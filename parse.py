# json gives everything in one ugly blob
import requests

response = requests.get("https://api.github.com/users/Adarsh-5harma")
print(response.status_code)

data = response.json()

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
    "avatar_url": data.get("avatar_url"),
}

print(profile_data)
