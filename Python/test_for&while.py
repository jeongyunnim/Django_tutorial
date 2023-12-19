# for {anything you want} in {iterable things}:

my_iterable = [1,2,3]

for num in my_iterable:
    print("num: {}".format(num))

my_list = [(1,2), (3,4), ('a','b')]

num = 0
for (item_one, item_two) in my_list:
    num += 1
    print ("======= {} ========".format(num))
    print("first is {}".format(item_one))
    print("second is {}".format(item_two))
