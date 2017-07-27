import matplotlib.pyplot as plt
import wordcloud
import jieba
import commentSpider


def makeCloud(_commentList):
    word_list = []
    for comment in _commentList:
        word_list += jieba.cut(comment)

    word_split = ' '.join(word_list)
    print(word_split)
    comment_cloud = wordcloud.WordCloud(font_path='DroidSansFallback.ttf', max_words=100).generate(word_split)

    plt.imshow(comment_cloud)
    plt.axis('off')  # 关闭刻度
    plt.show()


def main():
    commentList = commentSpider.getComment('av12615924')
    makeCloud(commentList)

if __name__ == '__main__':
    main()