import string
t=[]
fp=open('emma.txt')
for line in fp:
    line=line.replace('-',' ')
    for l in string.punctuation:
        line=line.replace(l,'')
    for i in line.split():
        i = i.strip(string.punctuation + string.whitespace)
        i=i.lower()
        t.append(i)
t.sort()
d={}
count=1
d.setdefault(t[0],1)
for i in range(1,len(t)):
    if t[i]==t[i-1]:
        count +=1
        d[t[i]]=count
    else:
        count=1
        d.setdefault(t[i],1)
c=[]
for m,n in d.items():
    c.append((m,n))
c=sorted(c,key=lambda x:x[1],reverse=True)

for (m,n) in c[:10]:
    print(m,n)
print(len(c),sum(d.values()))
