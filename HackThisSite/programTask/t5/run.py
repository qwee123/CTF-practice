import bz2
import time

corrupted_file = open("corrupted.png.bz2","rb")
data = []
counter = 0

while True:
    byte = corrupted_file.read(1).hex() #read 2 hex
    if byte == '':
        break
    data.append(byte)
corrupted_file.close()

def writeOutput(reserve_num_list):
    global data
    output_name = "recovered.png.bz2"
    output_file = open(output_name,"wb")
    count = 0
    for byte in data:
        if(byte == '--'):
            if(reserve_num_list[count] == 1):
                output_file.write(bytes.fromhex('0d'))
            count = count + 1
        else:
            output_file.write(bytes.fromhex(byte))
    output_file.close()
    return checkCorrupted(output_name)

def findRightmost(reserve_num_list):
    for index in reversed(range(len(reserve_num_list))):
        if reserve_num_list[index] == 1:
            return index
    return 0
        
def roundUp(reserve_num_list,round,deep):
    if(round == deep):
            return -1
    ri = findRightmost(reserve_num_list[:len(reserve_num_list) - round])

    if(ri == len(reserve_num_list)-round-1):
        reserve_num_list[ri] = 0
        restartIndex = roundUp(reserve_num_list,round+1,deep)
        if (restartIndex == -1):
            return -1
        reserve_num_list[restartIndex] = 1
        return restartIndex+1
    else:
        reserve_num_list[ri] = 0
        reserve_num_list[ri + 1] = 1
        return ri + 2
    
def runDeep(deep):
    global num_return
    reserve_num_list = [1]*deep + [0]*(num_return-deep)
    
    while True:
        if(writeOutput(reserve_num_list)):
            return True

        if(roundUp(reserve_num_list, 0, deep) == -1):
            return False
        
def bruteForceOutput():
    global num_return
    for deep in range(1,num_return+1):
        if(runDeep(deep)):
            break
    
def removeAllReturn():
    global data 
    
    count = 0
    index = 0
    while(index < len(data)):
        by = data[index]
        if (by == '0a' and index > 0 and data[index-1] == '0d'):
            data[index - 1] = '--'
            count = count + 1
        index = index + 1
    return count

def checkCorrupted(output_name):
    try:
        bz2.BZ2File(output_name).read()
        print("Recovered successed!")
        return True
    except:
        print("Recovered failed!")
        return False

num_return = removeAllReturn()
bruteForceOutput()
