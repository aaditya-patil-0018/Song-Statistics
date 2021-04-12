from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.instagram.com/p/CNYHX40ggEU/")
res = r.content
#content = res.page_source.encode('utf-8').strip()
#soup = BeautifulSoup(content,"lxml")
#titels=soup.find_all('div',{'div':'cell cell-title purple-label'})

print(res)
