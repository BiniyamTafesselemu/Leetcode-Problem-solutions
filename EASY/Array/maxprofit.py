def profit(nums):
    maxm=0
    l=0
    r=1
    sell=0
    buy=0
    while r < len(nums):
        prof=nums[r]-nums[l]
        if prof > 0:
            if prof > maxm:
                maxm=prof
                sell=r
                buy=l
        else:
            l=r
        r+=1
    return [buy,sell]
print(profit([7,1,3,6,3]))
