class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Sets to store numbers already present in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Keep track of all empty cells to avoid scanning the 9x9 grid repeatedly
        empty_cells = []
        
        # Step 1: Initialize the tracking sets and find empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    # Mapping 2D index (r, c) to a unique 1D box index from 0 to 8
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))
                    
        # Step 2: Backtracking function using O(1) set lookups
        def backtrack(cell_idx: int) -> bool:
            # Base Case: All empty cells have been successfully filled
            if cell_idx == len(empty_cells):
                return True
                
            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try filling the cell with digits '1' through '9'
            for num in "123456789":
                # Instant O(1) validation check instead of scanning loops
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    # Make the choice
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)
                    
                    # Move to the next empty cell
                    if backtrack(cell_idx + 1):
                        return True
                        
                    # Undo the choice (Backtrack)
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
                    
            return False
            
        # Start the recursion from the first empty cell
        backtrack(0)
