def binary (nums,k):
    l=0
    r=len(nums)-1
    while r>l:
        mid=(r+l)//2
        if nums[mid]==k:
            return mid
        elif nums[mid]>k:
            r=mid
        else:
            l=mid
    return -3
print(binary([1,2,3,4,5,6,7,8,9],6))