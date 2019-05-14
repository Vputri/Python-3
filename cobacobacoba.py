from prettytable import PrettyTable

list1 = ["a", "b", "c"]
list2 = ["1", "0", "9"]

table = PrettyTable(["list1","list2"])
for x in range(0,3):
    table.add_row([list1[x],list2[x]])
print (table)
