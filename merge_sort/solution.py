""" solution for merge_sort """

def merge_sort(arr):
    """ recursive function to reduce the array to sub-arrays of length one or zero """
	# if the array is length one or zero, return the array
    if len(arr) < 2:
        return arr
    # figure out the middle point
    middle = int(len(arr) / 2)

    # create an array of the left half
    left = arr[0 : middle]

    # create an array of right half
    right = arr[middle : len(arr)]

    # call merge on a recursively called left half and right half
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    """ function to merge two arrays into one in order """
    result = []
    # while both arrays have elements in them, zip them together
    while left and right:
        if not isinstance(left[0], int) or not isinstance(right[0], int):
            return None
    # if the left array first element is less than the right array first element, append to result
        if left[0] <= right[0]:
            result.append(left.pop(0))
    # else append the right array first element to result
        else:
            result.append(right.pop(0))

    # if left is the only array with elements, append them all in
    while left:
        result.append(left.pop(0))
    # if right is the only array with elmeents, append them all in
    while right:
        result.append(right.pop(0))
    # return final result
    return result
