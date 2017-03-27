import json
import getpass
import urllib.parse
import urllib.request
import time
import datetime
import os

def utimeToReadebleTime(utime):
    return datetime.datetime.fromtimestamp(utime).strftime('%Y-%m-%d %H:%M:%S')

# current UNIX time 
utimeNow = time.time()
readebleTime  = utimeToReadebleTime(utimeNow)

#load token
cwd = os.getcwd().split('\\')
cwdm2 = '\\'.join(cwd[0:len(cwd) - 2]) + '\\' #Slack ban tokens in public git :D
print(cwdm2)
tokf = open(cwdm2 + 'SlackPostsFreq-token.txt', 'r')
token = tokf.read()
print('Token is: ' + token)
exit()

#get channels.history
print('Loading history in ' + readebleTime)
ret = urllib.request.urlopen('https://slack.com/api/channels.history?token=' + token + '&channel=C0JHTES4B&pretty=1')

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