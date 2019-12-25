def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:        
    d = dict()
    for e in nums1:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    n = []
    for e in nums2:
        if e in d.keys():
            if d[e] > 0:
                n.append(e)
                d[e]-=1
    return n
