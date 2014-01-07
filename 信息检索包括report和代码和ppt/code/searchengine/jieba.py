import glob
import re
import os
import jieba
def dojiebawithf ( filename ):
	f = open ( filename , "r")
	print ( filename )
	name = f.readline ( )
	data = f.read()
	f.close ( )
	datalist = jieba.cut ( data , cut_all = True )
	f = open ( filename , "w" )
	f.write ( name )
	str1 = " ".join(datalist)
	f.write ( str1.encode("GBK" , 'ignore') )
	f.close ()
'''
dojiebawithf ( "C:\\Spider\\content\\1.txt")
'''
filelist = os.listdir("C:\\Spider\\content")
dict1 = {}
for filename in filelist:
	dojiebawithf ( "C:\\Spider\\content\\" + filename )
filelist = os.listdir("C:\\Spider\\title")
dict1 = {}
for filename in filelist:
	dojiebawithf ( "C:\\Spider\\title\\" + filename )
filelist = os.listdir("C:\\Spider\\reply")
dict1 = {}
for filename in filelist:
	dojiebawithf ( "C:\\Spider\\reply\\" + filename )





