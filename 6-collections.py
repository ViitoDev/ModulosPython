from collections import Counter, namedtuple, deque
from operator import itemgetter

#1 - Fruit Lists (counting)
fruits = ["Apple", "Banana", "Grape", "Pear", "Banana", "Grape", "Apple", "Orange", "Banana", "Pinapple", "Grape", "Pear", "Banana"]
print(fruits)
print(Counter(fruits))

#2 - Using named tuple
game = namedtuple("game", ["name", "price", "note"])
g1 = game('Fifa 23', 90.50, 8.5)
g2 = game("Resident evil 4 Remake", 300, 10.0)
print(g1)
print(g2)

#3- Sorting dictionaries
students = {"Pedro": 23, "Ana": 22, "Jake":26}
a = sorted(students.items(), key = itemgetter(1))
print(a)

#4- Using a queue on extremities
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)