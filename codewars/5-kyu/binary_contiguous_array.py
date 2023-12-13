def binarray(s)->int:
    hash_map = {}  
    curr_sum = 0
    max_len = 0
    ending_index = -1
 
    for i in range (0, len(s)): 
        if(s[i] == 0): 
            s[i] = -1
        else: 
            s[i] = 1
 
    for i in range (0, len(s)): 
        curr_sum = curr_sum + s[i] 
        if (curr_sum == 0): 
            max_len = i + 1
            ending_index = i 
        if curr_sum in hash_map:
            if max_len < i - hash_map[curr_sum]:
                max_len = i - hash_map[curr_sum]
                ending_index = i
        else: 
            hash_map[curr_sum] = i  
         
    for i in range (0, len(s)): 
        if s[i] == -1: 
            s[i] = 0
        else: 
            s[i] = 1
             
    return max_len