a="he is a boy and he have a "
b="she is a  girl man give promises month in the techi"
c="i found a pen give "

m="{} {} {}".format(a,b,c)
print(m)
c=m.split()
#print(c)
repeated=[]
for i in range(0,len(c)):
	k=i+1
	for j in range(k,len(c)):
		if c[i]==c[j] and c[i] not in repeated:
			repeated.append(c[i])
#print("dupicate values:",repeated)
A=set(repeated)
B=set(c)
#print(A)
#print(B)
hover=B.difference(A)
#print("unique values",hover)
m=list(repeated)
k=list(hover)
str1=", ".join(m)
str2=",".join(k)
print("duplicate: {}".format(str1))
print("uniques: {}".format(str2))
