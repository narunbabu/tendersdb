from bs4 import BeautifulSoup
import urllib.request
import lxml

website_list = ['https://arunachaltenders.gov.in/nicgep/app',
                # 'https://assamtenders.gov.in/nicgep/app',
                # 'https://etenders.kerala.gov.in/nicgep/app',
                # 'https://etenders.hry.nic.in/nicgep/app',
                # 'https://hptenders.gov.in/nicgep/app',
                # 'https://jharkhandtenders.gov.in/nicgep/app',
                # 'https://jktenders.gov.in/nicgep/app',
                # 'https://mahatenders.gov.in/nicgep/app',
                # 'https://manipurtenders.gov.in/nicgep/app',
                # 'https://meghalayatenders.gov.in/nicgep/app',
                # 'https://nagalandtenders.gov.in/nicgep/app',
                # 'https://tendersodisha.gov.in/nicgep/app',
                # 'https://eproc.rajasthan.gov.in/nicgep/app',
                # 'https://sikkimtender.gov.in/nicgep/app',
                # 'https://tripuratenders.gov.in/nicgep/app',
                # 'http://uktenders.gov.in/nicgep/app',
                # 'https://etender.up.nic.in/nicgep/app',
                'https://wbtenders.gov.in/nicgep/app']

for list in website_list:
    html = urllib.request.urlopen(list)
    bsObj = BeautifulSoup(html, 'html.parser')
    nameList = bsObj.find('table', {'id' : 'activeTenders'})
    print(nameList.get_text())
    saveFile = open('today.txt', 'a')
    saveFile.write(str(nameList.get_text()))
saveFile.close()



"""for list in website_list:
    page = urllib.request.urlopen(list)
    soup = BeautifulSoup(page, "html.parser")
    right_table=soup.find('table', {"id" : "activeTenders"})
    for name in right_table:
        print(name.get_text())
        #print(right_table)
        saveFile = open('18AUG2017.html','a')
        saveFile.write(str(name.get_text()))

saveFile.close()
"""
text=nameList.get_text()
proc_array=nameList.get_text().split('\n')
n=0
def printArray( proc_array ):
    for item in proc_array:
        print(item)
        # if len(item) >2:
            # final_array[n]=proc_array[ind]

def trimArray( proc_array ):
    n=0
    final_array=[]
    for item in proc_array:
        # print(len(item))
        if len(item) >2:
            final_array.append(item)
    return final_array

farray=trimArray(proc_array)

printArray(farray)
print(proc_array[2])