import urllib.request
import json

import os
import re

token = os.environ.get("GITHUB_TOKEN")
if not token:
    # Coba baca dari ~/.git-credentials jika ada
    cred_path = os.path.expanduser("~/.git-credentials")
    if os.path.exists(cred_path):
        try:
            with open(cred_path, "r", encoding="utf-8") as f:
                content = f.read()
                # format umum: https://username:token@github.com
                match = re.search(r":([^@:]+)@github\.com", content)
                if match:
                    token = match.group(1)
        except Exception:
            pass

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/vnd.github.v3+json"
}
if token:
    headers["Authorization"] = f"Bearer {token}"

def fetch_repos(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

org_repos = fetch_repos("https://api.github.com/orgs/Yayasan-Bina-Insan-Mustaqbal/repos?per_page=100")
user_repos_p1 = fetch_repos("https://api.github.com/users/decaller/repos?per_page=100&page=1")
user_repos_p2 = fetch_repos("https://api.github.com/users/decaller/repos?per_page=100&page=2")
user_repos = user_repos_p1 + user_repos_p2

all_data = {
    "org_repos": org_repos,
    "user_repos": user_repos
}

with open("data/github_repos_raw.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2)

print(f"Total org repos: {len(org_repos)}")
print(f"Total user repos: {len(user_repos)}")

print("\n=== REPOS YAYASAN BINA INSAN MUSTAQBAL ===")
for r in org_repos:
    name = r.get("name")
    desc = r.get("description") or "No description"
    url = r.get("html_url")
    lang = r.get("language")
    stars = r.get("stargazers_count", 0)
    updated = r.get("updated_at")
    print(f"* [{name}]({url}) - {desc} (Lang: {lang}, Updated: {updated})")

print("\n=== REPOS DECALLER (TERKAIT PKN/ISLAM/EDUTECH/AI) ===")
for r in user_repos:
    name = r.get("name")
    desc = r.get("description") or "No description"
    url = r.get("html_url")
    lang = r.get("language")
    updated = r.get("updated_at")
    print(f"* [{name}]({url}) - {desc} (Lang: {lang}, Updated: {updated})")
