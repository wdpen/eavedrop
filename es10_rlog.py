import os

if __name__=='__main__':
	if ('1' in sys.argv[1:]):
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
			dicc[a[0]]=a[1]
			fwr.write(a[0])
			fwr.write(' ')
			fwr.write(a[1])
			fwr.write('\n')			
			f.close()
		fwr.close()
	if ('2' in sys.argv[1:]):
		gett=input('name to get password: ')
		fwr=open('logdata.txt','w')
		for line in fwr.readlines:
			if line[0]==gett:
				print(line[1])
		fwr.close()
