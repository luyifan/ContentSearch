import glob 
import re
import os
import pickle
global dicttitle
global dictcontent
#global dictreply
global documentlist
global documentiddict
global idcount  
global titlelist
global urltxt
def dodictwithtitle ( filename ):
	global idcount 
	global documentiddict
	global dicttitle
	global documentlist
	global titlelist
	f = open ( filename , "r" )
	name = f.readline ( )
	urltxt [ name ] = filename 
	datalist = re.split(" |	|\n" ,f.read () )
	if not ( name in documentiddict ):
		idcount += 1
		documentiddict [ name ] = idcount
		documentlist.append ( name )
		
	for term in datalist:
		#term = term.replace (" " , "")
		#term = term.replace ("	" , "" )
		#term = term.replace ("\n" , "") 
		#print ( term )
		if ( term != "")and( term != "\n" )and( term != " "):
			#print ( term )
			if ( term in dicttitle ):
				posting = dicttitle [ term ][ "posting"] ;
				if ( titlelist [ term ][ -1 ] != idcount):					
					titlelist [ term ].append ( idcount )
				if ( name in posting ):
					posting [ name ][ "tf" ] += 1
				else:
					posting [ name ] = {}
					posting [ name ][ "tf" ] = 1
					dicttitle [ term ][ "df" ] += 1
			else:
				titlelist [ term ] = []
				titlelist [ term ].append ( idcount )
				dicttitle [ term ] = {}
				dicttitle [ term ][ "df" ] = 1
				dicttitle [ term ][ "posting" ] = {}
				dicttitle [ term ][ "posting" ][ name ] = {}
				dicttitle [ term ][ "posting" ][ name ][ "tf" ] = 1

def dodictwithcontent ( filename ):
	global idcount 
	global documentiddict
	global dictcontent
	f = open ( filename , "r" )
	name = f.readline ( )
	datalist = re.split(" |	|\n" ,f.read () )
	if not ( name in documentiddict ):
		print ( False )
	for term in datalist:
		#term = term.replace (" " , "")
		#term = term.replace ("	" , "" )
		#term = term.replace ("\n" , "") 
		#print ( term )
		if ( term != "")and( term != "\n" )and( term != " "):
			#print ( term )
			if ( term in dictcontent ):
				posting = dictcontent [ term ][ "posting"] ;
				if ( name in posting ):
					posting [ name ][ "tf" ] += 1
				else:
					posting [ name ] = {}
					posting [ name ][ "tf" ] = 1
					dictcontent [ term ][ "df" ] += 1
			else:
				dictcontent [ term ] = {}
				dictcontent [ term ][ "df" ] = 1
				dictcontent [ term ][ "posting" ] = {}
				dictcontent [ term ][ "posting" ][ name ] = {}
				dictcontent [ term ][ "posting" ][ name ][ "tf" ] = 1
'''
def dodictwithreply ( filename ):
	global idcount 
	global documentiddict
	global dictreply
	f = open ( filename , "r" )
	name = f.readline ( )
	datalist = re.split(" |	|\n" ,f.read () )
	if not ( name in documentiddict ):
		idcount += 1
		documentiddict [ name ] = idcount
		#print ( idcount )
		
	for term in datalist:
		#term = term.replace (" " , "")
		#term = term.replace ("	" , "" )
		#term = term.replace ("\n" , "") 
		#print ( term )
		if ( term != "")and( term != "\n" )and( term != " "):
			#print ( term )
			if ( term in dictreply ):
				posting = dictreply [ term ][ "posting"] ;
				if ( name in posting ):
					posting [ name ][ "tf" ] += 1
				else:
					posting [ name ] = {}
					posting [ name ][ "tf" ] = 1
					dictreply [ term ][ "df" ] += 1
			else:
				dictreply [ term ] = {}
				dictreply [ term ][ "df" ] = 1
				dictreply [ term ][ "posting" ] = {}
				dictreply [ term ][ "posting" ][ name ] = {}
				dictreply [ term ][ "posting" ][ name ][ "tf" ] = 1

'''
urltxt = {}
idcount = -1
documentlist = []
documentiddict = {}
titlelist = {}
filelist = os.listdir( "C:\\Spider\\title" )
dicttitle = {}
'''dodictwithtitle ( "C:\\Spider\\title\\1.txt" )

for term in dicttitle:
	print ( term )
	#print ( dicttitle[ term ][ "df"] )
	#print ( dicttitle[ term ][ "posting"])



print ( dicttitle )
'''
for filename in filelist:
	print ( filename )
	dodictwithtitle ( "C:\\Spider\\title\\" + filename )

with open ( 'dicttitle.pickle' , 'wb' ) as picklefile:
	pickle.dump ( dicttitle ,  picklefile )
	picklefile.close ()
#print ( dicttitle )

with open ( 'dicttitle.pickle' , 'rb' ) as picklefile:
	dicttitle = pickle.load ( picklefile )
	picklefile.close ()
'''for term in dicttitle:
	print ( term )
'''
dictcontent = {}
for filename in filelist:
	print ( filename )
	dodictwithcontent ( "C:\\Spider\\content\\" + filename )

with open ( 'dictcontent.pickle' , 'wb' ) as picklefile:
	pickle.dump ( dictcontent ,  picklefile )
	picklefile.close ()

with open ( 'dictcontent.pickle' , 'rb' ) as picklefile:
	dictcontent = pickle.load ( picklefile )
	picklefile.close ()
#for term in dictcontent:
#	print ( term )

with open ( 'documentlist.pickle' , 'wb') as picklefile:
	pickle.dump ( documentlist , picklefile )
	picklefile.close ( )
#for name in documentlist:
#	print ( name )

with open ( 'titlelist.pickle' , 'wb') as picklefile:
	pickle.dump ( titlelist  , picklefile )
	picklefile.close ( )

with open ( 'urltxt.pickle' , 'wb') as picklefile:

	pickle.dump ( urltxt  , picklefile )
	picklefile.close ( )

print ( idcount )

'''
dictreply = {}
for filename in filelist:
	print ( filename )
	dodictwithreply ( "C:\\Spider\\reply\\" + filename )

with open ( 'dictreply.pickle' , 'wb' ) as picklefile:
	pickle.dump ( dictreply ,  picklefile )
	picklefile.close ()

with open ( 'dictreply.pickle' , 'rb' ) as picklefile:
	dictreply = pickle.load ( picklefile )
	picklefile.close ()
#for term in dictreply:
#	print ( term )
'''