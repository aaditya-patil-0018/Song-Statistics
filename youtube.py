from selenium import webdriver
from bs4 import BeautifulSoup
singer=input('input the name of the singer')
n=int(input('input the number of songs'))
song=[str]*n
titels=[]
vus=[]
for i in range(n):
    
    song[i]=input('input the name of the song '+str(i+1))
    qw=str(song[i])
    driver = webdriver.Chrome()
    url='https://www.youtube.com/c/'+singer+'/search?query='+qw
    driver.get(url)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,'lxml')
    titel = soup.findAll('a',id='video-title')
    titels.append(titel[0])
    vu = soup.findAll('span',{'class':'style-scope ytd-video-meta-block'})
    print(vu[0].text)
