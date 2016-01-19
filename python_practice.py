# find the two biggest nums

arr = [1,5,8,1,3,10,6,4,7]

def find_biggest(arr):
    biggest = 0
    second_biggest = 0
    for num in arr:
        if num > biggest:
            second_biggest, biggest = biggest, num
        elif num < biggest and num > second_biggest:
            second_biggest = num
    print("biggest is %d and second biggest is %d" % (biggest, second_biggest))
# find_biggest(arr)

# fib

def fib_sequence(num):
    fibo = [0,1]
    for i in range(0, num):
        numb = fibo[i] + fibo[i+1]
        fibo.append(numb)
    print(fibo[num])
    print(fibo)
# fib_sequence(8)


# bubble sort
arr_to_sort = [9,8,7,6,5,4,1,2,3]
def bub_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bub_sort(arr_to_sort))






