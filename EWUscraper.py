from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import strptime

def notices():
	myUrl = "http://www.ewubd.edu/category/notices/"
	uClient = uReq(myUrl)
	pageHtml = uClient.read()
	uClient.close()
	pageSoup = soup(pageHtml, "html.parser")
	noticeHighlightContainers = pageSoup.findAll("div",{"class":"col-md-6 col-sm-6 col-xs-12 blog-cols-sidebar"})
	noticeLinks = []
	for i in range(len(noticeHighlightContainers)):
	    noticeLinks.append(noticeHighlightContainers[i].div.div.a['href'])
	noticeContainers=[]
	for i in range(len(noticeLinks)):
		myUrl = noticeLinks[i]
		uClient = uReq(myUrl)
		pageHtml = uClient.read()
		uClient.close()
		pageSoup = soup(pageHtml, "html.parser")
		noticeContainer = pageSoup.findAll("div",{"class":"wpb_text_column wpb_content_element "})
		noticeContainers.append(noticeContainer)
	return noticeHighlightContainers, noticeContainers

def news():
	myUrl = "http://www.ewubd.edu/category/news/"
	uClient = uReq(myUrl)
	pageHtml = uClient.read()
	uClient.close()
	pageSoup = soup(pageHtml, "html.parser")
	newsHighlightContainers = pageSoup.findAll("div",{"class":"col-md-6 col-sm-6 col-xs-12 blog-cols-sidebar"})
	newsLinks = []
	for i in range(len(newsHighlightContainers)):
	    newsLinks.append(newsHighlightContainers[i].div.div.a['href'])
	newsContainers=[]
	for i in range(len(newsLinks)):
		myUrl = newsLinks[i]
		uClient = uReq(myUrl)
		pageHtml = uClient.read()
		uClient.close()
		pageSoup = soup(pageHtml, "html.parser")
		newsContainer=[]
		newsImages=pageSoup.findAll("img",{"class":"attachment-full"})
		newsBody = pageSoup.findAll("div",{"class":"wpb_text_column wpb_content_element "})
		newsDate = pageSoup.find("li",{"class":"post_date h6"})
		###Date Convertion
		temp = str(newsDate.span.decode_contents())
		temp = temp.split()
		mm = strptime(temp[0][:3],'%b').tm_mon
		dd= temp[1][:-1]		
		yy= temp[2]
		temp = str(dd)+"/"+str(mm)+"/"+str(yy)	
		newsDate=temp
		newsPostedBy = pageSoup.find("li",{"class":"post_by h6"})
		newsTitle = pageSoup.find("h1",{"class":"h2 post_title"})	
		newsImageLinks=[]	
		for j in range(len(newsImages)):
			newsImageLinks.append(newsImages[j]['src'])	
		newsContainer = {
			u'title': newsTitle.decode_contents(),
			u'date'	: newsDate,
			u'postedBy': newsPostedBy.span.decode_contents(),
			u'imageLinks': newsImageLinks,
			u'body':newsBody[0].div.p
		}
		newsContainers.append(newsContainer)
	return newsHighlightContainers, newsContainers

def events():
	myUrl = "http://www.ewubd.edu/events/"
	uClient = uReq(myUrl)
	pageHtml = uClient.read()
	uClient.close()
	pageSoup = soup(pageHtml, "html.parser")
	eventHighlightContainers = pageSoup.findAll("div",{"col-md-3 col-sm-4 col-xs-6 teacher-col event-col"})
	eventLinks = []
	for i in range(len(eventHighlightContainers)):
	    eventLinks.append(eventHighlightContainers[i].div.a['href'])
	eventContainers=[]
	for i in range(len(eventLinks)):
		myUrl = eventLinks[i]
		uClient = uReq(myUrl)
		pageHtml = uClient.read()
		uClient.close()
		pageSoup = soup(pageHtml, "html.parser")
		eventContainer = pageSoup.findAll("div",{"class":"wpb_column vc_column_container vc_col-sm-8"})
		eventContainers.append(eventContainer)	
	return eventHighlightContainers, eventContainers