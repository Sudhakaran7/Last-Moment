class Solution:
    def getLastMoment(self, n: int, left , right ) -> int:
        res = 0
        if left:
            res = max(max(left), res)
        if right:
            res = max(n - min(right), res)
        return res
val=Solution()
unit,a,b=map(int,input().split())
a_arr=list(map(int,input().split()))
b_arr=list(map(int,input().split()))
print(val.getLastMoment(unit,a_arr,b_arr))
