def find_target (numbers , target):
    for i in range (len(numbers)):
        if numbers[i]== target :
            return i 
    return -1
nums = [10,25,40,55,70]
print("index of 55 is : " , find_target(nums,55))
print("index of 99 is : " , find_target(nums,99))        
        