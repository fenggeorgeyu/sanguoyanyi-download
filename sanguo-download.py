import urllib
import os

if not os.path.exists('mp3'):
    os.makedirs('mp3')

fname="sanguo-list.txt"
file=open(fname,'r')
for line in file:
    line=line[:-1]
    print('Downloading: '+line)
    line=urllib.quote(line)
    url='http://yuankuocheng1.zgpingshu.com/%E4%B8%89%E5%9B%BD%E6%BC%94%E4%B9%89/%E4%B8%89%E5%9B%BD%E6%BC%94%E4%B9%89'+line+'.mp3'
    urllib.urlretrieve(url,'mp3/'+urllib.unquote(line)+'.mp3')
    print('Complete.')

print('All downloading complete')




