class Solution:
    def isPalindrome(self, s: str) -> bool:
       inner_count = 0
       outer_count = 0
       while True:
            if len(s) == 0:
                return False
            
            end_character = s[-1 - outer_count].lower()

            while not end_character.isalnum() and len(s) >= (2+outer_count):
                end_character = s[-2 - outer_count].lower()
                outer_count += 1
            start_character = s[0+ inner_count].lower()   

            while not start_character.isalnum() and len(s) > (1+inner_count):
                start_character = s[1 + inner_count].lower()
                inner_count += 1

            if(len(s) - outer_count == 1 or inner_count == len(s) -1):
                return True
            if start_character != end_character:
                return False
            else:
                inner_count +=1
                outer_count +=1

            
