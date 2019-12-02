"""
文本的写入
"""
# with open("data.txt","w",encoding="utf-8") as f:
#     f.write("helo 100 200 你好")
"""
文本的读取
"""
with open("data.txt","r",encoding="utf-8") as f:
    info=f.read()
    print(info)