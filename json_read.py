# import json
# f=open("sample3.json","r")
# content=json.load(f)
# print(content)
import json

data=[
    {"name":"arun","age":23},
    {"name":"amal","age":20}
]
f=open('data.json','w')
json.dump(data,f)