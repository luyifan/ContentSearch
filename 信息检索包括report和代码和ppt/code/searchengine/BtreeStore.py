import pickle
class Btree:
    def __init__ ( self , anum = 0 , aleaf = 1 ):
        self.num = anum
        self.leaf = aleaf
        self.key = []
        self.c = []
        for i in range ( kk - 1):
            self.key.append ( None )
        for i in range ( kk ):
            self.c.append ( None )

def search ( x , o ):
    i = 0
    #print ( o  )
    #print ( x.key )
    while (( i < x.num )and( o > x.key [ i ] )):
        i = i + 1
    #print ( x.c[ i ]  )
    if (( i < x.num ) and ( o == x.key [ i ] )):
        print ( "Yes ," + o + " is in Btree" )
        return 1 
    if (( x.leaf != 1 )and( x.c[ i ] != None )):
        return search ( x.c[ i ] , o )
    else:
        print ( "No ," + o + " is not in Btree")
        return 0 

def searchbetween ( x , left , right ):
    i = 0
    listword = [] 
    while (( i < x.num )and ( left > x.key[ i ] )):
        i = i + 1 
    while (( i < x.num) and ( right > x.key [ i ] )):
        listword.append( x.key[ i ] )
        if (( x.leaf != 1 )and( x.key[ i ] > left )and( x.c[ i ] != None )):
            listword = listword + searchbetween ( x.c[ i ] , left , right  )
        i = i + 1
    if (( x.leaf != 1 )and((( i < x.num )and( right <= x.key [ i ]))or( i == x.num ))and( x.c[ i ] != None )):
        listword = listword + searchbetween (  x.c[ i ] , left , right )
    return listword 

def insert ( x , o ):
    if ( x.num == kk - 1 ):
        s = Btree ( 0 , 0 )
        s.c[ 0 ] = x 
        split_child ( s , 0 , x )
        insert_nofull ( s , o )
        return s
    else:
        insert_nofull ( x , o )
        return x 

def split_child ( x , t , y ):
    z = Btree ( 0 , y.leaf )
    for i in range ( k - 1 ):
        z.key[ i ] =  y.key[ i + k ]
        y.key[ i + k ] = None
    #print ( y.num )
    for i in range ( k ):
        z.c [ i ] =  y.c[ i + k ]
        y.c [ i + k ] = None
    z.num = k - 1
    y.num = k - 1

    i = x.num - 1
    while ( i >= t ):
        x.key [ i + 1 ] = x.key [ i ]
        i = i - 1 
    x.key [ t ] = y.key [ k - 1 ]
    y.key [ k - 1 ] = None 
    i = x.num
    while ( i >= t+1 ):
        x.c [ i + 1] = x.c [ i  ]
        i = i - 1
    x.c[ t ] = y
    x.c[ t + 1 ] = z
    x.num = x.num + 1
    #print ( x.key ) 
    #print ( x.key )
    #print ( y.key )
    #print ( z.key )

def insert_nofull ( x , o ):
    i = 0
    #print ( o )
    while (( i < x.num )and ( x.key [ i ] < o )):
        i = i + 1
    if ((i < x.num )and( o == x.key [ i ] )):
        #print ( o + "already exist\n" )
        return
    if ( x.leaf == 1 ):
        j = x.num - 1
        while ( j >= i ):
            x.key[ j + 1 ] = x.key [ j ]
            j = j - 1
        x.key [ i ] = o
        x.num = x.num + 1
    else:
        if ( x.c[ i ].num == kk -1 ):
            split_child ( x , i , x.c[ i ] )
            if ( o > x.key [ i ] ):
                insert_nofull ( x.c[ i + 1 ] , o )
            elif ( o < x.key [ i ] ):
                insert_nofull ( x.c[ i ] , o )
            else:
                #print ( o + "already exist\n" )
                return
        else:
            insert_nofull ( x.c[ i ] , o )
    #print ( x.key )
    

def getoldword ( word ):
    listword = word.split("$")
    return listword[ 1 ] + listword [ 0 ]

global k
global kk
k = 2
kk = 2*k
global root
root = Btree ( 0 , 1 )

with open ( 'dicttitle.pickle' , 'rb' ) as picklefile:
	dicttitle = pickle.load ( picklefile )
	picklefile.close ()

for term in dicttitle:
	l = len ( term )
	newword = term + '$'
	#print ( newword )
	root = insert ( root , newword )
	for i in range ( l ):
		oldword = newword [ l ] +newword [ 0:l ]
		#print ( oldword )
		root = insert ( root , oldword )
		#print ( getoldword ( oldword ))
		newword = oldword

with open ( 'dictcontent.pickle' , 'rb' ) as picklefile:
    dicttitle = pickle.load ( picklefile )
    picklefile.close ()

for term in dicttitle:
    l = len ( term )
    newword = term + '$'
    #print ( newword )
    root = insert ( root , newword )
    for i in range ( l ):
        oldword = newword [ l ] +newword [ 0:l ]
        #print ( oldword )
        root = insert ( root , oldword )
        #print ( getoldword ( oldword ))
        newword = oldword

'''
with open ( 'dictreply.pickle' , 'rb' ) as picklefile:
    dicttitle = pickle.load ( picklefile )
    picklefile.close ()

'''
for term in dicttitle:
    l = len ( term )
    newword = term + '$'
    #print ( newword )
    root = insert ( root , newword )
    for i in range ( l ):
        oldword = newword [ l ] +newword [ 0:l ]
        #print ( oldword )
        root = insert ( root , oldword )
        #print ( getoldword ( oldword ))
        newword = oldword

with open ( 'Btree.pickle' , 'wb' ) as picklefile:
    pickle.dump ( root , picklefile )
    picklefile.close ( ) 

#print ( True )