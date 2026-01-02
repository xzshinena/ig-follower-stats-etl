from pathlib import Path
from .filework import load_followers, load_following
from .logic import get_userswerenotfollowingback, get_usersnotfollowingusback


def call_pipeline1(followers : str | Path, following : str | Path) :
    followers_set = load_followers(followers)
    following_set = load_following(following)

    return get_usersnotfollowingusback(followers_set, following_set)
    
def call_pipeline2(followers : str | Path, following : str | Path) :
    followers_set = load_followers(followers)
    following_set = load_following(following)

    return get_userswerenotfollowingback(followers_set, following_set)

