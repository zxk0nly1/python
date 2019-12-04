import json
json_data="""[{"name":"小明"},{"age":"20"},{"sex":"男"}]"""
print(json_data)
print(type(json_data))
# for i in json_data:
#     print(i)

data=json.loads(json_data)#将json--->python

json_text=json.dumps(data,indent=2,ensure_ascii=False)#json.dump
with open("data.json","w",encoding="utf-8") as f:
    f.write(json_text)