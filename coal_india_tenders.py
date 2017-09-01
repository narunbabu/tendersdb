from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
#import lxml
html = urlopen("https://coalindiatenders.nic.in/nicgep/app")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll("table", {"id":"activeTenders"})
for name in nameList:
    print(name.get_text())
    # Open database connection
    db = pymysql.connect("localhost", "root", "09ne1a0508", "ameyem")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO coal_india_tenders(TENDER_TITLE, REFERENCE_NO, TENDER_CLOSING_DATE, TENDER_OPENING_DATE) VALUES ('%s', '%s', '%s', '%s' )" %(name.get_text())
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()
