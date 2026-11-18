def quick_sort(numbers):

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]

    smaller = []
    bigger = []

    for number in numbers[:-1]:

        if number <= pivot:
            smaller.append(number)
        else:
            bigger.append(number)

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


numbers = [859, 292, 281, 393, 822, 303, 383,909]

result = quick_sort(numbers)

print("Final result:", result)