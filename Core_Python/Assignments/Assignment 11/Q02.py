# Python Program to Merge Two Lists and Sort it

# list1 = [12, 5, 8, 3]
# list2 = [7, 14, 2, 10]


# merged_list = list1 + list2

# # Sort the merged list
# merged_list.sort()

# # Output the result
# print("Merged and Sorted List:", merged_list)

def merge(li, s, e, mid):
    lhs = []
    rhs = []

    for i in range(s, mid + 1):
        lhs.append(li[i])
    for j in range(mid + 1, e + 1):
        rhs.append(li[j])

    i = j = 0
    k = s

    while i < len(lhs) and j < len(rhs):
        if lhs[i] < rhs[j]:  # fixed rhs[i] → rhs[j]
            li[k] = lhs[i]
            i += 1
        else:
            li[k] = rhs[j]
            j += 1
        k += 1

    while i < len(lhs):
        li[k] = lhs[i]
        i += 1
        k += 1

    while j < len(rhs):
        li[k] = rhs[j]
        j += 1
        k += 1

def divide(li, s, e):
    if s < e:
        mid = (s + e) // 2
        divide(li, s, mid)
        divide(li, mid + 1, e)
        merge(li, s, e, mid)

# Two separate lists
list1 = [23, 30, 12, 50]
list2 = [45, 78, 90, 84]

# Merge the two lists
combined_list = list1 + list2

print("Before Sorting:", combined_list)

# Apply merge sort
divide(combined_list, 0, len(combined_list) - 1)

print("After Sorting:", combined_list)