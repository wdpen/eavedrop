import os

if __name__=='__main__':
	dicc={}
	fwr=open('/home/student_20194/jack/alllog.txt','w')
	path='/home/student_20194/log'
	files=os.listdir(path)
	for file in files:
		ff=os.path.join('/home/student_20194/log',file)
		f=open(ff,'r')
		num=0
		a=[]
		for line in f.readlines():
			line=line.strip()
			num+=1
			if (num==2):
				a.append(line)
			if (num==3):
				a.append(line)
				break
		if (a[0] in dicc) and (dicc[a[0]]==a[1]):
			print('hello')
			continue
		if (a[0] in dicc) and (dicc[a[0]]!=a[1]):
			fwr.write(a[0])
			fwr.write('\t')
			fwr.write(a[1])
			fwr.write('\n')
			continue
		if not (a[0] in dicc):
			dicc[a[0]]=a[1]
			fwr.write(a[0])
			fwr.write('\t')
			fwr.write(a[1])
			fwr.write('\n')			
		f.close()
	fwr.close()