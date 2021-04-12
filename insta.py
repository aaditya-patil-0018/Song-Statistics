from selenium import webdriver
from bs4 import BeautifulSoup
url=(input('input the url of the video in insta: '))
driver = webdriver.Chrome()
driver.get(url)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,'lxml')
vu=soup.find_all('div',{'class':'HbPOm _9Ytll'})
print(vu[0].text)

