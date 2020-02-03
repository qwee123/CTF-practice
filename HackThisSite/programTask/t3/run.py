import hashlib

wordLibrarys = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                '1','2','3','4','5','6','7','8','9','0']
plainText = ''
passText = ''
#------------------------original encrypt funcs---------------------------------------
def evalCrossTotal(strMD5):
    intTotal = 0
    arrMD5Chars = list(strMD5)
    for char in arrMD5Chars:
        hexChar = int('0x0' + char,16)
        intTotal = intTotal + hexChar
    return intTotal

def encryptString(strString, strPasswordMD5):
    #strPasswordMD5 = hashlib.md5(strPassword.encode("utf-8")).hexdigest()
    intMD5Total = evalCrossTotal(strPasswordMD5)
    arrEncryptedValues = []
    intStrlen = len(strString)
    index = 0
    while index < intStrlen:
        arrEncryptedValues.append(ord(strString[index]) 
                                  +  int('0x0'+strPasswordMD5[index%32],16)
                                  - intMD5Total)
        md5Str = hashlib.md5(strString[:index+1].encode("utf-8")).hexdigest()
        md5Pass = hashlib.md5(str(intMD5Total).encode("utf-8")).hexdigest()
        intMD5Total = evalCrossTotal(md5Str[:16] + md5Pass[:16])
        index = index + 1
    catChar = ' '
    return catChar.join(str(e) for e in arrEncryptedValues)
    
#-----------------------------------------------------------------------------------
def verifyResult(strChar, passNum, total, roundIndex):
    guessTotal = ord(strChar) + passNum - total
    return guessTotal == inputNum[roundIndex]

def passwordStage(roundIndex, strChar, total, originalTotal):
    global passText
    pass_total = evalCrossTotal(passText)
    for passNum in range(0,16):
        if (pass_total + passNum <= originalTotal and verifyResult(strChar,passNum,total,roundIndex)):
            nextTotal = generateNextTotal(total)
            passText = passText + str(hex(passNum))[2:]
            bruteForce(roundIndex+1, nextTotal, originalTotal)
            passText = passText[:-1]

def middleCheck(strChar,total,roundIndex):
    temp_total = ord(strChar) - total
    return temp_total > inputNum[roundIndex] or temp_total + 15 < inputNum[roundIndex]

def specialCase(roundIndex):
    pos = roundIndex%20
    if (pos == 3 or pos == 7 or pos == 11 or pos == 15):
        return '-'
    elif (pos == 8):
        return 'O'
    elif (pos == 9):
        return 'E'
    elif (pos == 10):
        return 'M'
    elif (pos == 16 or pos == 18):
        return '1'
    elif (pos == 17):
        return '.'
    elif (pos == 19):
        return '\n'        
    else:
        return ''

def plainTextStage(roundIndex, total, originalTotal):
    global plainText
    strChar = specialCase(roundIndex)
            
    if (strChar != ''):
        plainText = plainText + strChar
        passwordStage(roundIndex, strChar, total, originalTotal)
        plainText = plainText[:-1]
    else:
        for strChar in wordLibrarys:
            if(middleCheck(strChar,total,roundIndex)): #already exceed! no need to guess password!
                continue
            plainText = plainText + strChar
            passwordStage(roundIndex, strChar, total, originalTotal)
            plainText = plainText[:-1]

def checkPassTotal(plainFirstChar):
    global passText 
    pass_total = evalCrossTotal(passText)
    original_total = ord(plainFirstChar) + int('0x0' + passText[0],16) - inputNum[0]
    return pass_total == original_total

def verifyChar(strChar, total, roundIndex):
    global plainText, passText
    plainText = plainText + strChar
    if (verifyResult(strChar, int(passText[roundIndex%32],16), total, roundIndex)):
        next_total = generateNextTotal(total)
        findRestPlainText(roundIndex + 1, next_total)
    plainText = plainText[:-1]

def findRestPlainText(roundIndex, total):
    if (roundIndex == 100):
        print(' >> ' + plainText) 
        return

    strChar = specialCase(roundIndex)
    
    if (strChar != ''):
        verifyChar(strChar, total, roundIndex)
    else:
        for strChar in wordLibrarys:
            verifyChar(strChar, total, roundIndex)       

def bruteForce(roundIndex, total, originalTotal):
    global plainText, passText
    if (roundIndex == 32):
        if(checkPassTotal(plainText[0])):
            print(plainText)
            print('Pass: ' + passText)
            print('-----------go to next stage---------------------')
            findRestPlainText(roundIndex, total)
        return
    
    plainTextStage(roundIndex, total, originalTotal)
    
def generateNextTotal(roundTotal):
    global plainText
    strHash = hashlib.md5(plainText.encode("utf-8")).hexdigest()
    totalHash = hashlib.md5(str(roundTotal).encode("utf-8")).hexdigest()
    return evalCrossTotal(strHash[:16] + totalHash[:16])
    
def startBruteForce():
    global plainText, passText
    #guess char0 and pass0(base16) to compute the total0, then move to next round
    startRoundIndex = 0
    for strChar0 in wordLibrarys:
        print(strChar0)
        for passNum0 in range(0,16):
            total0 = ord(strChar0) + passNum0 - inputNum[startRoundIndex]
            plainText = strChar0
            nextTotal = generateNextTotal(total0)
            passText = str(hex(passNum0))[2:]
            bruteForce(startRoundIndex + 1, nextTotal, total0)

def decrypt(encryptNums):
    startBruteForce()

inputFile = open('encryptedText.txt', 'r')
inputNum = inputFile.read().split(' ')
inputFile.close()

for index in range(len(inputNum)):
    inputNum[index] = int(inputNum[index])

decrypt(inputNum)
#print(encryptString('R01-D99-OEM-AHD-1.1\nWZO-WTK-OEM-YWS-1.1\n8BI-A5R-OEM-04Y-1.1\nV7Q-5YQ-OEM-6CZ-1.1\nFOH-TKG-OEM-IHA-1.1\n','1aa12eb9bcf0a9551c772d3468c38f30'))
'''
-146 -161 -174 -124 -176 -165 -136 -193 -134 -113 -137 -194 -143 -188 -150 -126 -197 -218 -225 -203 
-188 -114 -142 -178 -117 -205 -159 -184 -163 -158 -164 -185 -135 -118 -125 -251 -150 -186 -192 -204 
-124 -138 -194 -248 -203 -196 -95 -164 -154 -198 -124 -153 -181 -149 -147 -155 -187 -140 -178 -239 
-115 -150 -157 -206 -163 -112 -126 -179 -164 -168 -131 -160 -175 -156 -135 -203 -213 -171 -220 -253 
-198 -128 -160 -204 -161 -176 -191 -189 -180 -196 -123 -158 -182 -133 -246 -210 -206 -187 -168 -201
'''

'''
def bruteForce(roundIndex, curPlainText, total, passText):
    if (roundIndex == 4):
        print(curPlainText + ' ' + passText)
        return True
    
    for strChar in wordLibrarys:
        for passNum in range(0,16):
            if (verifyResult(strChar,passNum,total,roundIndex)):
                nextTotal = generateNextTotal(curPlainText,total)
                if(bruteForce(roundIndex+1, curPlainText + strChar, nextTotal, passText + str(hex(passNum))[2:])):
                    return True
    return False
''' 
