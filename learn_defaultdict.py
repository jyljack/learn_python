from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] = 2

print(dict1[1])
print(dict1[2])
print(dict2[1])
print(dict3[1])
print(dict4[1])


d = defaultdict(lambda: {})
print(d["test"])
