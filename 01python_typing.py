# Python Typing Basics - Learning Examples
# This file demonstrates basic Python type hints for beginners

# 1. Basic function with type hints
def add_numbers(a: int, b: int, c: int) -> None:
    """Adds three numbers and prints the result."""
    print(a + b + c)

# Call the function
add_numbers(1, 2, 3)

# Import typing tools
from typing import List, Dict, Set, Optional, Any, Sequence, Tuple, Callable, TypeVar

# 2. Type hints for collections
# List of lists of integers
numbers_grid: List[List[int]] = [[1, 2], [3, 4]]

# Dictionary with string keys and values
word_map: Dict[str, str] = {"a": "b"}

# Example with age
person_info: Dict[str, Any] = {"name": "rupm", "age": 5}

# Set of strings
unique_words: Set[str] = {"a", "b"}

# Example with age in list
ages: List[int] = [5, 10, 15]

# 3. Custom type alias
# Define a type for a list of floats (like a vector)
Vector = List[float]

def process_vector(v: Vector) -> Vector:
    """Takes a vector and returns it (placeholder for processing)."""
    return v

# Example usage
process_vector([1.0, 2.0])

# Nested type: list of vectors
VectorList = List[Vector]

def process_vector_list(vectors: VectorList) -> VectorList:
    """Takes a list of vectors and returns it."""
    return vectors

# Example usage
process_vector_list([[1.0, 2.0]])

# 4. Optional parameters
def show_output(output: bool = False):
    """Shows output if flag is True."""
    if output:
        print("Output enabled")

show_output()

def show_optional_output(output: Optional[bool] = False):
    """Shows output with optional boolean."""
    if output:
        print("Optional output")

show_optional_output()

# 5. Any type (accepts anything)
def handle_anything(data: Any):
    """Handles any type of data."""
    print(f"Handling: {data}")

handle_anything(1)

# 6. Sequence types
def process_sequence(seq: Sequence[str]):
    """Processes a sequence of strings."""
    for item in seq:
        print(item)

# Examples with different sequence types
process_sequence(("a", "b", "c"))  # Tuple
process_sequence(["a", "b", "c"])  # List
process_sequence("hello")          # String (sequence of characters)

# 7. Tuple types
mixed_tuple: Tuple = (1, 2, 3, "hello")  # Mixed types

# Example with age in tuple
person_tuple: Tuple[str, int] = ("rupm", 5)

def process_string_sequence(seq: Sequence[str]):
    """Another example of processing strings."""
    pass  # Placeholder

# Specific tuple type
int_tuple: Tuple[int, int, int] = (1, 2, 3)

def another_string_processor(seq: Sequence[str]):
    """Yet another string processor."""
    pass

# 8. Callable types (functions as parameters)
def call_function(func: Callable[[int, int], int]):
    """Calls a function with two integers."""
    result = func(1, 2)
    print(f"Result: {result}")

def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

def use_add_function(func: Callable[[int, int], int]) -> None:
    """Uses an add function."""
    func(1, 2)

use_add_function(add)

# 9. Functions returning callables
def create_adder() -> Callable[[int, int], int]:
    """Creates and returns an adder function."""
    def adder(x: int, y: int) -> int:
        return x + y
    return adder

# Get the function
adder_func = create_adder()
adder_func(3, 4)  # This would work but not called here

def create_lambda_adder() -> Callable[[int, int], int]:
    """Creates an adder using lambda."""
    func: Callable[[int, int], int] = lambda x, y: x + y
    return func

# 10. Generic types with TypeVar
T = TypeVar('T')

def get_item(items: List[T], index: int) -> T:
    """Gets an item from a list by index."""
    return items[index]