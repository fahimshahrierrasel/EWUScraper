from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from time import strptime

def getAllEvents():
	### Defining URL for the operation, in this case Root Event URL
	myUrl = "http://www.ewubd.edu/events/"
	### Creating Web Request Client for the URL
	uClient = uReq(myUrl)
	### Extracting Raw data from URL
	pageHtml = uClient.read()
	### Closing Web Request Client
	uClient.close()
	### Parsing Raw URL data as HTML soup
	pageSoup = soup(pageHtml, "html.parser")
	### Collecting All Catelogue for the events
	eventHighlightContainers = pageSoup.findAll("div", {"col-md-3 col-sm-4 col-xs-6 teacher-col event-col"})
	eventLinks = []
	### Collecting links of all the events
	for i in range(len(eventHighlightContainers)):
		### Inserting Each link of event to list
	    eventLinks.append(eventHighlightContainers[i].div.a['href'])
	eventContainers = []
	### Collecting Actual event Body
	print("------------------",len(eventLinks)," events found------------------------")
	for i in range(len(eventLinks)):
		print("-----------------------Event no: ",i+1," ---------------------------")
		myUrl = eventLinks[i]
		uClient = uReq(myUrl)
		pageHtml = uClient.read()
		uClient.close()
		pageSoup = soup(pageHtml, "html.parser")
		eventContainer = []        
		eventBody = pageSoup.find("div", {"class": "wpb_text_column wpb_content_element "})
		if(eventBody is None):
			eventBody = pageSoup.find("div", {"class": "wpb_single_image wpb_content_element vc_align_center"})
		if(eventBody is None):
			eventBody = pageSoup.find("div", {"class": "wpb_raw_code wpb_content_element wpb_raw_html"})
		body = eventBody
		print(body)
		eventDate = pageSoup.find("li", {"class": "post_date h6"})
		### Date Convertion
		temp = str(eventDate.span.decode_contents())
		temp = temp.split()
		mm = strptime(temp[0][:3], '%b').tm_mon
		dd = temp[1][:-1]
		yy = temp[2]
		temp = str(dd) + "/" + str(mm) + "/" + str(yy)
		eventDate = temp
		eventPostedBy = pageSoup.find("li", {"class": "post_by h6"})
		eventTitle = pageSoup.find("h1", {"class": "h2 post_title"})
		eventContainer = {
			u'title': eventTitle.decode_contents(),
			u'date': eventDate,
			u'postedBy': eventPostedBy.span.decode_contents(),
			u'body': body
		}
		eventContainers.append(eventContainer)
	return eventContainers