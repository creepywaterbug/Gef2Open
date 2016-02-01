import os
import hashlib
import ast
from random import randint
import pickle
import re
import UtlGefOpen,UtlGef2
import UtlGef

def randList(cnt):
	tel=0;mylst=[]
	while tel<=cnt:
		#choice=randint(0,len(mydict))
		choice=randint(0,len(mydict)-1)
		if choice not in mylst:
			mylst.append(choice)
			tel=tel+1
	return mylst

def GetAllFunctions():
	FunctionList=[\
	'Gbr_Is_Gbr()',\
	'Gcr_Is_Gcr()',\
	'Get_CompanyID_Flag()',\
	'Get_Column()',\
	'Get_Column_Flag()',\
	'Get_CompanyID_Name()',\
	'Get_Data(i_Kol, iRij)',\
	'Get_MeasurementText_Flag(1)',\
	'Get_MeasurementText_Flag(15)',\
	'Get_MeasurementVar_Flag(1)',\
	'Get_MeasurementVar_Flag(15)',\
	'Get_MeasurementText_Tekst(1)',\
	'Get_MeasurementText_Tekst(15)',\
	'Get_MeasurementVar_Value(1)',\
	'Get_MeasurementVar_Value(15)',\
	'Get_Nr_Scans()',\
	'Get_Parent_Flag()',\
	'Get_Parent_Reference()',\
	'Get_ProcedureCode_Flag()',\
	'Get_ProcedureCode_Code()',\
	'Get_ProjectID_Flag()',\
	'Get_ProjectID_Number()',\
	'Get_ReportCode_Flag()',\
	'Get_ReportCode_Code()',\
	'Get_StartDate_Flag()',\
	'Get_StartDate_Yyyy()',\
	'Get_StartDate_Mm()',\
	'Get_StartDate_Dd()',\
	'Get_XYID_Flag()',\
	'Get_XYID_X()',\
	'Get_XYID_Y()',\
	'Get_ZID_Flag()',\
	'Get_ZID_Z()',\
	'Qn2Column(1)',\
	'Qn2Column(11)',\
	]
	return FunctionList


def tryUtlGef(mytype,functie):
	try:
		return eval('%s.%s'%(mytype,functie))
	except:
		return 'GeenResult'

def CompareGefTools(gefbestand,gefnaam,function):
	try:
		c2=tryUtlGef('UtlGef2',function)
		c3=tryUtlGef('UtlGef',function)
		MyLog.write('"%s";"%s";"%s";"%s"\n'%(gefnaam,function,c2,c3))
		return 'gelukt'
	except:
		MyLog.write('ergaatietsfout in %s-%s\n'%(gefnaam,function))
		return 'ergaatietsfoutin %s'%(gefnaam)
#

def getBestanden(mylocs):
	MyOut = open('MyOut.txt','w')
	MyOut.write('{')
	MyOut.close()
	mygefs1=[];myhashes=[];
	#mygefs2={}
	tel=0
	for myloc in mylocs:
		myfiles=os.listdir(myloc)
		tel2=0
		for myfile in myfiles:
			tel2=tel2+1
			MyOut = open('MyOut.txt','a')
			if myfile.lower()[-3:]=='gef':
				mygef=myfile[:-4]
				myhash = hashlib.md5(open('%s\\%s'%(myloc,myfile),'rb').read()).hexdigest()
				if mygef not in mygefs1 and myhash not in myhashes:
					tel=tel+1
					mygefs1.append(mygef)
					myhashes.append(myhash)
					print '%s: %s'%(tel,mygef)
					if tel==1:
						MyOut.write("'%s':{'gefnaam':'%s','gefloc':'%s\\\\%s','hash':'%s'}"%(mygef,mygef,myloc,myfile,myhash))
					else:
						MyOut.write(",'%s':{'gefnaam':'%s','gefloc':'%s\\\\%s','hash':'%s'}"%(mygef,mygef,myloc,myfile,myhash))
			MyOut.close()
	MyOut= open('MyOut.txt','a')
	MyOut.write('}')
	MyOut.close()
	return 'bestanden staan in MyOut.txt'

## Variabelen die in de FunctieTests zelf worden gebruikt
MyLog = open('MyLog.txt','w')
mylocs=[r'C:\\Users\\rvanderhelm\\ownCloud\\foutgefs']
#Main
myFunctions = GetAllFunctions()
#getBestanden(mylocs) #is uitgevoerd. info over gefbestanden staat in 'MyOut.txt'
a=open('MyOut.txt','r')
mydict=ast.literal_eval(a.readlines()[0])
a.close()
#a=open('randlist','w')
#a.write(str(randList(1000)))
#a.close()
a=open('randlist','r')
randList=ast.literal_eval(a.readlines()[0])
gefnaams=[]
for i in randList:
	mykey=mydict.keys()[i]
	gefnaams.append(mykey)
a=open('gefnaams','w')
a.write(str(gefnaams))
a=open('gefnaams','r')
UtlGef.Init_Gef()
gefnaams=ast.literal_eval(a.readlines()[0])
for mykey in gefnaams:
#for mykey in ['B28-130A']:
	myval=mydict[mykey]
	GefBestand=myval['gefloc']
	MyLog2 = open("MyLog2.txt","w")
	MyLog2.write(GefBestand)
	MyLog2.close()
	GefNaam=myval['gefnaam']
	print GefBestand
	headerdict=UtlGefOpen.headerdict(GefBestand)
	fp = open("tmpheaderdict.pkl","w")
	pickle.dump(str(headerdict), fp)
	fp.close()
	UtlGef.Read_Gef(GefBestand)
	for myFunction in myFunctions:
			print CompareGefTools(GefBestand,GefNaam,myFunction)
	b3b="UtlGef.Test_Gef('HEADER')"
	b3c="UtlGef.Test_Gef('DATA')"
	b3d="UtlGef.Test_Gef('GEF-CPT-Report')"
	b3e="UtlGef.Test_Gef('GEF-BORE-Report')"
	b3i='UtlGef.Is_Plotable()'
	c3b=tryUtlGef('UtlGef',b3b)
	c3c=tryUtlGef('UtlGef',b3c)
	c3d=tryUtlGef('UtlGef',b3d)
	c3e=tryUtlGef('UtlGef',b3e)
	c3i=tryUtlGef('UtlGef',b3i)
	MyLog.write('"%s";"%s";"%s";"%s"\n'%(GefNaam,b3b,"NietGetest",c3b))
	MyLog.write('"%s";"%s";"%s";"%s"\n'%(GefNaam,b3c,"NietGetest",c3c))
	MyLog.write('"%s";"%s";"%s";"%s"\n'%(GefNaam,b3d,"NietGetest",c3d))
	MyLog.write('"%s";"%s";"%s";"%s"\n'%(GefNaam,b3e,"NietGetest",c3e))
	MyLog.write('"%s";"%s";"%s";"%s"\n'%(GefNaam,b3i,"NietGetest",c3i))
MyLog.close()
