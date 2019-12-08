from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
#通过wordcloud模块传入词云相对应的参数
from imageio import imread
#
import codecs
#使用codecs打开文件，不需要考虑编码格式问题
import matplotlib.pylab as plt
#绘制数字统计图，用它来显示和绘制词云
from os import path

class Draw_pic:
    def __init__(self):
        self.font_path="./font/simhei.ttf"#设置字体路径
        self.image_path="timg.jpg"#设置图片路径
        self.cut_text="cut_text.txt"#设置文本路径

    def get_info(self):
        d=path.dirname(__file__)#获取当前文件操作路径
        image=imread(self.image_path)#将图片处理为多维数组
        text=codecs.open(path.join(d,self.cut_text),"rb",encoding="utf-8").read()#读取文本数据
        self.draw_wordcloud(image,text)#调用词云的方法

    def draw_wordcloud(self,image,text):
        stopwords=set(STOPWORDS)#使用默认屏蔽词
        #字体路径 图片数组 屏蔽字 背景颜色 最大词数限制 字体最大限制 文本数据
        wordcloud=WordCloud(font_path=self.font_path,mask=image,
                            stopwords=stopwords,background_color="white",
                            max_words=2000,max_font_size=200).generate(text)
        image_color=ImageColorGenerator(image)#让字体颜色随图片颜色改变
        wordcloud.to_file("wordcloud.jpg")#生成的词云命名
        plt.imshow(wordcloud.recolor(color_func=image_color))#生成词云颜色
        plt.axis("off")#不显示坐标轴
        plt.show()#显示词云

draw=Draw_pic()
draw.get_info()