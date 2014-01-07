把爬的数据存在C:\\Spider
然后用dowithfile.py处理[mp3][b][upload]之类的
然后用jieba.py 把数据分词一下
然后用 invertedindex.py存取invertedindex和其他为了显示的信息
然后用BtreeStore.py把term存在Btree里面
然后用preparetdidf.py把每个document的term的tdidf存起来
用cmd 运行simplehttpd.py 就可以开启服务了
然后在浏览器localhost:8060就可以进入搜索界面了
输入搜索词即可搜索了
