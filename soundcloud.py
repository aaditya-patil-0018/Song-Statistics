from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://soundcloud.com/search?q=مصطفى%20حجاج%20و%20وجيه%20الأسباني%20-%20كله%20شمال')
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,'lxml')
artists=soup.find_all('span',{'class':'soundTitle__usernameText'})
print(vu)
