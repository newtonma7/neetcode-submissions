class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        u: multisource bfs
            init q with borders of the grid
            bfs valid (equal or lower height) neighboring cells 

            can my neighbor flow into me?
                if yes then absorb it into q

            we want the intersection of the two pac and atl lists

        keep a set for pac and atlantic for visited

        p:
            visited sets for each
            init q with
                first row, first col --> pac
                last row, last col --> atl
            

        '''
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        pacq = collections.deque()
        atlq = collections.deque()
        dirs = {(1,0), (0,1), (-1,0), (0,-1)}

        def bfs(q, visited):
            while q:
                row, col = q.popleft() 

                for dr, dc in dirs:
                    nr = dr + row
                    nc = dc + col
                    if (nr >= ROWS or nc >= COLS 
                    or nr < 0 or nc < 0 or (nr,nc) in visited
                    or heights[row][col] > heights[nr][nc]):
                        continue
                    else:
                        visited.add((nr,nc))
                        q.append((nr,nc))

        for i in range(ROWS):
            tup = (i,0)
            pac.add(tup) # first col
            pacq.append(tup)

        for i in range(COLS):
            tup = (0,i)
            pac.add(tup) # first row
            pacq.append(tup)
            
        bfs(pacq, pac)

        for i in range(ROWS):
            tup = (i, COLS-1)
            atl.add(tup) # last col
            atlq.append(tup)
        for i in range(COLS):
            tup = (ROWS-1,i)
            atl.add(tup) # last row
            atlq.append(tup)

        bfs(atlq, atl)
        return list(pac & atl)






            



