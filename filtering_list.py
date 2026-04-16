data = [(1, 'a', 2, 'b'), (3, 'x', 4), ('p', 5, 'q', 6), (7, 8, 'z')]

result = [tuple(x for x in t if isinstance(x, int)) for t in data]

print("Original :", data)
print("Filtered :", result)