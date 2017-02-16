import psutil
import collections

a=psutil.net_connections()

print '"' + "pid" +  '"' + "," + '"' + "laddr" + '"' + "," + '"' +  "raddr" + '"' +  "," + '"' +"status" + '"' 
for i in range(len(a)):
	for j in range(len(a[i])):
		if(len(a[i][4]) != 0):
			from operator import itemgetter
			a.sort(key=lambda x:x[6])
			print '"' + str(a[i][6]) + '"' + "," + '"' + str(a[i][3][0]) +"@"+str(a[i][3][1]) + '"' + "," + '"' + str(a[i][4][0]) +"@"+str(a[i][4][1]) + '"' + "," + '"' + str(a[i][5]) + '"'
