

a =[1,2,3,4,5,6,7,8,9]

def recurve(a):
    if(len(a) == 1):
        a[0] = 0
        return
    a[-1] = 0
    recurve(a[:-1])
    print('q',a,len(a))
    
recurve(a)
print(a)