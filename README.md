# 코테 하면서 정리할 만한 꿀팁들

## **🔥itertools**

```python
from itertools import permutations
from itertools import combinations
from itertools import product
```

를 통해 import 할 수 있으며, 사용 방식은 다음과 같다.

</br>
</br>

### **1. 순열(permutations)**

```python
# permutations(<배열>, <고를 원소의 개수>)
test = ['A', 'B', 'C']
result = list(permutations(test, 2))
```

결과:
```python
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

</br>
</br>

### **2. 조합(combinations)**

```python
# combinations(<배열>, <고를 원소의 개수>)
test = ['A', 'B', 'C']
result = list(combinations(test, 2))
```

결과:
```python
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

</br>
</br>

### **3. 여러 리스트의 조합(product)**

```python
# product(*<이차원 배열>)
test = [['A', 'B'], ['가', '나'], ['1', '2']]
result = list(product(*test))
```

결과:
```python
[('A', '가', '1'),
 ('A', '가', '2'),
 ('A', '나', '1'),
 ('A', '나', '2'),
 ('B', '가', '1'),
 ('B', '가', '2'),
 ('B', '나', '1'),
 ('B', '나', '2')]
```

---

## **🔥리스트에서 중복 제거하기**

</br>

### **1. 집합(set)을 이용하여 중복 제거**

</br>

집합(set) 자료형은 중복이 불가능하다는 조건이 있기 때문에 리스트를 집합으로 바꾸고, 다시 리스트로 바꾸면 중복이 사라진다.

단, 리스트가 오름차순으로 정렬되게 된다.

```python
arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]
result1 = set(arr)
result2 = list(result1)
```

결과:

```python
result1 --> {1, 2, 3, 4, 5, 6, 7, 8, 9}
result2 --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</br>

### **2. for 문을 이용하여 중복 제거**

</br>

집합(set)을 통해 중복을 제거하며 정렬되는 것이 싫다면 for 문을 통해서도 중복을 제거할 수 있다.

```python
arr = [6, 5, 6, 4, 4, 1, 1, 2, 3, 9, 8, 7, 9, 8, 7]
result = []  #중복을 제거한 리스트를 저장할 리스트

for elem in arr:
    if elem not in result1:
        result.append(elem)
```

결과:

```python
result --> [6, 5, 4, 1, 2, 3, 9, 8, 7]
```

---

## **🔥자료구조 - 스택(QUEUE)**

</br>

스택은 별도의 import 없이 List를 활용해서도 사용할 수 있으며, 사용 방식은 다음과 같다.

</br>
</br>

```python
stack = []          #스택 초기화

stack.append(1)     #스택에 요소 넣기
a = stack.pop()     #스택의 오른쪽(가장 나중에 들어간 요소)에서 요소 꺼내기
```

---

## **🔥자료구조 - 큐(QUEUE)**

</br>

```python
from collections import deque
```

를 통해 import 할 수 있으며, 사용 방식은 다음과 같다.

</br>
</br>

```python
queue = deque()         #큐 초기화

queue.append(1)         #큐에 요소 넣기
a = queue.popleft()     #큐의 왼쪽(가장 먼저 들어간 요소)에서 요소 꺼내기
queue.appendleft()      #큐의 왼쪽에 요소 넣기

queue.reverse()         #큐에 저장된 요소 순서 뒤집기
```

---

## **🔥리스트를 정렬하는 다양한 방법**

</br>

리스트를 정렬하는 데에는 다양한 방법이 있다.

```python
a = [3, 4, 1, 9, 5, 6, 2, 7, 8]
b = sorted(a)	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = a.sort()	# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</br>

위 방법은 단순히 값에 따라서 오름차순으로 정렬할 때 사용할 수 있지만,
다양한 옵션값을 넣어서 정렬할 수도 있다.

```python
a = [3, 4, 1, 9, 5, 6, 2, 7, 8]
b = sorted(a, reverse=True)		# [9, 8, 7, 6, 5, 4, 3, 2, 1], 내림차순
```

```python
a = [["carrot", 1], ["apple", 3], ["banana", 5], ["peanut", 3]]
# 이름([0]) 순으로 정렬
b = sorted(a, key=lambda x: x[0])
# [["apple", 3], ["banana", 5], ["carrot", 1], ["peanut", 3]]

# 당도([1]) 역 순으로 정렬
c = sorted(a, key=lambda x: -x[1])
# [["banana", 5], ["apple", 3], ["peanut", 3], ["carrot", 1]]

# 당도([1]) 순으로 정렬하며, 같은 값이 있을 경우에는 이름([0]) 순으로 정렬
d = sorted(a, key=lambda x:(-x[1], x[0]))
# [["banana", 5], ["apple", 3], ["peanut", 3], ["carrot", 1]]
```