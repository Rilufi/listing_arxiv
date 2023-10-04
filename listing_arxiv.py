from bs4 import BeautifulSoup
import requests
import httplib2
import os
import base64
from user_settings import URL, list_key, api
import datetime
from time import sleep
import telebot

today = datetime.date.today() # ex 2015-10-31
data = today.strftime("%d/%m")

url_get = requests.get(URL)
soup = BeautifulSoup(url_get.content, 'html.parser')

h3 = soup.find('h3')
for sibling in h3.find_next_siblings():
    sleep(0.01)
    if sibling.name == "h3":
        break
    else:
        title_element = sibling.find_all("div", class_="list-title mathjax")
        abstract_element = sibling.find_all("p", class_="mathjax")
        link_element = sibling.find_all("a",  {"title":"Abstract"})

list_index = []

send = False
email_body = ""
for key in list_key:
    print("\n\n", key)
    email_body = email_body + key + "\n---------------------------" + "\n"
    aux = 0
    for index, title in enumerate(title_element):
        if set(list_key[key]) & set(title.text.strip().lower().split(' ')) or set(list_key[key]) & set(abstract_element[index]):            
            print(title.text.strip(), '\n')
            print(abstract_element[index].text.strip(), '\n')
            print("www.arxiv.org/abs/"+link_element[index].text.strip().split(':')[-1], '\n')
            print("---------------------------")

            email_body = email_body + str(title.text.strip())+'\n' + "Abstract:"+ str(abstract_element[index].text.strip())+'\n'+\
                            "www.arxiv.org/abs/"+str(link_element[index].text.strip().split(':')[-1])+'\n\n'
            list_index.append(index)
            aux = aux + 1
            send = True
    if aux == 0:
        print("No articles found today. \n")
        email_body = email_body + "No articles published today. \n\n"

TOKEN = os.environ["TELEGRAM_TOKEN"]
bot = telebot.TeleBot(TOKEN)
toReply = "nasobot" 

mystring = f""" Astrophysics 
new arXiv submissions {data}

https://arxiv.org/list/astro-ph/new"""

try:
    api.update_status(mystring)
except:
    print("não rolou o status")
    pass

myexstring = f"""{email_body}"""

def get_chunks(s, maxlength):
    start = 0
    end = 0
    while start + maxlength  < len(s) and end != -1:
        end = s.rfind(" ", start, start + maxlength + 1)
        yield s[start:end]
        start = end +1
    yield s[start:]

chunks = get_chunks(myexstring, 280)

#Make list with line lengths:
chunkex = [(n) for n in chunks]

coun = 0

try:
    while coun < len(chunkex):
        tweets = api.user_timeline(screen_name = toReply, count=1)
        for tweet in tweets:
            api.update_status(str(chunkex[coun]), in_reply_to_status_id = tweet.id, auto_populate_reply_metadata = True)
            coun += 1
except:
    print("não rolou o resto")
    pass
            
try:
    api.send_direct_message("1008771819745226754", mystring+ "\n" +myexstring)
    api.send_direct_message("1532143352837292033", mystring+ "\n" +myexstring)
except:
    print("treta nas dm")
    pass
