import requests
from bs4 import BeautifulSoup
import re

base_domain = "https://www.lbar.com/"

link_base= "https://www.lbar.com/staff"


list_link=[]
for one in range(97,98):
    # print(chr(one))
    item = link_base+chr(one)+"&pos=0,1000,1000&xsearch_id=rets_flex_active_agents_alpha&xsearch=dummy"
    list_link.append(item)



# for item in list_link:
#     #phân tích cú pháp bóc tách data
#      soup = BeautifulSoup(html_doc, 'html.parser')
#     #lưu file csv


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
f = open("output.csv", "a")
# head = f"link_profile,name1,desc,address,email,phone,\n"
# f.write(head)
for i in range(0, len(list_link)):
    print("counter: ", i)
    link = list_link[i]
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    tr_data=soup.find_all('tr')
    # tbody = tb_data[0].find("tbody")

    
    for row in tr_data[1:]:
        td_list = row.find_all('td')

        link_profile = td_list[0].find_all("a")[0].get('href')
        link_p = base_domain+link_profile

        name = td_list[1].text 
        names= name.split("\n")
        names.remove('')
        name1 =names[0].strip().replace(",", "-")
        name2 =names[1].strip().replace(",", "-")


        addr = td_list[2].text.strip().replace(",", "-").replace("\n", "")
        try:
            email = td_list[3].find_all("a")[0].text.strip()      
        except:
            email = ""
        phone = td_list[3].text
        
        try:
            p = re.compile(r"\([0-9]{3}\)\s+[0-9]{3}\-[0-9]{4}")
            x = p.search(phone)
            print(phone)
            pnb= str(x.group(0))
        
        except:
            pnb = ""
        # str1 = f"{link_p},\n"
        # str1 = f"{link_p},{name1},{name2},{addr},{email},{pnb},\n"
        str1 = f"{email},{pnb},\n"
        f.write(str1)

f.close()