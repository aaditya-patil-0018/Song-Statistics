from urllib import request
from bs4 import BeautifulSoup
r=request.urlopen("https://soundcloud.com/njmusicproductions/dggd7s6bjepo")
data=r.read()
html=data.decode('UTF-8')
soup=BeautifulSoup(html,"lxml") 
titel=soup.find_all('span')
#for i in range(len(titel)):
print(titel)
#print(soup)
