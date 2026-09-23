class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(a, b):
            p1 = find(a)
            p2 = find(b)

            # if true, then they are already connected (same component)
            if p1 == p2:
                return False

            # union the components
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        

        