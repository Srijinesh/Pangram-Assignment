z = str(input('enter a character string or sentence'))
r = 0
y = "abcdefghijklmnopqrstuvwxyz"
for i in y:
    if(i not in z.lower()):
        r+=1
        break
if(r==0):print('['+z+']','is a pangram')
else:print('['+z+']','is not a pangram')
