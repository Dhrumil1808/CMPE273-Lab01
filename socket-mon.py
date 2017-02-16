import psutil
import collections
import itertools
import operator


d={}
l=[]
a=psutil.net_connections()
count=1;
m=0;

print '"' + "pid" +  '"' + "," + '"' + "laddr" + '"' + "," + '"' +  "raddr" + '"' +  "," + '"' +"status" + '"' 
for i in range(len(a)):
	if(len(a[i][4])!=0):
		m=m+1
		l.insert(m,a[i])
		
	
for k in range(len(l)):
	from operator import attrgetter	
	a_sort=sorted(l,key=lambda x:x[6])

for j in range(len(a_sort)):
	if(j > 0):
		if(a_sort[j][6]==a_sort[j-1][6]):
			count=count + 1
		elif(a_sort[j][6] != a_sort[j-1][6]):
			d[a_sort[j-1][6]]=count
			count=1

dict_sort  = sorted(d.items(), key=operator.itemgetter(0))
dictionary=sorted(dict_sort,key=operator.itemgetter(1),reverse=True)

for i in range(len(dictionary)):
	for j in range(len(a_sort)):
		if(dictionary[i][0]==a_sort[j][6]):
			print '"' + str(a_sort[j][6]) + '"' + "," + '"' + str(a_sort[j][3][0]) +"@"+str(a_sort[j][3][1]) + '"' + "," + str(a_sort[j][3][0]) +"@"+str(a_sort[j][3][1]) +'"' + '"' + "," + '"' + str(a_sort[j][5]) + '"'
		else:
			continue

			