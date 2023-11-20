import requests
import json
import datetime

api_url = "https://api.github.com/users/VivianZhelyazkova"
response = requests.get(api_url)
response_body = response.json()
name = response_body["name"]
email = response_body["email"]
public_repos = response_body["public_repos"]
followers = response_body["followers"]
following = response_body["following"]
created_at = response_body["created_at"]

print(f"User info: \n"
      f"Name: {name}\n"
      f"E-mail: {email}\n"
      f"Public repos: {public_repos}\n"
      f"Followers: {followers}\n"
      f"Following: {following}\n"
      f"Created at: {created_at}\n")
