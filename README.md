# bilibiliSpider
抓取bilibili视频弹幕，生成词云

## 背景说明
通过爬虫获取指定av号的视频弹幕，分词之后生成词云  
*本项目所有代码在Python3.6.0下测试通过*

## 使用的模块
- requests(2.12.4)
- re
- matplotlib(2.0.0)
- wordcloud(1.3.1)
- jieba(0.38)

## 使用说明
- **commenSpider.py**  
def getComment(_av):  

  - _av:视频的av号，暂不支持视频合集  
  - 返回值:包含所有弹幕的一个列表

- **wordCloud.py**  
- def makeCloud(_commentList):  

  - _commentList:弹幕列表  
  - 显示词云  
  
- def countFreq(_wordList):  
	- _wordList:分词后的词语列表  
	- 返回值：统计词频的字典

## 效果展示  
注：由于没有筛选，出现了词语重复的现象  
![image](https://github.com/pancerZH/bilibiliSpider/blob/master/image/show1.png)

增加了过滤列表之后的效果(过滤掉了'哈哈哈'之类的词语)
![image](https://github.com/pancerZH/bilibiliSpider/blob/master/image/show2.png)

## 已知的问题  
- 对于合集类视频，目前只能爬取第一个视频的弹幕
- 对于番剧，由于弹幕储存机制不同，目前完全无法爬取弹幕
