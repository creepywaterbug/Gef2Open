import os
import hashlib
import ast
from random import randint
import pickle
import re
#import UtlGef
import Gef2Open,Gef2Config

def randList(cnt):
	tel=0;mylst=[]
	while tel<=cnt:
		choice=randint(0,len(mydict)-1)
		if choice not in mylst:
			mylst.append(choice)
			tel=tel+1
	return mylst

#def tryUtlGef(mytype,functie):
def tryUtlGef(functie):
	try:
		#return eval('%s.%s'%(mytype,functie))
		return eval('UtlGef.%s'%(functie))
	except:
		return 'GeenResult'

def tryGef2Open(functie):
	myResult = eval('Gef2Open.%s'%(functie))
	if myResult not in [None,False,True] and 'Error:' in str(myResult):
		myResult=None
	try:
		return myResult 
	except:
		return 'GeenResult'
# Met deze functie converteer ik functienaam van UtlGef.py naar die van 
# Gef2.dll/Gef2Open.py Dit om te voorkomen dat ik de inhoud van andermans
# scripts moet gaan aanpassen
def ChangetoFunctienaamGef2(functie):
	mydict={\
	'gbr_is_gbr':'gbr_is_gbr',\
	'gcr_is_gcr':'gcr_is_gcr',\
	'get_companyid_flag':'get_companyid_flag',\
	'get_column':'get_column',\
	'get_column_flag':'get_column_flag',\
	'get_companyid_name':'get_companyid_Name',\
	'get_data':'get_data',\
	'get_measurementtext_flag':'get_measurementtext_flag',\
	'get_measurementvar_flag':'get_measurementvar_flag',\
	'get_measurementtext_tekst':'get_measurementtext_Tekst',\
	'get_measurementvar_value':'get_measurementvar_Value',\
	'get_nr_scans':'get_nr_scans',\
	'get_parent_flag':'get_parent_flag',\
	'get_parent_reference':'get_parent_reference',\
	'get_procedurecode_flag':'get_procedurecode_flag',\
	'get_procedurecode_code':'get_procedurecode_Code',\
	'get_projectid_flag':'get_projectid_flag',\
	'get_projectid_number':'get_projectid_Number',\
	'get_reportcode_flag':'get_reportcode_flag',\
	'get_reportcode_code':'get_reportcode_Code',\
	'get_startdate_flag':'get_startdate_flag',\
	'get_startdate_yyyy':'get_startdate_Yyyy',\
	'get_startdate_mm':'get_startdate_Mm',\
	'get_startdate_dd':'get_startdate_Dd',\
	'get_xyid_flag':'get_xyid_flag',\
	'get_xyid_x':'get_xyid_X',\
	'get_xyid_y':'get_xyid_Y',\
	'get_zid_flag':'get_zid_flag',\
	'get_zid_z':'get_zid_Z',\
	'init_gef':'init_gef',\
	'qn2column':'qn2column',\
	'read_gef':'read_gef',\
	'is_plotable':'is_plotable',\
	'test_gef':'test_gef'
	}
	functienaamlower=str.lower(re.sub('(^.*)\(.*$','\\1',functie))
	functierest=re.sub('^.*(\(.*)','\\1',functie)
	try:
		functienaamGef2=mydict[functienaamlower]
		return '%s%s'%(functienaamGef2,functierest)
	except:
		return 'gaatfout'

def CompareGefTools(gefbestand,gefnaam,function):
	try:
		print 'function: %s'%(function)
		functieGef2 = ChangetoFunctienaamGef2(function)
		c2=tryGef2Open(functieGef2)
		#c3=tryUtlGef(function)
		c3='weggelaten'
		MyVglResult.write('"%s";"%s";"%s";"%s"\n'%(gefnaam,functieGef2,c2,c3))
		return 'gelukt'
	except:
		MyVglResult.write('ergaatietsfout in %s-%s\n'%(gefnaam,functieGef2))
		return 'ergaatietsfoutin %s'%(gefnaam)

def getBestanden(mylocs):
	MyGefFiles = open('MyGefFiles.txt','w')
	MyGefFiles.write('{')
	MyGefFiles.close()
	mygefs1=[];myhashes=[];
	tel=0
	for myloc in mylocs:
		myfiles=os.listdir(myloc)
		tel2=0
		for myfile in myfiles:
			tel2=tel2+1
			MyGefFiles = open('MyGefFiles.txt','a')
			if myfile.lower()[-3:]=='gef':
				mygef=myfile[:-4]
				#myhash = hashlib.md5(open('%s\\%s'%(myloc,myfile),'rb').read()).hexdigest()
				myhash = hashlib.md5(open('%s/%s'%(myloc,myfile),'rb').read()).hexdigest()
				if mygef not in mygefs1 and myhash not in myhashes:
					tel=tel+1
					mygefs1.append(mygef)
					myhashes.append(myhash)
					if tel==1:
#						MyGefFiles.write("'%s':{'gefnaam':'%s','gefloc':'%s\\\\%s','hash':'%s'}"%(mygef,mygef,myloc,myfile,myhash))
						MyGefFiles.write("'%s':{'gefnaam':'%s','gefloc':'%s//%s','hash':'%s'}"%(mygef,mygef,myloc,myfile,myhash))
					else:
#						MyGefFiles.write(",'%s':{'gefnaam':'%s','gefloc':'%s\\\\%s','hash':'%s'}"%(mygef,mygef,myloc,myfile,myhash))
						MyGefFiles.write(",'%s':{'gefnaam':'%s','gefloc':'%s//%s','hash':'%s'}"%(mygef,mygef,myloc,myfile,myhash))
			MyGefFiles.close()
	MyGefFiles= open('MyGefFiles.txt','a')
	MyGefFiles.write('}')
	MyGefFiles.close()
	return 'bestanden staan in MyGefFiles.txt'

## Variabelen
MyVglResult = open('MyVglResult.txt','w')
mylocs=Gef2Config.Locaties()
myFunctions = Gef2Config.Functies()
## Main
getBestanden(mylocs) # info over gefbestanden wordt geplaatst in 'MyGefFiles.txt'
a=open('MyGefFiles.txt','r')
mydict=ast.literal_eval(a.readlines()[0])
a.close()
gefnaams=[]
randList=randList(40)
for i in randList:
	mykey=mydict.keys()[i]
	gefnaams.append(mykey)
#UtlGef.Init_Gef()
for mykey in gefnaams:
	print 'mykey: %s'%(mykey)
	myval=mydict[mykey]
	GefBestand=myval['gefloc']
	GefNaam=myval['gefnaam']
	Gef2Open.read_gef(GefBestand)
	#UtlGef.Read_Gef(GefBestand)
	for myFunction in myFunctions:
			CompareGefTools(GefBestand,GefNaam,myFunction)
MyVglResult.close()
