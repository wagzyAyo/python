nums = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
new_arr = []

def product_of_array_except_self(nums):
    for i in nums:
        shallow = nums.copy()
        shallow.remove(i)
        number = 1
        for num in shallow:
            number *= num
        new_arr.append(number)

    print(new_arr)

product_of_array_except_self(nums=nums)
new_arr = []
product_of_array_except_self(nums=nums2)