def combine_alternatingly(list1, list2):
    combined = []
    for a, b in zip(list1, list2):
        combined.extend([a, b])
    combined.extend(list1[len(list2):])
    combined.extend(list2[len(list1):])
    return combined

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
print("Combined list:", combine_alternatingly(list1, list2))