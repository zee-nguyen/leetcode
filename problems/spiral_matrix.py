class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        
        i, j = 0, 0 # row-index, col-index
        
        # delta-i, delta-j
        # initially, we want to go same row, left to right so di = 0, dj = 1
        # when we reach last col, we want to go downward, so di, dj = dj, -di meaning di = 1, dj = 0 (incrementing row, staying same col)
        # di = 0, dj = -1 ==> staying same rol, going left (col decrementing)
        # di = -1, dj = 0 ==> staying same col, going up (row decrementing)
        di, dj = 0, 1 
        
        for _ in range(m * n):
            res.append(matrix[i][j])
            # mark as visited
            matrix[i][j] = '*'
            # check if the next cell in our direction is available (≠ '*')
            # if the dimension goes beyond the row/col border, % m (or % n) will bring it back to boundary, i.e. the cell would have been visited already. That's when we know we need to change direction.
            if matrix[(i+di) % m][(j+dj) % n] == '*':
                # change direction
                di, dj = dj, -di
            i += di
            j += dj
        return res
