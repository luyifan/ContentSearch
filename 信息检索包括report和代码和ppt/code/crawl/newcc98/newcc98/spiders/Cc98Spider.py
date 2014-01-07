# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from newcc98.items import Newcc98Item
import re
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
cc = 0 

class Cc98Spider ( BaseSpider ):
        name = "cc98"
        allowed_domains = [ "www.cc98.org" ]
        start_urls = [ "http://www.cc98.org" ]
        def parse4 ( self , response  ):
                item = Newcc98Item()
                item [ "urlname"] = response.url 
                hxs = HtmlXPathSelector ( response )
                title = hxs.select("/html/head/title/text()").extract()[0]
                item [ "title" ] = title[ :-9]
                
                #print ( item [ "urlname"])
                global cc 
                print ( cc )
                cc = cc + 1 
                

                #print ( item [ "title"].encode("GBK", 'ignore'))
                
                hxs = HtmlXPathSelector ( response )
                title = hxs.select("//blockquote/table/tr/td/span[@id=\"ubbcode1\"]/text()").extract()
                item [ "content"] = title

                #for eachitem in title:
                #        print ( eachitem.encode("GBK", 'ignore') )
                

                title = hxs.select("//blockquote/table/tr/td/span[@id!=\"ubbcode1\"]/text()").extract()
                item [ "reply"] = title 
                #for eachitem in item["reply"]:
                #        print ( eachitem.encode("GBK" , 'ignore'))
                
                title = hxs.select("//tbody/tr/td/table/tr/td/a/span[@style=\"color: #000066;\" or @style=\"color: #990000;\" ]/b/text()" ).extract()
                item [ "author"] = title
                #for eachitem in item["author"]:
                #        print ( eachitem.encode("GBK" , 'ignore'))
                
                f = open ( "C:\\Spider\\title\\" + str( cc ) + ".txt"  , "w" )
                f.write ( item [ "urlname"]  )
                f.write ( "\n")
                f.write ( item [ "title"].encode("GBK", 'ignore') )
                f.write ( "\n")
                f.write ( item["author"][0].encode("GBK" , 'ignore'))
                f.close ()

                f = open ( "C:\\Spider\\content\\" + str( cc ) + ".txt"  , "w" )
                f.write ( item ["urlname"] )
                f.write ("\n")
                for eachitem in item["content"]:  
                        f.write ( eachitem.encode("GBK" , 'ignore') )
                f.close ()

                f = open ( "C:\\Spider\\reply\\" + str( cc ) + ".txt"  , "w" )
                f.write ( item [ "urlname"] )
                f.write ( "\n")
                for eachitem in item [ "reply"]:
                        f.write ( eachitem.encode("GBK" , 'ignore') )
                f.write ( "\n")
                count = 1 
                for eachitem in item["author"]:
                        if ( count != 1 ):
                                f.write ( eachitem.encode("GBK" , 'ignore'))
                                f.write ( " ")
                        count = count + 1 

                f.close()

                
                #print ( item [ "content" ].encode("GBK", 'ignore'))



        def parse3 ( self , response  ):
                hxs = HtmlXPathSelector ( response )
                gotoboardurllist = hxs.select('//tr/td[2]/a[span]/@href').extract()
                for urls in gotoboardurllist:
                        realurl = urljoin_rfc( 'http://www.cc98.org/' , urls )
                        yield Request( realurl , callback = self.parse4 )
                
        def parse2 ( self , response ):
                hxs = HtmlXPathSelector ( response )
                gotoboardurllist =  hxs.select('//table/tr/td/a/@href').extract()
                for urls in gotoboardurllist:
                        if ( re.match( "list" , urls ) ):
                                realurl = urljoin_rfc( 'http://www.cc98.org/' , urls )
                                yield Request( realurl , callback = self.parse3 )


        def parse  ( self , response ):
                hxs = HtmlXPathSelector( response )
                gotoboardurllist = hxs.select('//table/tr/td/a/@href').extract()
                #print ( gotoboardurllist )
                for urls in gotoboardurllist:
                        if ( re.match( "list" , urls ) ):
                                realurl = urljoin_rfc( 'http://www.cc98.org/' , urls )
                                yield Request( realurl , callback = self.parse2 )
