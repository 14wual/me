import requests

class Display:
    
    def __init__(self) -> None:
        
        repo_url = "https://api.github.com/repos/14wual/me"
        response = requests.get(repo_url)
        if response.status_code == 200:repo_data = response.json();stars =  repo_data['stargazers_count']
        else:print("Failed to get repository data.")
        
        url = 'https://api.github.com/repos/14wual/me/commits'
        res = requests.get(url)
        if res.ok:
            commits = res.json()
            total_commits = len(commits)
            latest_commit = [[commits[0]['commit']['author']['name']], [commits[0]['commit']['message']]]

        url = "https://api.github.com/repos/14wual/me"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            me_license = data["license"]
            descripción = data["description"]
            git_url = data["html_url"]

        
        show = f"""
Welcome to ME!
-------------------------------------------------
Version: BV0.63
File path: /usr/local/etc/me/
-------------------------------------------------
Code By WUAL >> https://github.com/14wual
Star: https://github.com/14wual/me
Twitter: https://twitter.com/codewual
-------------------------------------------------
Powered by 14wual/me!
-------------------------------------------------                                        
GitHub /me:

- About: {descripción}
- Stars: {stars}
- License: {me_license['name']}
- Total Commits: {total_commits}
 - Latest Commit: {latest_commit[1][0]} by {latest_commit[0][0]}
- URL: {git_url}
"""
        print(show)
