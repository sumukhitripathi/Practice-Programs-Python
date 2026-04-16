#Magic Square with numbers from 1-9 having sum = 15

def create_magic_square(n):
    square = [[0] * n for _ in range(n)]
    num = 1
    row, col = 0, n // 2

    while num <= n * n:
        square[row][col] = num
        num += 1
        new_row = (row - 1) % n
        new_col = (col + 1) % n
        if square[new_row][new_col]:
            row = (row + 1) % n
        else:
            row, col = new_row, new_col

    return square

square = create_magic_square(3)

print("Magic Square (3x3)")
print("-" * 25)
for row in square:
    print("|", " | ".join(f"{n:^3}" for n in row), "|")
print("-" * 25)

print("\nRow sums    :", [sum(row) for row in square])
print("Col sums    :", [sum(square[r][c] for r in range(3)) for c in range(3)])
print("Diag sums   :", [sum(square[i][i] for i in range(3)), sum(square[i][2-i] for i in range(3))])