def twoSum(nums,target):
        
  # create a empty dict to store each element of array as key and its complement as the value
  checkedItems = {};
  # loop throguh the array for each element in the nums arr
  for e in range(0,len(nums)):
  
    #keep track of the complement for the current element
    complement = target - nums[e]
    #if current element is a key (meaning it was a complement of a prev element), return the value of the key (index of the previous element) as well as the current elements index
    if nums[e] in checkedItems:
      return[checkedItems[nums[e]],e]
    else:
    #store the current elements complement as the key, and its index as the value
      checkedItems[complement] = e
                
            
            
            
print(twoSum([2,7,11,15],17))