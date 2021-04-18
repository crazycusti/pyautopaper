import json
import urllib.request
import hashlib
import re

def getpaperversionnet():
    with urllib.request.urlopen("https://papermc.io/api/v1/paper") as url:
        paperversionnet = json.loads(url.read().decode())
        global paperversionfiltered 
        paperversionfiltered = next(iter(paperversionnet["versions"]))

def getpaperversionlocal():
    with open('version_history.json') as f:
        paperversionlocal = json.loads(f.read())
        global paperversionlocalfiltered
        paperversionlocalprefiltered = re.search(r'MC: (.*)\)$', paperversionlocal["currentVersion"])
        paperversionlocalfiltered = paperversionlocalprefiltered.group(1)

getpaperversionnet()
getpaperversionlocal()

print(paperversionfiltered)
print(paperversionlocalfiltered)