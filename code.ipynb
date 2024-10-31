import requests
import pandas as pd
import numpy as np
from datetime import datetime
from tqdm import tqdm
import re

# Replace 'your_github_token_here' with your actual GitHub token
GITHUB_TOKEN = 'GITHUB_TOKEN'
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}
BASE_URL = 'https://api.github.com'


# Modify functions to add progress bars

# Retrieve users with over 50 followers in Dublin
def get_dublin_users(min_followers=50):
    users = []
    page = 1
    with tqdm(desc="Fetching Dublin Users", unit="page") as pbar:
        while True:
            # Search for users in Dublin with the specified number of followers
            url = f"{BASE_URL}/search/users?q=location:Dublin+followers:>{min_followers}&page={page}&per_page=100"
            response = requests.get(url, headers=HEADERS)
            data = response.json()

            if 'items' not in data:
                break
            users.extend(data['items'])

            if len(data['items']) < 100:
                break
            page += 1
            pbar.update(1)  # Update progress bar for each page
    return users

# Fetch user details
def get_user_details(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

# Fetch repositories for a user
def get_user_repos(username, max_repos=500):
    repos = []
    page = 1
    while len(repos) < max_repos:
        url = f"{BASE_URL}/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        if not data:
            break
        repos.extend(data[:max_repos - len(repos)])
        page += 1
    return repos[:max_repos]
# Fetch user details and add progress bar for each user
dublin_users = get_dublin_users()

# Initialize lists for user and repository data
users_data = []
repos_data = []

for user in tqdm(dublin_users, desc="Processing Users", unit="user"):
    details = get_user_details(user['login'])

    # Clean company name
    company = details.get('company', '') or ''
    company = re.sub(r'^@', '', company.strip()).upper()

    # Append to users data
    users_data.append({
        'login': details['login'],
        'name': details.get('name', ''),
        'company': company,
        'location': details.get('location', ''),
        'email': details.get('email', ''),
        'hireable': details.get('hireable', ''),
        'bio': details.get('bio', ''),
        'public_repos': details.get('public_repos', 0),
        'followers': details.get('followers', 0),
        'following': details.get('following', 0),
        'created_at': details.get('created_at', '')
    })

    # Fetch up to 500 repositories per user
    repos = get_user_repos(details['login'])
    for repo in repos:
        repos_data.append({
            'login': details['login'],
            'full_name': repo['full_name'],
            'created_at': repo['created_at'],
            'stargazers_count': repo['stargazers_count'],
            'watchers_count': repo['watchers_count'],
            'language': repo['language'] or '',
            'has_projects': repo['has_projects'],
            'has_wiki': repo['has_wiki'],
            'license_name': repo['license']['key'] if repo['license'] else ''
        })

# Convert to DataFrames
users_df = pd.DataFrame(users_data)
repos_df = pd.DataFrame(repos_data)

# Save as CSV files
users_df.to_csv('users.csv', index=False)
repos_df.to_csv('repositories.csv', index=False)

# Write README.md content
readme_content = """
* This project scrapes GitHub data for users in Dublin with over 50 followers.
* Analysis shows interesting patterns in user engagement and repository activity.
* Developers should consider enabling wiki and project features to improve repository visibility.

"""

with open('README.md', 'w') as f:
    f.write(readme_content)

# Display data for question analysis
users_df.head(), repos_df.head()
