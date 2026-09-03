class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Creating a sorted stack of tuples containing the speed and position for 
        # each car, sorted by position in ascending order
        car_stack = []

        for i in range(len(position)):
            # Calculating the time to target
            target_time = (target - position[i])/speed[i]
            car_stack.append((position[i],target_time))

        # Sorting the car stack by position, then speed for tie-breaking
        car_stack.sort() 
    
        # Keep track of the current minimum, each time there is a new minimum, increase the fleet count
        cur_min = 0

        # Keep track of the current fleet count
        fleet_count = 0
        for i in range(len(car_stack)):
   
            cur_car = car_stack.pop() 
        
            if cur_car[1] > cur_min:
                cur_min = cur_car[1]
                fleet_count += 1
            
        return fleet_count
        

