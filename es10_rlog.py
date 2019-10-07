import os, sys

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
	elif ('2' in sys.argv[1:]):
		namelist=[]
		#fwr=open('logdata.txt','r')
		fwr=open('/home/student_20194/jack/alllog.txt','r')
		for line in fwr.readlines():
			lss=line.split(' ')
			if lss[0] in namelist:
				continue
			else:
				namelist.append(lss[0])
				sys.stdout.write(lss[0])
				sys.stdout.write('  ')
		fwr.close()
		gett=input('\nname to get password: ')
		#fwr=open('logdata.txt','r')
		fwr=open('/home/student_20194/jack/alllog.txt','r')
		dicn={}
		for line in fwr.readlines():
			lss=line.split(' ')
			ss=lss[1]
			for k in list(range (2, len(lss))):
				ss=ss+' '+lss[k]
			if lss[0]==gett:
				#print(len(lss))
				if (ss in dicn):
					dicn[ss]+=1
				else:
					dicn[ss]=1
		print(len(dicn))
		for k,v in dicn.items():
			sys.stdout.write(str(v))
			sys.stdout.write(' ')
			sys.stdout.write(k)
		fwr.close()
	elif ('3' in sys.argv[1:]):
		namelist=[]
		fwr=open('/home/student_20194/jack/alllog.txt','r')
		for line in fwr.readlines():
			lss=line.split(' ')
			if lss[0] in namelist:
				continue
			else:
				namelist.append(lss[0])
		fwr.close()
		
		for nam in namelist:
			dicn={}
			#print(nam)
			fwr=open('/home/student_20194/jack/alllog.txt','r')
			for line in fwr.readlines():
				lss=line.split(' ')
				ss=lss[1]
				for k in list(range (2, len(lss))):
					ss=ss+' '+lss[k]
				if lss[0]==nam:
					if (ss in dicn):
						dicn[ss]+=1
					else:
						dicn[ss]=1
			maxv=0; maxk=0
			for k,v in dicn.items():
				if v>maxv:
					maxv=v; maxk=k
			sys.stdout.write(nam)
			sys.stdout.write(' ')
			sys.stdout.write(maxk)
			fwr.close()
	else:
		print('Need input 1 , 2 or 3')
