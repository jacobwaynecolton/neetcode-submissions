import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Creating an adjacency list
        adj_list = {}
        for time in times:
            if time[0] in adj_list:
                adj_list[time[0]].append(time[1:])
            else:
                adj_list[time[0]] = [time[1:]]

        # Keeping track of the current min distance 
        min_dists = {}
        #  Using a min heap to keep track of the potential paths to take at any given time 
        min_heap = []

        cur_node_val = k


        if cur_node_val in adj_list:
            for neighbor in adj_list[cur_node_val]:
                # switching the order when pushing to the heap because the heap will sort based on the first element of the list
                # If I was giving this as code for others to build from, I would find away to reduce confusion around this
                heapq.heappush(min_heap, [neighbor[1],neighbor[0]])

        
        while min_heap:

            # popping off the shortest edge 
            short_edge = heapq.heappop(min_heap)
            short_edge_dist = short_edge[0]
            short_edge_val = short_edge[1]
            # updating the value of that connected node if its >= cur distance
            if short_edge_val in min_dists or short_edge_val == k:
                continue
            else:
                min_dists[short_edge_val] = short_edge_dist
            
            # Adding the neighbors of this new node to the heap
            if short_edge_val in adj_list:
                for neighbor in adj_list[short_edge_val]:
                    if neighbor[0] in min_dists and min_dists[neighbor[0]] <= (short_edge_dist + neighbor[1]):
                        continue
                    else:
                        heapq.heappush(min_heap,[neighbor[1] + short_edge_dist,neighbor[0]])


        

        if len(min_dists) != (n-1):
            return -1
        
        else:
            return max(min_dists.values())