from .pipeline import call_pipeline1, call_pipeline2
from .sets import followers, following

def get_report() :
    set1 = call_pipeline1(followers, following)
    set2 = call_pipeline2(followers, following)

    print(f"there are {len(set1)} users not following you back")
    print(f"there are {len(set2)} users you are not following back")
    print("these are all the users not following you back:")
    for user in set1 :
        print(user)
    
    print("these are all the users you aren't following back: ")
    for user in set2:
        print(user)


get_report()