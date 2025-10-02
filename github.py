import requests

owner = "bassilhossien"
repo = "contoso-university"

token = "----"
headers = {
    "token": f"{token}"
}

url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

def fetch_open_pulls():
    response = requests.get(url, headers=headers, params={"state": "open"})

    open_pulls = response.json()

    open_pulls_list = []
    for pr in open_pulls:
        open_pulls_list.append({
            "number": pr["number"],
            "title": pr["title"],
            "user": pr["user"]["login"],
            "created_at": pr["created_at"],
            "url": pr["html_url"]
        })

    return open_pulls_list

def get_pulls_grouped_by_user():
    response = requests.get(url, headers=headers, params={"state": "open"})

    open_pulls = response.json()

    pulls_by_user = {}
    for pr in open_pulls:
        user = pr["user"]["login"]
        if user not in pulls_by_user:
            pulls_by_user[user] = []
        pulls_by_user[user].append({
            "number": pr["number"],
            "title": pr["title"],
            "created_at": pr["created_at"],
            "url": pr["html_url"]
        })

    return pulls_by_user

def get_pulls_sorted_by_creation_date():
    response = requests.get(url, headers=headers, params={"state": "open"})

    open_pulls = response.json()

    sorted_pulls = sorted(open_pulls, key=lambda pr: pr["created_at"])

    sorted_pulls_list = []
    for pr in sorted_pulls:
        sorted_pulls_list.append({
            "number": pr["number"],
            "title": pr["title"],
            "user": pr["user"]["login"],
            "created_at": pr["created_at"],
            "url": pr["html_url"]
        })

    return sorted_pulls_list

def accept_pull_request(pr_number):
    merge_token = "----"
    merge_header = {
        "Authorization": f"token {merge_token}"
    }
    accept_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/merge"
    response = requests.put(accept_url, headers=merge_header)

    if response.status_code == 200:
        return {"status": "success", "message": f"Pull request #{pr_number} merged successfully."}
    else:
        return {"status": "error", "message": f"Failed to merge pull request #{pr_number}.", "details": response.json()}