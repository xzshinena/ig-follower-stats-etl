
def get_usersnotfollowingusback(followers: set, following: set) -> set :
    # difference : following - followers

    res = set()
    for user in following :
        if not user in followers :
            res.add(user)

    return res

def get_userswerenotfollowingback(followers: set, following: set) -> set :
    # followers - following

    res = set()
    for user in followers :
        if not user in following :
            res.add(user)

    return res

#def get_ratio(followers: set, following: set) -> str :
    # ratio format --> followers : following





