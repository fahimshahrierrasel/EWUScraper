from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = "http://www.ewubd.edu/events/"
uClient = uReq(myUrl)
pageHtml = uClient.read()
uClient.close()
pageSoup = soup(pageHtml, "html.parser")
noticeHighlightContainers = pageSoup.findAll("div", {"col-md-3 col-sm-4 col-xs-6 teacher-col event-col"})
noticeLinks = []
for i in range(len(noticeHighlightContainers)):
    noticeLinks.append(noticeHighlightContainers[i].div.a['href'])
noticeContainers = []
for i in range(len(noticeLinks)):
    myUrl = noticeLinks[i]
    uClient = uReq(myUrl)
    pageHtml = uClient.read()
    uClient.close()
    pageSoup = soup(pageHtml, "html.parser")
    noticeContainer = pageSoup.findAll("div", {"class": "wpb_column vc_column_container vc_col-sm-8"})
    noticeContainers.append(noticeContainer)
# print(noticeContainers[0])
print(noticeHighlightContainers[0])
