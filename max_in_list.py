def maximum(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

lst = [10, 20, 30, 40, 50]
print("The maximum number in the list is: ", maximum(lst))