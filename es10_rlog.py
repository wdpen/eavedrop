import os

if __name__=='__main__':
	dic={}
	fwr=open('/home/jack/alllog.txt','w')
	path='/home/log'
	files=os.listdir(path)
	for file in files:
		ff=os.path.join('/home/log',file)
		f=open(ff,'r')
		num=0
		a=[]
		for line in f.readlines():
			line=line.strip()
			num+=1
			if (num==2):
				a.append(str(line))
			if (num==3):
				a.append(str(line))
				break
		if (a[0] in dic) and (dic(a[0])==a[1]):
			continue
		if (a[0] in dic) and (dic(a[0])!=a[1]):
			fwr.write(a[0])
			fwr.write('\t')
			fwr.write(a[1])
			fwr.write('\n')
			continue
		if not (a[0] in dic):
			dic[a[0]]=a[1]
			fwr.write(a[0])
			fwr.write('\t')
			fwr.write(a[1])
			fwr.write('\n')			
		f.close()
	fwr.close()