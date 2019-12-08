import  jieba

def cut_info():
    with open("comment.txt","r",encoding="utf-8")as f:
        text=f.read()
        cut_text=" ".join(jieba.cut(text))
        with open("cut_text.txt","w",encoding="utf-8") as f:
            f.write(cut_text)

cut_info()