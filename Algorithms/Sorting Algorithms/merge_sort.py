__author__ = 'Avinash'
 
 
def merge_sort(sort_list):
    print("splitting", sort_list)
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        leftHalf = sort_list[:mid]
        rightHalf = sort_list[mid:]
 
        merge_sort(leftHalf)
        merge_sort(rightHalf)
 
        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                sort_list[k] = leftHalf[i]
                i = i + 1
            else:
                sort_list[k] = rightHalf[j]
                j = j + 1
            k = k + 1
 
        while i < len(leftHalf):
            sort_list[k] = leftHalf[i]
            i = i + 1
            k = k + 1
 
        while j < len(rightHalf):
            sort_list[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    print("merging...", sort_list)
 
 
lst = []
size = int(input("Enter size of the list: \t"))
 
for i in range(size):
    elements = int(input("Enter an element: \t"))
    lst.append(elements)
 
merge_sort(lst)
