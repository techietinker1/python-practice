""" 30 python exercises with full type hints - Solutions """

from typing import List, Dict, Tuple, Optional, Set, Any, Union, Callable
from dataclasses import dataclass
import json
from abc import ABC, abstractmethod
import math

# 1-5 basic operations

# 1 Add two numbers
print("Q1")
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(5, 3))  # expected: 8

# 2 Check if number is even
print("Q2")
def is_even(num: int) -> bool:
    return num % 2 == 0

print(is_even(4))  # expected: True
print(is_even(5))  # expected: False

# 3 Find maximum of three numbers
print("Q3")
def max_of_three(a: float, b: float, c: float) -> float:
    return max(a, b, c)

print(max_of_three(5.5, 3.2, 7.8))  # expected: 7.8

# 4 Calculate factorial
print("Q4")
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # expected: 120

# 5 Convert temperature
print("Q5")
def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))  # expected: 32.0
print(celsius_to_fahrenheit(100))  # expected: 212.0

# 6-10 string manipulation

# 6 Reverse a string
print("Q6")
def reverse_string(text: str) -> str:
    return text[::-1]

print(reverse_string("Hello"))  # expected: "olleH"

# 7 Count vowels
print("Q7")
def count_vowels(text: str) -> int:
    return sum(1 for c in text.lower() if c in "aeiou")

print(count_vowels("Hello World"))  # expected: 3

# 8 Check palindrome
print("Q8")
def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("madam"))  # expected: True
print(is_palindrome("A man a plan a canal Panama"))  # expected: True

# 9 Capitalize words
print("Q9")
def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split())

print(capitalize_words("hello world"))  # expected: "Hello World"

# 10 Remove duplicates from string
print("Q10")
def remove_duplicate_chars(text: str) -> str:
    seen = set()
    result = ""
    for char in text:
        if char not in seen:
            result += char
            seen.add(char)
    return result

print(remove_duplicate_chars("hello"))  # expected: "helo"

# 11-15 list operations

# 11 Sum of list
print("Q11")
def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))  # expected: 15

# 12 Find average
print("Q12")
def calculate_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0

print(calculate_average([1.0, 2.0, 3.0, 4.0, 5.0]))  # expected: 3.0

# 13 Filter even numbers
print("Q13")
def filter_even(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))  # expected: [2, 4, 6]

# 14 Find second largest
print("Q14")
def second_largest(numbers: List[int]) -> Optional[int]:
    unique_nums = list(set(numbers))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([1, 2, 3, 4, 5]))  # expected: 4

# 15 Flatten list
print("Q15")
def flatten_list(nested_list: List[Union[int, List[int]]]) -> List[int]:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

print(flatten_list([1, [2, 3], 4, [5, 6]]))  # expected: [1, 2, 3, 4, 5, 6]

# 16-20 dictionary operations

# 16 Word frequency counter
print("Q16")
def word_frequency(text: str) -> Dict[str, int]:
    words = text.lower().split()
    freq: Dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("hello world hello"))  # expected: {'hello': 2, 'world': 1}

# 17 Merge dictionaries
print("Q17")
def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    result = dict1.copy()
    result.update(dict2)
    return result

print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))  # expected: {'a': 1, 'b': 3, 'c': 4}

# 18 Invert dictionary keys and values
print("Q18")
def invert_dict(original: Dict[str, int]) -> Dict[int, str]:
    return {v: k for k, v in original.items()}

print(invert_dict({"a": 1, "b": 2, "c": 3}))  # expected: {1: 'a', 2: 'b', 3: 'c'}

# 19 Find common keys
print("Q19")
def common_keys(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Set[str]:
    return set(dict1.keys()) & set(dict2.keys())

print(common_keys({"a": 1, "b": 2}, {"b": 3, "c": 4}))  # expected: {'b'}

# 20 Filter dictionary by value
print("Q20")
def filter_dict_by_value(data: Dict[str, int], min_value: int) -> Dict[str, int]:
    return {k: v for k, v in data.items() if v >= min_value}

print(filter_dict_by_value({"a": 1, "b": 5, "c": 3}, 3))  # expected: {'b': 5, 'c': 3}

# 21-25 functions & lambda

# 21 Create multiplier function
print("Q21")
def create_multiplier(factor: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

multiply_by_3 = create_multiplier(3)
print(multiply_by_3(5))  # expected: 15

# 22 Apply function to list
print("Q22")
def apply_function(func: Callable[[int], int], numbers: List[int]) -> List[int]:
    return [func(num) for num in numbers]

def double(x: int) -> int:
    return x * 2

print(apply_function(double, [1, 2, 3, 4, 5]))  # expected: [2, 4, 6, 8, 10]

# 23 Sort complex data
print("Q23")
def sort_students(students: List[Dict[str, Union[str, int]]], 
                  by: str = "name") -> List[Dict[str, Union[str, int]]]:
    return sorted(students, key=lambda s: s[by])  # type: ignore

students = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
print(sort_students(students, "name"))  # expected: sorted by name
print(sort_students(students, "age"))  # expected: sorted by age

# 24 Filter with predicate
print("Q24")
def filter_with_condition(numbers: List[int], 
                         predicate: Callable[[int], bool]) -> List[int]:
    return [num for num in numbers if predicate(num)]

def is_positive(x: int) -> bool:
    return x > 0

print(filter_with_condition([-2, -1, 0, 1, 2], is_positive))  # expected: [1, 2]

# 25 Compose two functions
print("Q25")
def compose_functions(f: Callable[[int], int], 
                     g: Callable[[int], int]) -> Callable[[int], int]:
    def composed(x: int) -> int:
        return f(g(x))
    return composed

def add_five(x: int) -> int:
    return x + 5

def multiply_by_two(x: int) -> int:
    return x * 2

composed_func = compose_functions(add_five, multiply_by_two)
print(composed_func(3))  # expected: 11 (3*2=6, 6+5=11)

# 26-30 classes & OOP

# 26 Person class
print("Q26")
@dataclass
class Person:
    name: str
    age: int
    email: str
    
    def is_adult(self) -> bool:
        return self.age >= 18
    
    def greet(self) -> str:
        return f"Hello, my name is {self.name}"

person = Person("Rupm", 45, "rupm@example.com")
print(person.is_adult())  # expected: True
print(person.greet())  # expected: "Hello, my name is Rupm"

# 27 Bank account class
print("Q27")
class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        self.account_holder: str = account_holder
        self._balance: float = initial_balance
    
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount: float) -> bool:
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self) -> float:
        return self._balance
    
    def __str__(self) -> str:
        return f"Account: {self.account_holder}, Balance: ${self._balance:.2f}"

account = BankAccount("John", 1000)
account.deposit(500)
print(account.get_balance())  # expected: 1500.0
print(account.withdraw(200))  # expected: True
print(str(account))  # expected: "Account: John, Balance: $1300.00"

# 28 Rectangle class
print("Q28")
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def is_square(self) -> bool:
        return self.width == self.height

rect = Rectangle(5, 5)
print(rect.area())  # expected: 25.0
print(rect.perimeter())  # expected: 20.0
print(rect.is_square())  # expected: True

# 29 Abstract shape class and circle
print("Q29")
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

circle = Circle(5)
print(f"{circle.area():.2f}")  # expected: 78.54
print(f"{circle.perimeter():.2f}")  # expected: 31.42

# 30 JSON serialization
print("Q30")
def serialize_to_json(data: Dict[str, Any]) -> str:
    return json.dumps(data)

def deserialize_from_json(json_string: str) -> Dict[str, Any]:
    return json.loads(json_string)

data = {"name": "Alice", "age": 25}
json_str = serialize_to_json(data)
print(json_str)  # expected: '{"name": "Alice", "age": 25}'
deserialized = deserialize_from_json(json_str)
print(deserialized)  # expected: {'name': 'Alice', 'age': 25}