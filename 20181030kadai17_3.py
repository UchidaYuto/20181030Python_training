import re

l="The ghost that says boo haunts the loo"
w=re.findall(".oo",l,re.IGNORECASE)

print(w)
