import matplotlib.pyplot as plt
import wordcloud
import jieba
import commentSpider


def countFreq(_wordList):
    word_dict = {}
    for word in _wordList:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    ordered_list = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    print(ordered_list)
    return word_dict  # 返回词频字典


def makeCloud(_commentList):
    word_list = []
    for comment in _commentList:
        word_list += jieba.cut(comment)

    word_split = ' '.join(word_list)
    print(word_split)
    stop_words_list = ['哈', '哈哈', '哈哈哈', '哈哈哈哈']
    # ordered_list = countFreq(word_list)
    # comment_cloud = wordcloud.WordCloud(font_path='Deng.ttf', max_words=100).fit_words(ordered_list)
    comment_cloud = wordcloud.WordCloud(font_path='Deng.ttf',
                                        max_words=50,
                                        max_font_size=50,
                                        stopwords=stop_words_list).generate(word_split)

    plt.imshow(comment_cloud, interpolation='bilinear')
    plt.axis('off')  # 关闭刻度
    plt.show()


def main():
    av = input('输入要查询的视频AV号：')
    commentList = commentSpider.getComment(av)
    makeCloud(commentList)

if __name__ == '__main__':
    main()
