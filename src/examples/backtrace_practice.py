# Practice Tasks
import heapq
from collections import deque, defaultdict, Counter
from logging import fatal


# 1. List
class ListPractice:
    def __init__(self):
        self.arr = []

    # Insert into list
    def insert(self, item):
        self.arr.append(item)

    # Rotate a list
    def rotate_list(self, k):
        # 1. First way to reverse
        # Rotate right by k positions:
        print(f"Before Rotation list:: {self.arr}")
        rotated = self.arr[-k:] + self.arr[:-k]
        print(f"Rotated list:: {rotated}")
        # Using collections.deque (efficient for large lists)
        # deque has a built-in rotate method
        # if k is positive rotate right by k position
        dq = deque(self.arr)
        dq.rotate(k)
        # if k is negative, rotate right by k position
        print(f"Rotated list by deque:: {list(dq)}")

    # Find the second-largest number in the list (without sorting)
    def second_largest(self):
        if len(self.arr) < 2:
            return None  # Not enough elements
        first = second = float('-inf')  # Initialize
        for num in self.arr:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num
        return second if second != float('-inf') else None

    # Find the Kth-largest number
    def kth_largest(self, k):
        heap = []
        for num in self.arr:
            if len(heap) < k:
                """
                or the first k numbers, just push them into the heap.
                After this, heap has k elements, smallest of them at the root.
                """
                heapq.heappush(heap, num)
            elif num > heap[0]:
                """
                For the rest of the array (50, 23, 90):
                Compare current number with heap[0] (smallest in heap).
                If num > heap[0], it must be among the k largest, so:
                Push num to heap
                Pop the smallest element from heap (root)
                """
                heapq.heappushpop(heap, num)
                """
                The root of the min-heap is the smallest of the k largest elements, which is exactly the kth largest element.
                """

        return heap[0]
        # Time: O(n log k) → n elements, each heap operation is O(log k)


# Tuple
class TuplePractice:
    # A tuple is a collection which is ordered, unchangeable*, and indexed.
    def __init__(self):
        self.tup = tuple()

    # Swap two values of tuple without use of third variable
    def swap(self):
        if len(self.tup) < 2:
            print("Tuple has less than 2 elements, cannot swap.")
            return
        # Unpack first two elements
        a, b, *rest = self.tup
        print(f"a and b before swap => {a}, {b}")
        b, a = a, b
        print(f"a and b after swap => {a}, {b}")

    # convert it into a dict where values are lists of keys with same value
    # output: {1: ['a','c'], 2: ['b']}
    def convert_tuple(self):
        list_tuple = [('a', 1), ('b', 2), ('c', 1)]
        dic = {}
        for key, num in list_tuple:
            if num in dic:
                dic[num].append(key)
            else:
                dic[num] = [key]
        print(dic)
        # {1: ['a', 'c'], 2: ['b']}
        # Another approach
        dic = defaultdict(list)

        for key, num in list_tuple:
            dic[num].append(key)

        print(dict(dic))
        # {1: ['a', 'c'], 2: ['b']}


class SetPractice:
    # A set is a collection which is unordered, unchangeable*, and un-indexed.
    def __init__(self):
        self.set = set()

    # Insert item in set
    def add(self, item):
        self.set.add(item)

    # Get items
    def get(self):
        for s in self.set:
            print(f"{s}", end=" ")

    # Find intersection between two sets
    def inter(self):
        set_b = {1, 55, 2, 56, 8}
        inter_s = self.set.intersection(set_b)
        print(inter_s)
        # {1, 2}
        inter_ss = self.set & set_b  # work as intersection
        print(inter_ss)

    # Union
    def union(self):
        set_b = {1, 55, 2, 56, 8}
        union_s = self.set.union(set_b)  # also we can use |
        print(union_s)

    # difference
    def diff(self):
        set_b = {1, 55, 2, 56, 8}
        diff = self.set.difference(set_b)  # also we can use -
        print(diff)

    # Given a list with duplicates, find the element that appears only once using sets.
    def find_unique(self):
        lis = [1, 44, 2, 55, 44, 1, 66, 4, 2]
        print(f"\n -------- With sets--------")
        seen_once = set()
        seen_multiple = set()
        for it in lis:
            if it in seen_once:
                seen_multiple.add(it)
            else:
                seen_once.add(it)
        unique = seen_once - seen_multiple
        print(unique)
        # {66, 4, 55}
        print(f"\n -------- Without sets--------")

        uni = []
        for l in lis:
            if l not in uni:
                uni.append(l)
            else:
                ind = uni.index(l)
                uni.pop(ind)
        print(uni)
        print(f"\n -------- Find unique with O(n)--------")
        # Another way with O(n)
        freq = Counter(lis)
        uniq = [num for num, count in freq.items() if count == 1]
        print(uniq)

    # Check if two strings are anagrams using sets and lengths.
    def anagram(self):
        word_a = 'spar'
        word_b = 'rasp'
        len_a = len(word_a)
        len_b = len(word_b)
        set_a = set([w for w in word_a])
        set_b = set([b for b in word_b])
        print(set_a)
        count = 0
        if len_a == len_b:
            for ch in set_a:
                if ch in set_b:
                    count += 1
        if count == len_a and count == len_b:
            print("Both words are anagram")
        print(f"\n -------- Second approach - Time: O(n log n) → because of the sorting step --------")
        st_a = sorted(word_a)
        st_b = sorted(word_b)
        print(st_a)
        if st_a == st_b:
            print("Both words are anagram")


class Map:
    """
    Suppose you have map(func, iterable) and iterable has n elements.
    map() applies func to each element exactly once.
    If func is O(1) (constant time), then:
    Time complexity =𝑂(𝑛)
    If func is O(f(n)), then total complexity = O(n * f(n)).
    """

    def __init__(self):
        self.lis = [1, 44, 2, 55, 44, 1, 66, 4, 2]

    # Convert a list of numbers to strings using map.
    def convert_list_to_string(self):
        new_lis = list(map(str, self.lis))
        print(new_lis)

    # Convert a list of floats to integers
    def convert_floats_to_int(self):
        lis = [1.2, 44.1, 2.4, 55.5, 44.6, 1.2, 66.4, 4.5, 2.3]
        new_lis = list(map(int, lis))
        print(new_lis)

    # Multiply each element in [1,2,3,4] by 10 using map().
    def arithmetic(self):
        multiply = list(
            map(lambda a: a * 10, self.lis))  # converting to list is O(n) because map returns a iterator not a list
        print(f"Multiply by 10 : {multiply}")
        # we can avoid that by .join() accepts any iterable of strings, not just a list.
        sq = ' '.join(map(lambda x: str(x ** 2), self.lis))
        print(f"Square of each number : {sq}")
        # Addition
        ad = ' '.join(map(lambda r: str(r + 5), self.lis))
        print(f"Add 5 in each number : {ad}")

        # Convert a list of lower to upper
        low_list = ['ssaf', 'fdds', 'gffdd']
        up_li = ' '.join(map(lambda d: str.upper(d), low_list))
        print(f"Lower to upper case : {up_li}")

        # Get the length of each word in ['apple', 'banana', 'cherry'].
        len_each = ' '.join(map(lambda w: str(len(w)), low_list))
        print(f"length of each words : {len_each}")

        list1 = [1, 2, 3]
        list2 = [4, 5, 6]

        # Use map with lambda
        summed = list(map(lambda x, y: x + y, list1, list2))
        print(summed)
        # If else in map
        nums = [1, 2, 3, 4]
        labels = list(map(lambda x: "small" if x < 2 else "medium" if x < 4 else "large", nums))
        print(labels)

    # Filter
    def filter_list(self):
        list_a = [1, 2, 3, 4, 5, 6]
        # Given [1,2,3,4,5,6], keep only even numbers → [2,4,6].
        fil_even = list(filter(lambda x: x % 2 == 0, list_a))
        print(fil_even)  # [2, 4, 6]
        fil_odd = list(filter(lambda y: y % 2 != 0, list_a))
        print(fil_odd)  # [1, 3, 5]

        # Filter strings containing a letter
        li_str = ["apple", "banana", "cherry"]
        filter_s = list(filter(lambda x: 'a' in x, li_str))
        print(filter_s)  # ['apple', 'banana']

        # Filter numbers greater than a threshold
        filter_n = list(filter(lambda a: a > 3, list_a))
        print(filter_n) # [4, 5, 6]
        def fil(a):
            return a > 3

        filter_fn = list(filter(fil, list_a))

        print(filter_fn) # [4, 5, 6]

        # Filter non-empty strings
        emp_str = ["", "hello", " ", "world"]
        filter_non_empty = list(filter(lambda x: len(x.strip())!=0,emp_str))
        print(filter_non_empty)

        # Filter strings with digits
        str_l = ["abc", "123", "a1b2"]
        filter_str_digits = list(filter(lambda x: x.isdigit(),str_l))
        print(filter_str_digits) # ['123']

        # Filter using a custom function
        def is_prime(n):
            # 0 and 1 are not prime numbers
            if n==0 or n==1:
                return False
            for p in range(2,n):
                if n%p == 0:
                    return False
            return True
        prime = list(filter(is_prime, list_a))
        print(f"Prime numbers are: {prime}")

        # Filter negative numbers
        neg = [-1,4,-5,3,-6]
        filter_neg = list(filter(lambda x: x<0,neg))
        print(filter_neg) # [-1, -5, -6]

        # Filter numbers divisible by a value
        filter_div = list(filter(lambda x: x%2 == 0, list_a))
        print(filter_div)  # [2, 4, 6]





if __name__ == '__main__':
    print(f"\n -------- List --------")
    list_p = ListPractice()
    for i in [1, 22, 3, 4, 5]:
        list_p.insert(i)
    list_p.rotate_list(2)
    print(f"Second Largest number:: {list_p.second_largest()}")
    print(f"{2}nd Largest number is using heap :: {list_p.kth_largest(2)}")
    print(f"\n -------- Tuple --------")
    tup = TuplePractice()
    tup.tup = ("apple", "banana", "cherry")
    print(tup.tup)
    tup.swap()
    # tuple to dict
    tup.convert_tuple()

    print(f"\n -------- Set --------")
    ss = SetPractice()
    for i in [2, 3, 1, 4, 5]:
        ss.add(i)
    ss.get()
    print(f"\n -------- Intersection --------")
    ss.inter()
    # {1, 2}
    print(f"\n -------- Union --------")
    ss.union()
    # {1, 2, 3, 4, 5, 8, 55, 56}
    print(f"\n -------- Difference --------")
    ss.diff()  # {3, 4, 5} in set a not in others
    print(f"\n -------- Find unique --------")
    ss.find_unique()
    print(f"\n -------- Find Anagram --------")
    ss.anagram()

    print(f"\n -------- Map --------")
    map_ob = Map()
    map_ob.convert_list_to_string()
    map_ob.convert_floats_to_int()
    print(f"\n -------- Map Arithmetic--------")
    map_ob.arithmetic()
    map_ob.filter_list()
