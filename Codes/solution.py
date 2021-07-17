## Problem Statement

# -Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].




def solve(nums,lower,upper):
    results = []  
    #if input arrar is empty      
    if not nums:
        results.append(pat_gen(lower, upper))
        return results

    #range is inclusive so using prev_num to check the first item
    prev_num = lower - 1

    for num in nums:
        if prev_num != num and num - 1 != prev_num:                
            missing = pat_gen(prev_num + 1, num - 1)                
            results.append(missing)
            prev_num = num                
        else:
            prev_num = num
            
    if nums[-1] != upper:
        missing = pat_gen(nums[-1] + 1, upper)
        results.append(missing)    
    
    return results

#format the range in string as per the requried output format
def pat_gen(left, right):
    return str(left) if left == right else str(left) + "->" + str(right)



# #Test Cases:

# #Test Case 1: Sample
# #nums=[0, 1, 3, 50, 75]
# print(solve(nums, 0, 99))

# #Test Case 2: Empty Array
# nums=[]
# print(solve(nums, 0, 99))

#Test Case 3: negative values
# nums=[-12, 0, 1, 3, 50, 75]
# print(solve(nums, -12, 100))