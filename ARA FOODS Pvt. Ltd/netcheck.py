import urllib.request as ur

def connect(host='http://google.com'):
    try:
        ur.urlopen(host) 
        return True
    except:
        return False

if connect():
    print('yes')
else:
    print('no')
