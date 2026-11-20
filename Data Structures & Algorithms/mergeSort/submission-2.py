# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortRecursion(arr=pairs, s=0, e=len(pairs)-1)

    def mergeSortRecursion(self, arr, s, e):
        if e - s <= 0:
            return arr

        def merge(arr, s, m, e):
            left = arr[s:m+1]
            right = arr[m+1:e+1]

            i, j = 0, 0
            k = s

            while i < len(left) and j < len(right):
                if left[i].key <= right[j].key:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                
                k += 1

            # Insert leftover values
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        m = (s + e) // 2

        # Sorting Left
        self.mergeSortRecursion(arr, s=s, e=m)
        # Sorting Right
        self.mergeSortRecursion(arr, s=m+1, e=e)

        # Merge Sorted Halves
        merge(arr, s=s, m=m, e=e)

        return arr
