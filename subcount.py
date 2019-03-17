import urllib.request
import json

name=input("Enter username: ")
key = "AIzaSyC8XpMZL4K96H2DoOXW2P3Mx0Y-x3acWwU"


data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(name + " has " + "{:,d}".format(int(subs)) + " subscribers!🎉")
