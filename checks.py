numbers = [1, 3, 5, 8, 10, 13, 16]

list_len = len(numbers)

for n in numbers:
    current_idx = numbers.index(n)
    print("Current Number:", numbers[current_idx])
    list_end = list_len - current_idx
    if list_end != 1:
        next_idx = current_idx + 1
        print("Next Number:   ", numbers[next_idx])
    else:
        print("End Of List!")