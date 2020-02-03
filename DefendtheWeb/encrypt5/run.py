import time
substitution = {'j': 't','z': 'h','c': 's', 'f':'p', 'd':'a', 'y':'e', 't':'o'}

input = open('input.txt','r')
text = input.readline()
reversed_text = ''
for c in reversed(text):
    reversed_text = reversed_text + c.lower()
print(reversed_text)
#use this https://www.guballa.de/substitution-solver

'''
def Subs(text):
    answer = ''
    for c in text:
        if(c in substitution):
            answer = answer + substitution[c] + '.'
        else:
            answer = answer + c
    return answer

def CalWordFrequency(text):
    frequency = {}
    for c in text:
        frequency.setdefault(c,0)
        frequency[c] = frequency[c] + 1
    return frequency


    
freq_dict = CalWordFrequency(reversed_text)
print(sorted(freq_dict.items(), key=lambda d: d[1], reverse = True))

print(Subs(reversed_text))    
'''