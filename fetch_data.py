import requests 


response = requests.get("https://api.github.com/users/Adarsh-5harma")
print(response.status_code)
print(response.json())