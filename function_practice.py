
def find_max(number):
    max_num = number[0]

    for num in number :
        if num > max_num :
            max_num = num

    return max_num


nums = [12,45,2,89,34]
print(f"maximum number is : {find_max(nums)}")
