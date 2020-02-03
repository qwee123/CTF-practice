
substitution = {'h':'a', 'l':'s', 'J':'P', 'c':'i', 'q':'e', 'g':'t', 'd':'h', 'G':'t', 'D':'H', 'u':'w', 'k':'d', 'y':'c', 'o':'g', 'm':'n', 'a':'f',
            'n':'r', 'r':'m', 's':'l', 'z':'o', 'w':'v'}

input_file = open("input.txt",'r')
input_text = input_file.readline()

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
    
freq_dict = CalWordFrequency(input_text)
print(sorted(freq_dict.items(), key=lambda d: d[1], reverse = True))
print(Subs(input_text))    
