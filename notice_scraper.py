from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = "http://www.ewubd.edu/category/notices/"
uClient = uReq(myUrl)
pageHtml = uClient.read()
uClient.close()
pageSoup = soup(pageHtml, "html.parser")
noticeHighlightContainers = pageSoup.findAll("div", {"class": "col-md-6 col-sm-6 col-xs-12 blog-cols-sidebar"})
noticeLinks = []
for i in range(len(noticeHighlightContainers)):
    noticeLinks.append(noticeHighlightContainers[i].div.div.a['href'])
noticeContainers = []
for i in range(len(noticeLinks)):
    myUrl = noticeLinks[i]
    uClient = uReq(myUrl)
    pageHtml = uClient.read()
    uClient.close()
    pageSoup = soup(pageHtml, "html.parser")
    noticeContainer = pageSoup.findAll("div", {"class": "wpb_text_column wpb_content_element "})
    noticeContainers.append(noticeContainer)
print("----------------noticeHighlightContainers------------------")
print(noticeHighlightContainers[0])
print("----------------noticeContainers------------------")
print(noticeContainers[0])
