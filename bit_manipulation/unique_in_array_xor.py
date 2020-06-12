def find_non_duplicate(nums: list) -> int:
    '''
    >>>find_non_duplicate([1, 2, 1, 2, 3, 4, 3])
    4
    This occurs as:
    1. Any number xor itself is 0.
    2. Any number xor 0 is itself.
    '''
    x = 0
    for num in nums:
        x ^= num
    return x
