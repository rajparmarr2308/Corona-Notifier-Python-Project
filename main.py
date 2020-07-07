from plyer import notification
import requests
from bs4 import BeautifulSoup
import time




def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon='download.ico',
        timeout=8
    )
def getData(url):
    r=requests.get(url)
    #print html template
    return r.text

if __name__ == "__main__":
    # notifyMe("Raj","Let's fight With Corona Together")
    while True:
        myHtmlData=getData("https://www.mohfw.gov.in/")
        soup=BeautifulSoup(myHtmlData,'html.parser')
        # print(soup.prettify())
        mystr=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mystr+=tr.get_text()
        mystr=mystr[1:]

        itemList=mystr.split("""\n\n""") 
        states=['Gujarat','Maharashtra']
        for item in itemList[0:34]:
            dataList=item.split('\n')
            if dataList[1] in states:
                # print(dataList)
                ntitle="Cases of Covid-19"
                nText=f"{dataList[1].upper()}\nTotal Confirmed Cases : {dataList[2]}\nCured\Discharged : {dataList[3]}\nDeaths : {dataList[4]}"
                notifyMe(ntitle,nText)
            
                time.sleep(10)
              
        time.sleep(3600)
