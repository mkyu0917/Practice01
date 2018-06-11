s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.replace(".", "")
s = s.replace(",", "")
s = s.upper()
s = s.split()
s.sort()

lst=set(s)
print(lst)
lst2=list(lst)
lst2.sort()
i=0
for st in lst:

    print(lst2[i])
    i=i+1


