import re
def codemeli (code):
    if not re.search(r'^\d{10}$', code):
        return False
    check = int(code[9])
    s = sum([int(code[x]) * (10 - x) for x in range(9)]) % 11
    if  (s < 2 and check == s) or (s >= 2 and check + s == 11):
        print(code)
with open('303.txt','r') as f:
    f1=f.readlines()
for x in f1:
    codemeli(x)

#f=open('file.txt','r')
#f1=f.readlines()
#f.close()
#use these instead of with open...
