from read_data import fromJson as FJ
from datetime import datetime as DT

def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    d={}
    for i in range(1,13):
        d[i]=0
    for j in data["messages"]:
        if j["type"]=="message":
            k=DT.fromtimestamp(int(j["date_unixtime"])).month
            d[k]+=1
    return d
f=FJ("data/result.json")
print(get_post_per_month(f))