import math, numpy as np

def intersection(list1, list2):
    count = []
    for l in list1:
        if l in list2:
            count.append(l)
    return count

# euclidean point point distance
def point_point_distance(p1,p2):
    return np.linalg.norm(p1-p2)

# distance between point p and segment Q = a + t*(b-a)
def seg_point_distance(p0,p1,r):
    v = p1-p0
    w = r-p0
    c1 = np.dot(w,v)
    c2 = np.dot(v,v)

    if c1 <= 0: 
        return point_point_distance(p0,r)
    elif c2 <= c1:
        return point_point_distance(p1,r)
    else:
        b = c1/c2
        Pb = p0+v*b

        return point_point_distance(Pb,r)

# distance between segment P = p + s*(q-p) and segment Q = m + t*(n-m)
def seg_seg_distance(s0,s1,r0,r1):
    d0 = seg_point_distance(s0,s1,r0)
    d1 = seg_point_distance(s0,s1,r1)
    d2 = seg_point_distance(r0,r1,s0)
    d3 = seg_point_distance(r0,r1,s1)

    return min(d0,d1,d2,d3)

if __name__ == '__main__':
    print(segmentSegmentDistance([1,0,0],[2,4,5],[1,0,0],[3,5,6]))