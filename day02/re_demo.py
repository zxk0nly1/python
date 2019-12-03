import re

s="""hello world 123
45678 你好"""

#result=re.match('^h\w\w\w\w\s\w{5}',s)
# result=re.match('^h(\w{4}\s\w{5})\s(\d{4}\s\d{4})',s)
#result=re.match('^h.*',s)#匹配所有字符
# print(result.group(1))#匹配第一个括号里的内容
# print(result.group(2))
#result=re.match('^h(.*?)(\d+)',s)#      .* 贪婪匹配    .*? 非贪婪匹配
#result=re.search('\w\s',s) #只能返回第一个匹配正则表达式的数据
#print(result.group())
#print(result) # findall()没有group属性
p=re.compile('.*',re.S)
#result=re.findall('.*',s,re.S)
result=re.findall(p,s)
print(result)
