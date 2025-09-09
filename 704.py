def search(nums, target) -> int:
    mn, mx = 0, len(nums)-1

    while mn <= mx:
        mid = (mn + mx)//2
        if target > nums[mid]:
            mn = mid + 1
        elif target == nums[mid]:
            return mid
        else: #target less
            mx = mid - 1

    return -1