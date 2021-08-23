import json

list = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(type(list))
print(type(dict))

# loads()：将json数据转化成Python对象
# dumps()：将Python对象转化成json数据

json_list = json.dumps(list)
json_dict = json.dumps(dict)
print(json_list)
print(type(json_list))
print(json_dict)
print(type(json_dict))

_list = json.loads(json_list)
_dict = json.loads(json_dict)

print(_list)
print(type(_list))
print(_dict)
print(type(_dict))
