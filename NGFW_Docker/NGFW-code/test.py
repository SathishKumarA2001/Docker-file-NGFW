import re
count =0
iplist = open("subnet.txt", "r")
for IP in iplist:
    IP = IP.strip()
    x = re.search("\A2.59.", IP)
    if x:
        count=count+1
print(count)