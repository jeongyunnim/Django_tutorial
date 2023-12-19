#!/usr/bin/python

myvar = 10
mylist = [1,2,3,myvar]
print(mylist)
mylist.pop(3)
print(mylist)
mylist.reverse()
print(mylist)

stock_prices =  {"GOOGL":[200,210,220],"GME":[20,100,300]}

history = stock_prices["GOOGL"]

print("First day price is: {}".format(history[0]))

mydict ={"OUTER": {"INNER":100}}
print(mydict["OUTER"])
print(mydict["OUTER"]["INNER"])
