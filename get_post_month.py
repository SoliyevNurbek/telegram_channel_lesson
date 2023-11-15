from read_data import fromJson as FJ
from datetime import datetime as DT
def fx(f):
    m=int(input('oy = ',))
    if m>0 and m<13:
        print(get_post_month(f,m))
    else :
        fx(f)
def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    n=0
    for j in data["messages"]:
        if j["type"]=="message":
            k=DT.fromtimestamp(int(j["date_unixtime"])).month
            n+=1
    return n
f=FJ("data/result.json")
fx(f)



    


