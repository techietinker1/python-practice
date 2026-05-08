"""30 python exercises with full type hints."""
# 1 Add two numbers

print("Q1") # to identify output for each question
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(5, 3))  # expected: 8

# 2 Subtract two numbers

print("Q2")
def subtract_numbers(a: int, b: int) -> int:
    return a - b

print(subtract_numbers(5, 3)) # expected: 2

# 3 Multiply two numbers

print("Q3")
def multiply_numbers(a: int, b: int) -> int:
    return a * b

print(multiply_numbers(5, 3)) # expected: 15

# 4 Divide two numbers

print("Q4")
def divide_numbers(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print(divide_numbers(8, 2)) # expected: 4.0

# 5 Check even or odd

print("Q5")
def is_even(num: int) -> bool:
    return num % 2 == 0

print(is_even(4)) # expected: True
print(is_even(5)) # expected: False

# 6 Maximum of two numbers

print("Q6")
def max_of_two(a: int, b: int) -> int:
    return max(a, b)

print(max_of_two(5, 3)) # expected: 5

# 7 Maximum of three numbers

print("Q7")
def max_of_three(a: int, b: int, c: int) -> int:
    return max(a, b, c)

print(max_of_three(5, 3, 7)) # expected: 7

# 8 Square of a number

print("Q8")
def square(num: int) -> int:
    return num ** 2

print(square(4)) # expected: 16

# 9 Cube of a number

print("Q9")
def cube(num: int) -> int:
    return num ** 3

print(cube(3)) # expected: 27

# 10 Check positive/negative/zero

print("Q10")
def check_number(num: int) -> str:
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
print(check_number(5)) # expected: "Positive"
print(check_number(-3)) # expected: "Negative"
print(check_number(0)) # expected: "Zero"

# 11 Sum of First N numbers

print("Q11")
def sum_of_first_n(n: int) -> int:
    return sum(range(1, n + 1))

print(sum_of_first_n(5)) # expected: 15 (1+2+3+4+5)

# 12 Factorial

print("Q12")
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
print(factorial(5)) # expected: 120 (2*3*4*5)

# 13 Fibonacci sequence

print("Q13")
def fibonacci(n: int) -> list[int]:
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
    
print(fibonacci(10)) # expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 14 Reverse number

print("Q14")
def reverse_number(num: int) -> int:
    return int(str(num)[::-1])

print(reverse_number(12345)) # expected: 54321

# 15 Count digits

print("Q15")
def count_digits(num: int) -> int:
    return len(str(abs(num)))

print(count_digits(12345)) # expected: 5

# 16 Sum of digits

print("Q16")
def sum_of_digits(num: int) -> int:
    return sum(int(i) for i in str(abs(num)))

print(sum_of_digits(12345)) # expected: 15 (1+2+3+4+5)

# 17 Multiplication table

print("Q17")
def table(n: int) -> list[int]:
    return [n*i for i in range(1, 11)]

print(table(5)) # expected: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# 18 Prime check

print("Q18")
def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7)) # expected: True
print(is_prime(10)) # expected: False

# 19 Reverse string

print("Q19")
def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("Hello")) # expected: "olleH"

# 20 Palindrome string

print("Q20")
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

print(is_palindrome("madam")) # expected: True
print(is_palindrome("hello")) # expected: False

# 21 Count vowels

print("Q21")
def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")

print(count_vowels("Hello world")) # expected: 3 (e, o, o)

# 22 Uppercase string

print("Q22")
def to_upper(s: str) -> str:
    return s.upper()

print(to_upper("Hello")) # expected: "HELLO"

# 23 Lowercase string

print("Q23")
def to_lower(s: str) -> str:
    return s.lower()

print(to_lower("Hello")) # expected: "hello"

# 24 Remove spaces

print("Q24")
def remove_spaces(s: str) -> str:
    return s.replace(" ", "")

print(remove_spaces("Hello World")) # expected: "HelloWorld"

# 25 Sum of list

print("Q25")
def sum_of_list(nums: list[int]) -> int:
    return sum(nums)

print(sum_of_list([1, 2, 3, 4, 5])) # expected: 15

# 26 Maximum in list

print("Q26")
def max_list(nums: list[int]) -> int:
    return max(nums)

print(max_list([1, 2, 3, 4, 5])) # expected: 5

# 27 Minimum in list

print("Q27")
def min_list(nums: list[int]) -> int:
    return min(nums)

print(min_list([1, 2, 3, 4, 5])) # expected: 1

# 28 Remove duplicates

print("Q28")
def remove_duplicates(nums: list[int]) -> list[int]:
    return list(dict.fromkeys(nums))

print(remove_duplicates([1, 2, 2, 3, 3, 4, 5, 5])) # expected: [1, 2, 3, 4, 5]

# 29 Second largest number

print("Q29")
def second_largest(nums: list[int]) -> int:
    nums = list(set(nums)) # remove duplicates
    nums.sort()
    if len(nums) < 2:
        return -1
    return nums[-2]

print(second_largest([1, 2, 3, 4, 5])) # expected: 4

# 30 Frequency of elements

print("Q30")
def frequency(nums: list[int]) -> dict[int, int]:
    freq: dict[int, int] = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq
    
print(frequency([1, 2, 2, 3, 3, 3, 4, 5])) # expected: {1: 1, 2: 2, 3: 3, 4: 1, 5: 1}