


def removeDuplicates( nums):
    removidos = set(nums)
    k = len(removidos)
    removidos = list(removidos)
    while len(removidos) <= k:
        removidos.append('_')
    return k
input(removeDuplicates([1,1,2]))    