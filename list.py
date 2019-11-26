
l=[1,2] # index start with 0 
print(l.count(2)) # count each number in list
l.append(3)  # append 3 in the list
print(l)
l.sort(reverse=True) # sort in reverse order
print(l)
l.pop(2) # pop 2 no index
print(l)

s1=["cat","elephant","cow","dog"]
print(s1[1:3]) # print start with 1 and end before 3
print(s1[::-1]) # reverse list

for i in s1:
	if "cow" == i:
		print(True)
	else:
	     print(False)
print(l+s1)