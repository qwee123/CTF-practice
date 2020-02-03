import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

morse_Table = {"-":"T",  "--":"M",  "---":"O",  "-----":"0",  "----.":"9",  "---..":"8",  "--.":"G",  "--.-":"Q",  "--..":"Z",  "--...":"7",
                "-.":"N",  "-.-":"K",  "-.--":"Y", "-.-.":"C",  "-..":"D",  "-..-":"X",  "-..-.":"/",  "-...":"B",  "-....":"6",  ".":"E",  "..":"I",
                "...":"S",  "....":"H",  ".....":"5",  "....-":"4",  "...-":"V",  "...--":"3",  "..-":"U",  "..-.":"F",  "..---":"2",  ".-":"A",  ".-.":"R",
                ".-..":"L",  ".--":"W",  ".--.":"P",  ".---":"J", ".----":"1"}

def isBlack(pix):
    return (pix[0]==0.0 and pix[1]==0.0 and pix[2]==0.0)

def morseDecode(code):
    decode_str = ''
    single_char = ''
    for c in code:
        if c != ' ':
            single_char = single_char + c
        else:
            decode_char = morseLookup(single_char)
            single_char=''
            decode_str = decode_str + decode_char
    return decode_str
    
def morseLookup(single_char):
    if single_char in morse_Table:
        return morse_Table[single_char]
    return '#' + single_char +'#' #no results

pic = mpimg.imread("下載.png")

answer_morse_code = []
index = 0
for row in pic:
    for pix in row:
        if(not isBlack(pix)):
            answer_morse_code.append(chr(index))
            index = 0
        index = index + 1

print(morseDecode(answer_morse_code))