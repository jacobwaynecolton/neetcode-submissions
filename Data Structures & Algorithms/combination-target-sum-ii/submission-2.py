class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Backtracking task

        # The amount of decisions at each iteration is len(candidates), meaning
        # a loop will be needed 
        output = []
        ongoing = []

        candidates = sorted(candidates)

        def dfs(cur_i,total):
            if total == target:
                output.append(ongoing.copy())
                return
            
            for i in range(cur_i,len(candidates)):
                if total + candidates[i] > target:
                    break
                # If this number is a duplicate, bypass it
                if i > cur_i and candidates[i] == candidates[i-1]:
                    continue
                ongoing.append(candidates[i])
                dfs(i+1,total + candidates[i])
                ongoing.pop()

        dfs(0,0)

        return output
            


            

