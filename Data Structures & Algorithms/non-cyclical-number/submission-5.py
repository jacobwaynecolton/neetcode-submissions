class Solution:
    def isHappy(self, n: int) -> bool:
        n_string = str(n)
        n_list = list(n_string)
        seen = set()

        while True:
            
            total = 0
            # Sum the squares from the list of digits
            for num in n_list:
                total += int(num) ** 2
            if total == 1:
                return True
            # If we have seen this digit before, return False
            # Otherwise add it to the seen set
            if total in seen:
                return False
            else:
                seen.add(total)
            # Update list to be the new total
            n_list = list(str(total))


            