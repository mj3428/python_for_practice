queryString = 'rnd=4868944880959973&authType=10&id=448809'
strs = queryString.split("&")
print(str)
strs.sort()
vals = ''
for i in range(len(strs)):
    vals = vals+strs[i].split("=")[1]
print(vals)
