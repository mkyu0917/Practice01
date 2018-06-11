s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

print(s.count("to"))

s = s.replace(".", "")
s = s.replace(",", "")
s = s.upper()
s = s.split()
s.sort()

lst3=s
lst=set(s)
lst2=list(lst)
lst2.sort()
i=0
for st in lst2:

            print(st +":"+str(s.count(s[i])))
            i=i+1


