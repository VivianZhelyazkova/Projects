import requests
from datetime import datetime

username = input()
api_url = f"https://api.github.com/users/{username}"
response = requests.get(api_url)
if response.status_code != 200:
    print("Username does not exist!")
    exit()
response_body = response.json()
name = response_body["name"]
email = response_body["email"]
public_repos = response_body["public_repos"]
followers = response_body["followers"]
following = response_body["following"]
created_at = response_body["created_at"].split("T")[0]

datetime.strptime(created_at, "%Y-%m-%d")

print(f"User info: \n"
      f"Name: {name}\n"
      f"E-mail: {email}\n"
      f"Public repos: {public_repos}\n"
      f"Followers: {followers}\n"
      f"Following: {following}\n"
      f"Created at: {created_at}")
