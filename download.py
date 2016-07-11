import urllib
import os

if not os.path.exists('mp3'):
    os.makedirs('mp3')

fname="sanguo-list.txt"
file=open(fname,'r')
for line in file:
    line=line[:-1]    
    url='http://yuankuocheng1.zgpingshu.com/%E4%B8%89%E5%9B%BD%E6%BC%94%E4%B9%89/%E4%B8%89%E5%9B%BD%E6%BC%94%E4%B9%89'+urllib.quote(line)+'.mp3'
    if not os.path.isfile('mp3/'+line+'.mp3'):
        print('Downloading: '+line)
        # urllib.urlretrieve(url,'mp3/'+line+'.mp3')
        os.system('wget '+url+' -vO mp3/'+line+'.mp3')
        print('Complete.')
    else:
        print('mp3/'+line+'.mp3 exists')

print('All downloading complete')






