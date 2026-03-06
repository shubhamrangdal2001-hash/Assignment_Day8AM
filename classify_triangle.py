# classify_triangle.py
# Part C - Q2: Triangle Classification Function

def classify_triangle(a, b, c):
    # check for zero or negative values
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input: sides must be positive numbers"

    # check if it forms a valid triangle
    if a >= b + c or b >= a + c or c >= a + b:
        return "Not a triangle"

    # classify the triangle
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


# testing the function
print("===== Triangle Classifier =====\n")

test_cases = [
    (5, 5, 5),
    (5, 5, 3),
    (3, 4, 5),
    (1, 2, 3),   # not a triangle
    (0, 4, 5),   # invalid - zero
    (-1, 4, 5),  # invalid - negative
    (10, 1, 1),  # not a triangle
]

for a, b, c in test_cases:
    result = classify_triangle(a, b, c)
    print(f"classify_triangle({a}, {b}, {c}) => {result}")
