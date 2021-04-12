from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get('https://play.anghami.com/artist/8156296')
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,'lxml')
titel=soup.find_all('spam')
for i in range (len(titel)):
    print(titel[i].text)
