def search_in_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the left half is not sorted, the right half must be sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Example usage:
nums = [4, 5, 6, 7, 8, 1, 2]
target = 6
result = search_in_rotated_array(nums, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found in the array.")
