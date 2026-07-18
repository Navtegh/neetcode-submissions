class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        q=deque()
        q.append(0)
        visited=set()
        total_coins=0
        while q:
            total_coins+=1
            for _ in range(len(q)):
                curr=q.popleft()
                for i in coins:
                    if curr+i==amount:
                        return total_coins
                    if curr+i in visited or curr+i>amount:
                        continue
                    q.append(curr+i)
                    visited.add(curr+i)
        return -1


