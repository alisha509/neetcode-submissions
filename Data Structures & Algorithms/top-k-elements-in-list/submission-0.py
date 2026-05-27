import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        empty_dict={}
        for i in nums:
            if i not in empty_dict:
                empty_dict[i]=1
            else:
                empty_dict[i]+=1
            top_k = heapq.nlargest(k, empty_dict, key=empty_dict.get)
        return top_k

