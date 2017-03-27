import json
import getpass
import urllib.parse
import urllib.request
import time
import datetime


# current UNIX time 
utimeNow = time.time()
readebleTime  = datetime.datetime.fromtimestamp(utimeNow).strftime('%Y-%m-%d %H:%M:%S')

#get channels.history
print('Loading history in ' + readebleTime)
ret = urllib.request.urlopen('https://slack.com/api/channels.history?token=xoxp-18038795252-135432840195-159583001056-5633a19bc6f7a1294b4b2d82cd591082&channel=C0JHTES4B&pretty=1')

#nice print json
#print(json.dumps(json.load(ret), indent=4, sort_keys=True))

jsonRet = json.load(ret)

if jsonRet['ok'] == True:
    print('Successfully loaded history')
    #continue (az to bude ve smycce)


