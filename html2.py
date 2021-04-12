from bs4 import BeautifulSoup
import requests
r=requests.get("https://www.instagram.com/p/CNYHX40ggEU/")
soup=BeautifulSoup(r.text,"lxml") 
chanel=soup.find_all('a',{'class':"zV_Nj"})

print(chanel)
