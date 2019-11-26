t=("cow","dog","cat")# tuple is unchangable
print(t[::])
print(len(t))
print(t.count("dog"))
t=list(t)
t.append("goat")
print(t)