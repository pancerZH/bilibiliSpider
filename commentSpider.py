import requests
import re


def getComment(_av):
    s = requests.session()
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/59.0.3071.115 Safari/537.36'}
    url = 'https://www.bilibili.com/video/' + _av + '/'
    res = s.get(url, headers=header, verify=False)
    body = res.text
    cid = re.findall('cid=(.*)&aid', body)[0]  # 找到弹幕文件的名字

    danmu_url = 'https://comment.bilibili.com/{}.xml'.format(cid)
    res = s.get(danmu_url, headers=header, verify=False)
    body = res.text  # 提取弹幕文件内容

    dm_list = re.findall('<.*>(.*)</d', body)  # 提取弹幕组成列表
    return dm_list


def main():
    getComment('av12615924')

if __name__ == '__main__':
    main()
