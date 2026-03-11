import json

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.filework import parse_followers_data, parse_following_data
from src.logic import get_usersnotfollowingusback, get_userswerenotfollowingback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/analyze")
async def analyze(
    followers: UploadFile = File(...),
    following: UploadFile = File(...),
):
    try:
        followers_raw = json.loads(await followers.read())
        following_raw = json.loads(await following.read())
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON file: {e}")

    followers_set = parse_followers_data(followers_raw)
    following_set = parse_following_data(following_raw)

    not_following_back = get_usersnotfollowingusback(followers_set, following_set)
    you_dont_follow_back = get_userswerenotfollowingback(followers_set, following_set)
    mutual = followers_set & following_set

    total_following = len(following_set)
    ratio = round((len(mutual) / total_following * 100), 1) if total_following else 0

    return {
        "totalFollowers": len(followers_set),
        "totalFollowing": total_following,
        "notFollowingBack": len(not_following_back),
        "youDontFollowBack": len(you_dont_follow_back),
        "mutualFollows": len(mutual),
        "followBackRatio": ratio,
    }
