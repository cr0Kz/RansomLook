import os
from bs4 import BeautifulSoup

def main():
    list_div=[]

    for filename in os.listdir('source'):
        try:
            if filename.startswith(__name__.split('.')[-1]+'-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                tbody = soup.find('tbody')
                divs_name = tbody.find_all('tr') # type: ignore
                for div in divs_name:
                    print(div)
                    tds = div.find_all('td')
                    title = tds[0].text.strip()
                    description = tds[2].text.strip()
                    list_div.append({"title" : title, "description" : description})
                file.close()
        except:
            print("Failed during : " + filename)
            pass
    print(list_div)
    return list_div
