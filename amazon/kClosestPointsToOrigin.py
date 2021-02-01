#K Closest Points to Origin
import heapq

def kClosest(points, K):
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:K]

def kClosestMinHeap(points, K):
    heap = []
    for (x,y) in points:
        dist = -(x*x + y*y)
        if len(heap) == k:
            heapq.heappushpop(heap, (dist, x,y))
        else:
            heapq.heappush(heap,(dist,x,y))
    return [(x,y) for (dist, x, y) in heap]
        
    
print(kClosest([[3,3],[5,-1],[-2,4]],2))


