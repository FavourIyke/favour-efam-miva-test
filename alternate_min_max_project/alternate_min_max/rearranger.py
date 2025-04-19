# alternate_min_max/rearranger.py

def rearrange(arr):
    """
    Rearranges the array such that the smallest, then largest,
    then second smallest, then second largest, etc., alternate.
    """
    if not arr:
        return []

    arr.sort()
    result = []
    left, right = 0, len(arr) - 1

    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.extend([arr[left], arr[right]])
        left += 1
        right -= 1

    return result
