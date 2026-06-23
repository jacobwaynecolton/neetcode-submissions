class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # iterating through each row looking for duplicates
        rows = {}
        cols = {}
        sub_boxes = {}

        # iterating through each element in the board
        for i in range(len(board)):
            for j in range(len(board[i])): 
                element = board[i][j]
                if element == '.':
                    continue
                # adding the element to the corresponding row set
                if i not in rows:
                    rows[i] = set(element)
                else:
                    if element in rows[i]:
                        return False
                    else:
                        rows[i].add(element)
                # adding the element to the corresponding col set
                if j not in cols:
                    cols[j] = set(element)
                else:
                    if element in cols[j]:
                        return False
                    else:
                        cols[j].add(element)

                # adding the element to the corresponding sub_box set
                sub_box_index = (i//3) * 3 + (j//3)

                if sub_box_index not in sub_boxes:
                    sub_boxes[sub_box_index] = set(element)
                else:
                    if element in sub_boxes[sub_box_index]:
                        return False
                    else:
                        sub_boxes[sub_box_index].add(element)
        return True
