
morse_Table = {"-":"T",  "--":"M",  "---":"O",  "-----":"0",  "----.":"9",  "---..":"8",  "--.":"G",  "--.-":"Q",  "--..":"Z",  "--...":"7",
                "-.":"N",  "-.-":"K",  "-.--":"Y", "-.-.":"C",  "-..":"D",  "-..-":"X",  "-..-.":"/",  "-...":"B",  "-....":"6",  ".":"E",  "..":"I",
                "...":"S",  "....":"H",  ".....":"5",  "....-":"4",  "...-":"V",  "...--":"3",  "..-":"U",  "..-.":"F",  "..---":"2",  ".-":"A",  ".-.":"R",
                ".-..":"L",  ".--":"W",  ".--.":"P",  ".---":"J", ".----":"1", "/":" ", "--..--":",", ".-.-.-":".", "---...":":"}

def morseLookup(single_char):
    if single_char in morse_Table:
        return morse_Table[single_char]
    return '#' + single_char +'#' #no results
                
morse_code = open('input.txt','r')
words = morse_code.readline().split(' ')

answer = ''
for w in words:
    answer = answer + morseLookup(w)
print(answer)