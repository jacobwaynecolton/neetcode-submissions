class Solution:
    def isHappy(self, n: int) -> bool:
        n_string = str(n)
        n_list = list(n_string)
        seen = set()

     
        while True:
            
            total = 0
            for num in n_list:
                total += int(num) ** 2
            print(total)
            if total == 1:
                return True
            
            if total in seen:
                return False
            else:
                seen.add(total)
            
            n_list = list(str(total))


            