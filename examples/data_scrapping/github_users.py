import requests as req
from bs4 import BeautifulSoup as bsoup

base_url = "https://github.com"
r = req.get(base_url)
soup = bsoup(r.text, 'html.parser')
# print(soup.img)
# print(soup.find_all("img"))
# print(soup.find_all("img"))
# print(soup.find_all(class_='logo-img-sm px-2 px-sm-4 px-md-5 my-md-3'))
input_tag = soup.find_all(class_='logo-img-sm px-2 px-sm-4 px-md-5 my-md-3')
elem_id = []
for tagss in input_tag:
    elem_id.append(tagss.get('alt'))
    # elem_id = tagss.get('alt')
print(elem_id[0:3:2])
# if soup.find_all(class_='logo-img-sm px-2 px-sm-4 px-md-5 my-md-3'):
#     print("found")
#     for i in soup.find_all(class_='logo-img-sm px-2 px-sm-4 px-md-5 my-md-3'):
#         print(str(i))
# else:
#     print('not found')