
from collections import Counter,OrderedDict
class OrderedCounter(Counter,OrderedDict):
    pass

list_1 = []
num = int(input("Enter the total number of inputs: "))
for e in range(0,num):
    num1 = input("Enter the words: ")
    list_1.append(num1)

word = OrderedCounter(list_1)

list_2 = set(list_1)

print(len(list_2))
for x in word:
    print(word[x],end="")
