def merge_sort(nums):

    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2

    left_half = nums[:middle]
    right_half = nums[middle:]

    print(f"Splitting: {nums}")
    print(f"Left half: {left_half}")
    print(f"Right half: {right_half}")

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    def combine(left, right):

        final_list = []

        left_pointer = 0
        right_pointer = 0

        while left_pointer < len(left) and right_pointer < len(right):

            left_item = left[left_pointer]
            right_item = right[right_pointer]

            if left_item <= right_item:
                final_list.append(left_item)
                left_pointer += 1

            else:
                final_list.append(right_item)
                right_pointer += 1

        remaining_left = left[left_pointer:]
        remaining_right = right[right_pointer:]

        final_list = final_list + remaining_left + remaining_right

        return final_list

    return combine(sorted_left, sorted_right)


nums = [859, 292, 281, 393, 822, 303, 383]

result = merge_sort(nums)

print("Final result:", result)