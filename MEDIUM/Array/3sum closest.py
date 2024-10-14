def threesumclosest(nums,target):
    nums.sort()
    comp=sum(nums[:3])
    for i in range(len(nums)-2):
        l=i+1
        r=len(nums)-1
        while l<r:
            curr=nums[i]+nums[l]+nums[r]
            if abs(curr-target)<abs(comp-target):
                comp=curr
            if curr<target:
                l+=2
            else:
                r-=1
    return comp
print(threesumclosest([1,-2,2,-4],1))