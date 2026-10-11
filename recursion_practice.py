def sum_list(numbers):
    if numbers == []:
        return 0
    return numbers[0] + sum_list(numbers[1:]) 
    
print(sum_list([2,4,6,8]))






        

