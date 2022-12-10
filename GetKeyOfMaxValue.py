open_set = {}
open_set[17] = 0
open_set[12] = 2
open_set[13] = 4
open_set[19] = 9
open_set[18] = 9
print(max(open_set)) # return 19
print(max(open_set, key=open_set.get)) # return 18
current = max(open_set, key=open_set.get)
open_set.pop(current)
print(open_set)