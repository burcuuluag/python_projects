## time o(n)
## space o(n)

def majorityElement(nums):
    result = 0
    count = 0

    for num in nums:
        if count == 0:
            result = num
        if num == result:
            count += 1
        else:
            count -= 1

    print(result)
    return result



nums = [2,2,1,1,1,2,2]
majorityElement(nums)
