"""
Recursion Examples in Python
Academic implementations from Data Structures coursework
"""

def reverse_string(word):
    if len(word) == 0:
        return ''
    return reverse_string(word[1:]) + word[0]


def find_index(array, value, i=0):
    if not array or i >= len(array):
        return None
    if array[i] == value:
        return i
    return find_index(array, value, i + 1)


def count_letter(word, letter, i=0):
    if not word or i >= len(word):
        return 0
    if word[i] == letter:
        return 1 + count_letter(word, letter, i + 1)
    return count_letter(word, letter, i + 1)


def print_numbers(n):
    if n == 0:
        return ''
    return f"{n} " + print_numbers(n - 1)


def count_zero(number):
    if number == 0:
        return 0
    if number % 10 == 0:
        return 1 + count_zero(number // 10)
    return count_zero(number // 10)


def count_file(lines, i=0):
    if not lines or i >= len(lines):
        return 0, 0

    numbers = [int(x) for x in lines[i].split() if x.isdigit()]
    line_count = 1 if numbers else 0
    line_sum = sum(numbers)

    next_sum, next_count = count_file(lines, i + 1)
    return next_sum + line_sum, next_count + line_count


def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def tower_of_hanoi(n, start, temp, goal):
    if n == 1:
        print(f"{start} -> {goal}")
        return
    tower_of_hanoi(n - 1, start, goal, temp)
    print(f"{start} -> {goal}")
    tower_of_hanoi(n - 1, temp, start, goal)


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def print_subsequences(s, current='', i=0):
    if i == len(s):
        print(current)
        return
    print_subsequences(s, current + s[i], i + 1)
    print_subsequences(s, current, i + 1)
