import pickle
#import numpy
import math
with open ( 'documentlist.pickle' , 'rb' ) as picklefile:
	documentlist = pickle.load ( picklefile )
	picklefile.close ()
with open ( 'dictcontent.pickle' , 'rb' ) as picklefile:
	dictcontent = pickle.load ( picklefile )
	picklefile.close ()
idcount = 4008
termlong = len ( dictcontent )
print ( termlong )


for i in range ( 0 , idcount  ):
	with open ( 'document' + str( i ) + '.pickle' , 'wb' ) as picklefile:
		name = documentlist [ i ]
		a = {}
		print ( name ) 
		square = 0 
		for term in dictcontent:
			if ( name in dictcontent [ term ][ "posting"]):
				a[ term ] =  ( 1 + math.log ( dictcontent [ term ][ "posting"][ name ][ "tf"] , 10 ) )* math.log( idcount*1.0/dictcontent [ term ][ "df"] , 10 )
				square = square + a [ term ]*a [ term ] 

		a [ "sqrtsquare"] = math.sqrt ( square )		

		pickle.dump ( a , picklefile )
		picklefile.close ( )

 


