def BubbleSort(li):
    for i in range(1, len(li)):
        for j in range(0, len(li) - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                print("Swapped:", li)
    return li


li = [60, 50, 40, 30, 20, 10]
print("List Before Sorting:", li)

li = BubbleSort(li)
print("List After Sorting:", li)

if len(li) >= 2:
    print("Second Largest Number:", li[-2])
else:
    print("List doesn't have enough elements.")