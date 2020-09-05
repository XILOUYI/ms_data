# Python3 code to demonstrate 
# Matching elements count 
# using list comprehension and index() + len() 
  
import pandas as pd
df1 = pd.read_csv('data1.csv')
df2 = pd.read_csv('data2.csv')
df3 = pd.read_csv('data3.csv')
list1 = list(df1.carat)
list2 = list(df2.carat)
list3 = list(df3.carat)
#p = set(list2)&set(list1)&set(list3)
p = set(list1).intersection(set(list2))
#Python Set union() Method，Return a set that contains all items from both sets, duplicates are excluded
b = set(list1).union(set(list2))
# Python code to get the difference between two sets， using difference() between set A and set B 
s = set(list1).difference(set(list2))

print(p)
print(len(p))
