#<center color = "Red">CC98文本检索</center>
=======
** 1、简介**
------
	这是一个简易的文本检索系统，采用python编写，基本方法比较简单，主要是反向页表和Wtd-idf,中文分词采用的是python的库结巴分词。支持*用于模糊查找，比如“紫金*”

** 2、方法**
-------
	使用scrapy进行爬虫
	使用结巴分词对文本处理，得到关键字和codebook
	求出反向页表中每个页面的信息
	将搜索的语句和每个页面，求wtd-idf，按大小排序
	页面采用bootstrap
** 3、缺陷**
--------
	时间比较长，可以通过k－means先处理一下，可以用flann快速knn
	可以使用flask框架，使页面更美观
	

