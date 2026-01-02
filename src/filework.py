import json
from pathlib import Path

#files
def load_json(filepath: str | Path) -> dict | list :
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data: dict | list, filepath: str | Path) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

#loading
def load_followers(filepath: str | Path) -> set[str] :
    data = load_json(filepath)
    usernames = set()

    for user in data :
        if user.get("string_list_data"):
            usernames.add(user["string_list_data"][0]["value"])
    
    return usernames

def load_following(filepath: str | Path) -> set[str] :
    data = load_json(filepath)
    usernames = set()
    
    for user in data.get("relationships_following", []) :
        usernames.add(user["title"])
    
    return usernames
