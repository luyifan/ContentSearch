import pickle
import jieba
import re
import numpy
import math
import yate
import glob
import cgi
import cgitb
cgitb.enable()
form_data = cgi.FieldStorage ( )
global kkk
global kk
kkk = 2
kk = 2*kkk
global root

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
    for i in range ( kkk - 1 ):
        z.key[ i ] =  y.key[ i + kkk ]
        y.key[ i + kkk ] = None
    #print ( y.num )
    for i in range ( kkk ):
        z.c [ i ] =  y.c[ i + kkk ]
        y.c [ i + kkk] = None
    z.num = kkk - 1
    y.num = kkk - 1

    i = x.num - 1
    while ( i >= t ):
        x.key [ i + 1 ] = x.key [ i ]
        i = i - 1 
    x.key [ t ] = y.key [ kkk - 1 ]
    y.key [ kkk - 1 ] = None 
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

def OrOperation(Blist):
    list1=titlelist[Blist[0]]
    for i in range(1,len(Blist)):
        if not ( Blist[ i ] in titlelist):
            continue 
        list2=titlelist[Blist[i]]
        list3=[]
        p=0
        q=0
        l1=len(list1)
        l2=len(list2)
        while ((p<l1) and (q<l2)):
            if (list1[p]==list2[q]):
                list3.append(list1[p])
                q=q+1
                p=p+1
            elif (list1[p]<list2[q]):
                list3.append(list1[p])
                p=p+1
            elif (list1[p]>list2[q]):
                list3.append(list2[q])
                q=q+1
        while ( q < l2 ):
            list3.append ( list2[ q ])
            q = q + 1 
        while ( p < l1 ):
            list3.append ( list1 [ p ])
            p = p + 1 
 
        list1=list3
    return list1

def AndOperation(list1,list2):
    list3=[]
    p=0
    q=0
    l1=len(list1)
    l2=len(list2)
    while ((p<l1) and(q<l2)):
        if (list1[p]==list2[q]):
            list3.append(list1[p])
            q=q+1
            p=p+1
        elif (list1[p]<list2[q]):
            p=p+1
        elif (list1[p]>list2[q]):
            q=q+1
    list1=list3
    return list1
print ( yate.start_response ())
print ( yate.include_header ( "Welcome to Shy Search of CC98" ))
def downheap ( i , sum ):
    x = valuelist [ i ]
    y = heaplist [ i ] 
    j = i*2 
    while ( j <= sum ):
        if ( j + 1 <= sum )and( valuelist [ j + 1 ] < valuelist [ j ] ):
            j += 1
        if ( x > valuelist [ j ] ):
            valuelist [ i ] = valuelist [ j ] 
            heaplist [ i ] = heaplist [ j ] 
            i = j 
            j = j*2 
        else:
            break 
    valuelist [ i ] = x 
    heaplist [ i ] = y

with open ( 'titlelist.pickle' , 'rb' ) as picklefile:
    titlelist = pickle.load ( picklefile )
    picklefile.close ()

with open ( 'documentlist.pickle' , 'rb' ) as picklefile:
    documentlist = pickle.load ( picklefile )
    picklefile.close ()

with open ( 'urltxt.pickle' , 'rb' ) as picklefile:
    urltxt = pickle.load ( picklefile )
    picklefile.close ()


    
str1 = form_data[ "content"].value
#print ( str1 )
count = 0
empty = 0
topk = 10
idcount = 4008
list1 = []

if not ( '*' in str1 ):
    
    #print ( str1 )
    list1 = jieba.cut ( str1 , cut_all = True )
    str1 = " ".join(list1)
    list1 = re.split( " | |\n" ,str1 )
    datalist = []
    for term in list1:
        if ( term != ''):
            datalist.append ( term )
    #print ( datalist )
    termlen = len ( datalist )
    if ( termlen == 0 ):
        empty = 1
    #print ( datalist )    
    #print ( list1 )
    if ( datalist[ 0 ] in titlelist ):
        list1 = titlelist [ datalist [ 0 ] ]
    else:
        list1 = []
    #print ( list1 )
    for i in range ( 1 , termlen ):
        if ( list1 == []):
            break 
        if ( datalist [ i ] in titlelist):
            list2 =  titlelist [ datalist [ i ] ]
        else:
            list1 = []
            break
        #print ( list2 )
        list3 = []
        j = 0 
        k = 0
        l1 =len ( list1 )
        l2 =len ( list2 ) 
        while (( j < l1 )and ( k < l2 )):
            if ( list1[ j ] == list2 [ k ] ):
                list3.append ( list1[ j ])
                j += 1 
                k += 1
            elif ( list1[ j ] < list2[ k ] ):
                j += 1
            elif ( list1 [ j ] > list2[ k ] ):
                k += 1
        list1 = list3[:]
    #for cc in list1:
    #    print ( documentlist [ cc ] )
    #    print ( urltxt [ documentlist [ cc ] ] )
    now = len ( list1 )
    if ( now < topk ):
        with open ( 'dictcontent.pickle' , 'rb' ) as picklefile:
            dictcontent = pickle.load ( picklefile )
            picklefile.close ()
        remain = topk - now
        dictquery = {}
        for term in datalist:
            if not ( term in dictquery ):
                dictquery [ term ] = 1
            else:
                dictquery [ term ] += 1
        b = {}
        square = 0 
        for term in dictquery:
            if ( term in dictcontent ):
                b[ term ] = ( 1 + math.log( dictquery [ term ] , 10 ))*math.log( idcount*1.0/dictcontent[ term ][ "df"] ,10 )
            else:
                b[ term ] = ( 1 + math.log( dictquery [ term ] , 10 ))*math.log( idcount, 10 )
            square = square + b [ term ]*b [ term ]
        
        square = math.sqrt ( square )

        heaplist = [ -1 ]
        valuelist = [ -1 ]

        for i in range ( 0 , remain ):
            if not ( i in list1 ):
                #print ( i )
                heaplist.append ( i )
                with open ( 'document' + str( i ) + '.pickle' , 'rb' ) as picklefile:
                    a = pickle.load ( picklefile )
                    picklefile.close()
                cosine = 0 
                for term in b:
                    if ( term in a ):
                        cosine = cosine + a[ term ]*b [ term ]
                

                cosine = cosine /( a["sqrtsquare"]*square )
                valuelist.append ( cosine )
                #print ( valuelist [ i + 1 ])

        i = remain//2
        #print ( i )
        while ( i >=1 ):
            downheap ( i , remain )
            i -= 1
        for i in range ( remain , idcount ):
            with open ( 'document' + str( i ) + '.pickle' , 'rb' ) as picklefile:
                a = pickle.load ( picklefile )
                picklefile.close ()
            cosine = 0
            for term in b:
                if ( term in a ):
                    cosine = cosine + a [ term ]*b [ term ]
            if ( a [ "sqrtsquare"] < 0.0000001 ):
                    continue
            cosine = cosine / ( a[ "sqrtsquare"]*square ) 
            if ( cosine > valuelist [ 1 ] ):
                valuelist [ 1 ] = cosine
                heaplist [ 1 ] = i 
                downheap ( 1 , remain )

        list2 = []
        i = remain -1 
    
        while ( remain >= 0 ):
            list2.append ( heaplist [ 1 ])
            heaplist[ 1 ] = heaplist [ remain ]
            valuelist [ 1 ] = valuelist [ remain ]
            remain -= 1 
            downheap ( 1 , remain )
        while ( i !=-1 ):
            list1.append ( list2 [ i ])
            i -= 1
        #for i in range ( 1 , remain + 1 ):
            
            #print ( valuelist [ i ] )
            #print ( heaplist [ i ] ) 
            #print ( documentlist [ heaplist [ i ] ])
else:
    with open('Btree.pickle','rb')as read_file:
        root=pickle.load(read_file)
        read_file.close()
    string=str1
    stringlist=re.split('\*',string)
    #print (stringlist)
    query_list=[]
    list1=[]
    for i in range(0,len(stringlist)):
        #print( i )
        list1 = jieba.cut ( stringlist[i] , cut_all = True )
        str1 = " ".join(list1)
        list1=re.split(" |\n",str1)
        list2=[]
        for j in list1:
            if (j!=''):
                list2.append(j)
        #print( list2 )
        if  (i==0):
            if ( list2 != []):
                list2[-1]=list2[-1]+'*'
        elif ( list2 !=[ ]) :
            list2[0]='*'+list2[0]
        query_list=query_list+list2
    for i in range(1,len(stringlist)-1):
        #print( i )
        list1 = jieba.cut ( stringlist[i] , cut_all = True )
        str1 = " ".join(list1)
        list1=re.split(" |\n",str1)
        list2=[]
        for j in list1:
            if (j!=''):
                list2.append(j)
        #print( list2 )
        if ( list2 != [] ):
            list2[-1]=list2[-1]+'*'
        query_list=query_list+list2
   
    DocID=[]

    for term in query_list:
        if ('*' in term):
            i=term.find('*')
            if (i==0):
                Bterm=term[1:len(term)]+'$'
            elif (i==(len(term)-1)):
                Bterm='$'+term[0:i]
            else:
                Bterm=term[i+1:len(term)]+'$'+term[0:i]
            #print(Bterm)
            Bterm1=Bterm[0:len(Bterm)-1]+chr ( ord ( Bterm [ - 1 ]) + 1)
            #print (Bterm1)
            Blist=searchbetween(root,Bterm,Bterm1)
            ii = len ( Blist )
            for iii in range( ii ):
                Blist [ iii ] = getoldword ( Blist [ iii ] )
                #print (  Blist [ iii ] ) 
            Orlist=OrOperation(Blist)
            if (DocID==[]):
                DocID=Orlist
            else:
                DocID=AndOperation(DocID,Orlist)
        else:
            if (DocID==[]):
                DocID=titlelist[term]
            DocID=AndOperation(DocID,titlelist[term])
        list1 = DocID




list3 = []
for i in list1:
    list3.append ( documentlist [ i ] )
list4 = []
for i in list3:
    filename = urltxt[ i ] 
    f = open (  filename )
    f.readline ( )
    str1 = f.read ( )
    list4.append ( str1 )

print ( yate.output_alist( list3 , list4 ))

print ( yate.include_footer ( { "Home" : "/index.html" } ))





