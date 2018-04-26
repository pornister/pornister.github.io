import requests 
from bs4 import BeautifulSoup as bs
from urlparse import urljoin

url="http://openloadporn.com/categories/private"

r=requests.get(url)
a=r.content
g=bs(a,"html.parser")

m=g.findAll('div', {'class': "item"})

links=[]
final_links=[]
for i in m:
    b= i.findChild("a")
    links.append(b["href"])

for i in links:
    url=i
    with requests.Session() as session:
        response = session.get(url)
        soup = bs(response.content, 'html.parser')
        soup=soup.findAll("iframe", {"allowtransperancy":False})[0]
        url=soup["src"]
        

        r=requests.get(url)
        
        frame_soup = bs(r.content, 'html.parser')
        final=frame_soup.find("iframe")
        final_links.append(final["src"])

f=open("links.txt","w")
for i in final_links:
    f.write(i)
    f.write("\n")
f.close()
    