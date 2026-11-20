class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []


        # Remaining is the amnt of parentheses still to be closed
        def dfs(cur_str,rem_o,rem_c): 
            if not rem_o and not rem_c:
                out.append(cur_str)
                return

            if not cur_str:
                dfs('(',rem_o-1,rem_c+1)
                return
            
            if rem_c:
                dfs(cur_str +')',rem_o,rem_c-1)
            
            if rem_o:
                dfs(cur_str +'(',rem_o-1,rem_c+1)

            


        dfs('',n,0)

        return out





