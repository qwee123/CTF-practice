import requests
from bs4 import BeautifulSoup

def Sort(text):
    sorted_list = [text[0]]
    for word in text[1:]:
        
        sorted = False
        index = 0
        for index in range(len(sorted_list)):
            if(word < sorted_list[index]):
                sorted_list.insert(index, word)
                sorted = True
                break
            index = index + 1
        
        if(not sorted):
            sorted_list.append(word)
                
    return sorted_list

def Output(list):
    answer_sentence = list[0]
    for word in list[1:]:
        answer_sentence = answer_sentence + ', ' + word
    return answer_sentence

def Auth():
    sess = requests.Session()
    url = 'https://www.hackthis.co.uk/?login'
    data = {"username": "", "password": ""} #credentials deleted
    sess.post(url, data = data).text   
    return sess

def ExtractText(unsorted_text):
    start = unsorted_text.find("<textarea>") + len("<textarea>")
    end = unsorted_text.find("</textarea>")
    return unsorted_text[start:end]
    
def FindText(content):
    soup = BeautifulSoup(content, 'html.parser')
    level_form = soup.find_all('div',class_='level-form')
    unsorted_text = level_form[0].find_all('textarea', attrs={'name': ''})
    unsorted_text = ExtractText(str(unsorted_text[0]))
    return unsorted_text
    
sess = Auth()
url = 'https://www.hackthis.co.uk/levels/coding/1'
html = sess.get(url)

unsorted_text = FindText(html.text)
sorted_list = Sort(unsorted_text.split(', '))        
answer_sentence = Output(sorted_list)

print('sending: ',answer_sentence)
payload = {'answer': answer_sentence}
res = sess.post(url, data = payload)
print(res)