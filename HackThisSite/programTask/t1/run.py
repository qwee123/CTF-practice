wordfile = open('wordlist.txt','r')
inputfile = open('input.txt','r')
wordslist = wordfile.read().split('\n')
inputlist = inputfile.read().split('\n')

def match(iw):
    for word in wordslist:
        if(len(word) == len(iw)):
            if(checkContain(word,iw)):                
                return word
        else:
            continue
            
    return "no result!"

def checkContain(ori_word,iw):
    for char in iw:
        index = ori_word.find(char)
        if(index == -1):
            return False
        ori_word = ori_word[:index]+ori_word[index+1:]
    return True
    
def formatOutput(answer):
    ans = ''
    for word in answer:
        ans = ans + word + ','
    return ans[:len(ans)-1]
    
answer = []
for iw in inputlist:
    answer.append(match(iw))

print(formatOutput(answer))
 

