
input = open('input.txt','r')
text = input.readline()
for c in reversed(text):
    print(c,end='')