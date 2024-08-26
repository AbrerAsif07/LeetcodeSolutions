# Brute force approach
# class Solution:
#     def evenlyDivides(self, N):

#         x = str(N)
#         count = 0
#         for ch in x:
#             y = int(ch)
#             if N != 0:
#                 if N == 1:
#                     count = 1
#                 if N % y == 0:
#                     count += 1
#         return count


# Optimised Approach


class Solution:
    def evenlyDivides(self, N):
        count = 0

        x = N
        while x > 0:
            a = x % 10
            if a != 0:
                count += 1
            x = x // 10
        return count


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends
