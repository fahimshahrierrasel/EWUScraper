from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def getAllNotice():
	### Defining URL for the operation, in this case Root Notice URL
	myUrl = "http://www.ewubd.edu/category/notices/"
	### Creating Web Request Client for the URL
	uClient = uReq(myUrl)
	### Extracting Raw data from URL
	pageHtml = uClient.read()
	### Closing Web Request Client
	uClient.close()
	### Parsing Raw URL data as HTML soup
	pageSoup = soup(pageHtml, "html.parser")
	### Collecting All Catelogue for the notices
	noticeHighlightContainers = pageSoup.findAll("div", {"class": "col-md-6 col-sm-6 col-xs-12 blog-cols-sidebar"})
	noticeLinks = []
	### Collecting links of all the notices
	for i in range(len(noticeHighlightContainers)):
		### Inserting Each link of notice to list
	    noticeLinks.append(noticeHighlightContainers[i].div.div.a['href'])
	noticeContainers = []
	###Collecting Actual Notice Body
	for i in range(len(noticeLinks)):
	    myUrl = noticeLinks[i]
	    uClient = uReq(myUrl)
	    pageHtml = uClient.read()
	    uClient.close()
	    pageSoup = soup(pageHtml, "html.parser")
	    noticeContainer = pageSoup.findAll("div", {"class": "wpb_text_column wpb_content_element "})
	    noticeContainers.append(noticeContainer)
	return noticeHighlightContainers, noticeContainers
nt, ntb = getAllNotice()
print("-----------------------------------------Notice Catalogue---------------------------------------")
print(nt)
print("-----------------------------------------Notice Body---------------------------------------")
print(ntb)