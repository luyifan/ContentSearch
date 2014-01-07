import glob
import re
import os 

def dowithupload ( str1 ):
    start= 0
    str2 = ''
    while ( True ):
        agostart = start
        start = str1.find (  "[upload"  , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart :start ]
        final = str1.find ("[/upload]", start )
        if ( final == -1 ):
            final = start + 3 
        start = final + 9
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart :stringlen ]
    #print ( str2 )
    return str2
def dowithi ( str1 ):
    start= 0
    str2 = ''
    while ( True ):
        agostart = start
        start = str1.find (  "以下是引用["  , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart :start ]
        final = str1.find ("[/i]", start )
        start = final + 12
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart :stringlen ]
    #print ( str2 )
    return str2

def dowithbianji ( str1 ):
    start = 0
    str2 = ''
    #print ( str1 )
    while ( True ):
        agostart = start
        start = str1.find ( "[此" , start )
       # print ( start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart :stringlen ]
    #print ( str2 )
    return str2

def dowithmp3 ( str1 ):
    str2 = ''
    start = 0
    while ( True ):
        agostart = start
        start = str1.find ("[mp3" , start )
        if ( start == -1 ):
            break
        
        str2 = str2 + str1 [ agostart :start ]
        final = str1.find ( "[/mp3]" , start )
        if( final == -1 ):
            final = str1.find ( "[/mp 3]" , start )+1
            if ( final == 0 ):
                final = str1.find ("[/MP3]" , start )
                if ( final == -1 ):
                    final = str1.find ( "[ /mp3]" , start ) + 1
        
        start = final + 6
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2

def dowithfont1 ( str1 ):
   
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[font" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithfont2 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[/font]" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithsize1 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[size" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2    
def dowithsize2 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[/size]" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithem ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[em" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithb1 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[b" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2    
def dowithb2 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[/b]" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithquote1 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[quote" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2    
def dowithquote2 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[/quote" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithcolor1 ( str1 ):
   
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[color" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithcolor2 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[/color]" , start )
        #print ( start ) 
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        #print ( str2 )
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    #print ( str2 )
    return str2
def dowithurl1 ( str1 ):
   
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[url=" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithurl2 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[/url]" , start )
        #print ( start ) 
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        #print ( str2 )
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    #print ( str2 )
    return str2
def dowithalign1 ( str1 ):
   
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[align" , start )
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    return str2
def dowithalign2 ( str1 ):
    
    start = 0
    str2 = ''
    while( True ):
        agostart = start
        start = str1.find ( "[/align]" , start )
        #print ( start ) 
        if ( start == -1 ):
            break
        str2 = str2 + str1 [ agostart : start ]
        #print ( str2 )
        final = str1.find ( "]" , start )
        start = final + 1
    stringlen = len ( str1 )
    str2 = str2 + str1 [ agostart : stringlen ]
    #print ( str2 )
    return str2
def dowithfile ( filename ):
    f = open ( filename , "r" )
    str1 = f.read ( )
    f.close ( )
    str1 = dowithupload ( str1 )
    str1 = dowithi ( str1 )
    #print ( str1 )
    str1 = dowithcolor1 ( str1 )
    #print ( str1 )
    str1 = dowithcolor2 ( str1 )
    
    str1 = dowithbianji ( str1 )
    #print ( str1 )
    str1 = dowithmp3 ( str1 )
    #print ( str1 )
    str1 = dowithfont1 ( str1 )
    #print ( str1 )
    str1 = dowithfont2 ( str1 )
    #print ( str1 )
    str1 = dowithsize1 ( str1 )
    #print ( str1 )
    str1 = dowithsize2 ( str1 )
    #print ( str1 )
    str1 = dowithem ( str1 )
    #print ( str1 )
    str1 = dowithb1 ( str1 )
    str1 = dowithb2 ( str1 )
    str1 = dowithquote1 ( str1 )
    str1 = dowithquote2 ( str1 )
    str1 = dowithurl1 ( str1 )
    str1 = dowithurl2 ( str1 )
    str1 = dowithalign1 ( str1 )
    str1 = dowithalign2 ( str1 )
    #print ( str1 )
    f = open ( filename , "w" )
    f.write ( str1 )
    f.close  ()
'''dowithfile ( "C:\\Spider\\reply\\4019.txt" )
'''
filelist = os.listdir ( "C:\\Spider\\content" )
for afile in filelist:
    filename =  "C:\\Spider\\content\\" + afile
    print ( filename )
    dowithfile ( filename )
filelist = os.listdir ( "C:\\Spider\\title" )
for afile in filelist:
    filename =  "C:\\Spider\\title\\" + afile
    print ( filename )
    dowithfile ( filename )
filelist = os.listdir ( "C:\\Spider\\reply" )
for afile in filelist:
    filename =  "C:\\Spider\\reply\\" + afile
    print ( filename )
    dowithfile ( filename )
#'''
