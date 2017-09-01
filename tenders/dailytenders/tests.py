# from django.test import TestCase
from bs4 import BeautifulSoup
import urllib.request
import lxml
from dailytenders.models import Tender
from dailytenders.weblist import website_list

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



for list in website_list:
    try:
        html = urllib.request.urlopen(list)
        bsObj = BeautifulSoup(html, 'html.parser')
        nameList = bsObj.find('table', {'id' : 'activeTenders'})
        tenders_array=trimArray(nameList.get_text().split('\n') )
        saveindb(tenders_array)
    except expression as identifier:
        pass
    # html = urllib.request.urlopen(list)
    # bsObj = BeautifulSoup(html, 'html.parser')
    # nameList = bsObj.find('table', {'id' : 'activeTenders'})
    # tenders_array=trimArray(nameList.get_text().split('\n') )
    # saveindb(tenders_array)

def printArray( proc_array ):
    for item in proc_array:
        print(item)



# farray=trimArray(proc_array)

# printArray(farray)
# print(proc_array[2])