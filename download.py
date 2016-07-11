import urllib
import os
import time

if not os.path.exists('mp3'):
    os.makedirs('mp3')

fname="list.txt"
file=open(fname,'r')
prefix=file.readline()
prefix=prefix.split("=")[1][:-1]
for line in file:
    line=line[:-1]
    if not line:
        continue        
    url=prefix+urllib.quote(line)+'.mp3'
    if not os.path.isfile('mp3/'+line+'.mp3'):
        print('Downloading: '+line)       
        #urllib.urlretrieve(url,'mp3/'+line+'.mp3')
        os.system('wget '+url+' -vO mp3/'+line+'.mp3')
        time.sleep(0.5)
        print('Complete.')
    else:
        print('mp3/'+line+'.mp3 exists')

print('All downloading complete')






