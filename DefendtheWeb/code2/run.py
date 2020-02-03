import requests
from bs4 import BeautifulSoup

def Auth():
    sess = requests.Session()
    url = 'https://www.hackthis.co.uk/?login'
    data = {"username": "", "password": ""} #credentials deleted
    sess.post(url, data = data)
    return sess

def ExtractText(unsorted_text):
    start = unsorted_text.find("<textarea>") + len("<textarea>")
    end = unsorted_text.find("</textarea>")
    return unsorted_text[start:end]
    
def FindText(content):
    soup = BeautifulSoup(content, 'html.parser')
    level_form = soup.find_all('div',class_='level-form')
    encrypted_text = level_form[0].find_all('textarea', attrs={'name': ''})
    encrypted_text = ExtractText(str(encrypted_text[0]))
    return encrypted_text
    
def Decrypt(input):
    answer = ''
    for word in input.split(','):
        if word != ' ':
            answer = answer + chr(94 - (int(word) - 32) + 32) # #visible_chars = 94
        else:
            answer = answer + ' '
    return answer
    
sess = Auth()
url = 'https://www.hackthis.co.uk/levels/coding/2'
html = sess.get(url)

encrypted_text = FindText(html.text)
answer = Decrypt(encrypted_text)

print('sending: ', answer)
payload = {'answer': answer}
res = sess.post(url, data = payload)
print(res)
