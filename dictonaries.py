#dictonaries has two parameter one is key and another is value
d={6759:["kaisar","Student","CSE"],
   7100:"ash"
   }

print(d)
print(d[6759])

for i in d.values():
	print(i)

for i,j in d.items():
	print(i,j)