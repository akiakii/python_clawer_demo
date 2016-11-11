from urllib.request import urlopen
from bs4 import BeautifulSoup
def getchild(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser").find("table",{"id":"giftList"}).tr.next_siblings
    except AttributeError as e:
        return None
    return bsObj
bsObj =getchild("http://www.pythonscraping.com/pages/page3.html")
for child in bsObj:
    print(child)