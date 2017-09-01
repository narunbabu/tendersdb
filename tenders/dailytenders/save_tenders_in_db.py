from bs4 import BeautifulSoup
import urllib.request
import lxml
from models import Tender
from weblist import website_list

# website_list = ['https://arunachaltenders.gov.in/nicgep/app',
#                   'https://wbtenders.gov.in/nicgep/app']

for list in website_list:
    html = urllib.request.urlopen(list)
    bsObj = BeautifulSoup(html, 'html.parser')
    nameList = bsObj.find('table', {'id' : 'activeTenders'})
    print(nameList.get_text())
    saveFile = open('today.txt', 'a')
    saveFile.write(str(nameList.get_text()))
    tenders_array=trimArray(nameList.get_text().split('\n') )
    saveindb(tenders_array)

def printArray( proc_array ):
    for item in proc_array:
        print(item)

def trimArray( proc_array ):
    n=0
    final_array=[]
    for item in proc_array:
        # print(len(item))
        if len(item) >2:
            final_array.append(item)
    return final_array

def saveindb(tenders_array):
    for i in range(1, len(tenders_array),4):
        print(tenders_array[i-1])
        tender = Tender(description=tenders_array[i-1],tender_number=tenders_array[i],
        start_date=tenders_array[i+1],end_date=tenders_array[i+2])
        tender.save()

# farray=trimArray(proc_array)

# printArray(farray)
# print(proc_array[2])