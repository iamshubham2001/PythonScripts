import requests

username = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{username}"

response = requests.get(url)  

# Check API status first
if response.status_code != 200:
    print("API request failed.")
else:
    data = response.json()

    print(f"Username: {data['login']}")
    print(f"public Repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
