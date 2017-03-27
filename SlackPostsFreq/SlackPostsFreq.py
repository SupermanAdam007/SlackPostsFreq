import json
import getpass
import urllib.parse
import urllib.request
import time
import datetime

def utimeToReadebleTime(utime):
    return datetime.datetime.fromtimestamp(utime).strftime('%Y-%m-%d %H:%M:%S')

# current UNIX time 
utimeNow = time.time()
readebleTime  = utimeToReadebleTime(utimeNow)

#get channels.history
print('Loading history in ' + readebleTime)
ret = urllib.request.urlopen('https://slack.com/api/channels.history?token=xoxp-18038795252-135432840195-161044726919-3e573edec59f92ad8420c224ae389006&channel=C0JHTES4B&pretty=1')

#nice print json
#print(json.dumps(json.load(ret), indent=4, sort_keys=True))

jsonRet = json.load(ret)

if jsonRet['ok'] == True:
    print('Successfully loaded history')
    #continue (az to bude ve smycce)
else:
    print('Not successfully loaded history')
    exit()

for x in jsonRet['messages']:
    print(utimeToReadebleTime(float(x['ts'])))