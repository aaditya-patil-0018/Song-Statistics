import urllib.request
import re
import requests
from bs4 import BeautifulSoup
def modif(name):
    while (name.find(' ')!=-1):
        name=name[:name.find(' ')]+'20%'+name[name.find(' ')+1]
    return name
while True:
    artistname = input('write the Artist name without space in the beginning and the end : ')
    if(artistname!='')and(artistname[0]!=' ')and(artistname[-1]!=' '):
        break
while True:
    songname=input('write the song name without space in the beginning and the end : ')
    if(songname!='')and(songname[0]!=' ')and(songname[-1]!=' '):
        break

html2 = urllib.request.urlopen('https://open.spotify.com/search/'+modif(artistname))
video_ids = re.findall(r"artist\?(\S{22})", html2.read().decode())
url='https://open.spotify.com/artist/'+video_ids[0]

html = urllib.request.urlopen(url)
html1 = html.read().decode()
soup = BeautifulSoup(html1, 'html.parser')
alldiv = soup.find_all("span", class_='track-name')
for i in range (len(alldiv)):
    alldiv[i]=alldiv[i].text


vu = soup.find_all('div', {"class" : 'e8ea6a219247d88aa936a012f6227b0d-scss'})
print(alldiv)