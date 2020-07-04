char_total = 100000
def MAX_DIST_CHAR(str, n): 
    num = [0] * char_total 
    for i in range(n): 
        num[ord(str[i])] += 1
      
    max_dist = 0
    for i in range(char_total): 
        if (num[i] != 0): 
            max_dist += 1    
      
    return max_dist 
  
def SMALL_SUBSTR_MAX_CHAR(str): 
  
    n = len(str)
    max_dist = MAX_DIST_CHAR(str, n) 
    min_len = n 
    for i in range(n): 
        for j in range(n): 
            substr = str[i:j] 
            substr_len = len(substr) 
            substr_distinct_char = MAX_DIST_CHAR(substr, substr_len) 
            if (substr_len < min_len and max_dist == substr_distinct_char): 
                min_len = substr_len 
  
    return min_len 
  
if __name__ == "__main__": 
      
    str = input()
    len = SMALL_SUBSTR_MAX_CHAR(str); 
    print(len) 
