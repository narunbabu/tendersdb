from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql

conn = pymysql.connect("localhost","root","09ne1a0508","ameyem", charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")
random.seed(datetime.datetime.now())

def store(tender_title, reference_no, tender_closing_date, tender_opening_date):
    cur.execute("INSERT INTO COAL_INDIA_TENDERS (TENDER_TITLE, REFERENCE_NO, TENDER_CLOSING_DATE, TENDER_OPENING_DATE) VALUES (\"%s\",\"%s\",\"%s\",\"%s\")",(tender_title, reference_no, tender_closing_date, tender_opening_date))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("https://coalindiatenders.nic.in/nicgep/app")
    bsObj = BeautifulSoup(html, "html.parser")
    tender_title = bsObj.find("table", {"id":"activeTenders"}).find('td width="30%"').get_text()
    reference_no = bsObj.find("table", {"id":"activeTenders"}).find('td width="20%"').get_text()
    tender_closing_date = bsObj.find("table", {"id":"activeTenders"}).find('td width="25%"').get_text()
    tender_opening_date = bsObj.find("table", {"id":"activeTenders"}).find('td width="25%"').get_text()
    store(tender_title, reference_no, tender_closing_date, tender_opening_date)
    #return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    #links = getLinks("/wiki/Kevin_Bacon")

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
