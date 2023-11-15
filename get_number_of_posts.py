from read_data import fromJson as FJ
import pprint
def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """
    n=0
    for i in data["messages"]:
        if i["type"]=="message":
            n+=1
    return ""
x=FJ("data/result.json")
pprint.pprint(get_number_of_posts(x))