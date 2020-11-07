import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr.find_all('td')
            ulist.append([tds[0].string.strip(),tds[1].a.string.strip(),tds[4].string.strip()])    

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:^10}\t{2:^10}"

    #格式在IDLE里显示串行，但在Terminal里显示正常
    #tplt = "{0:{3}^10}\t{1:{3}^10}\t{2:{3}^10}\t"
    
    print(tplt.format('排名','学校名称','总分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/202011'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo,20) #top 20 university

main()
