subjectList = ['physics', 'chemistry', 'english', 'chinese']
print(subjectList)
print(type(subjectList))
print(subjectList[0])
print(type(subjectList[0]))
print(subjectList[1:2])
print(type(subjectList[1:2]))

subjectList.append('music')
print(subjectList)

subjectList.remove(subjectList[2])
print(subjectList)

print("######################")
for subject in subjectList:
    print(subject)

print("######################")
for index in range(len(subjectList)):
    print(subjectList[index])