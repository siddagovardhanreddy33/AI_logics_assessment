

# itterate over the string 
# check each element and count until we find a duplicate , 
# if we have a duplicate stop the count , and restart the count from their until next duplicate on end of string 
# repeat it until the string 
# check all counts , the max count has to be displayed output


def analyzer(x):
    duplicates = []
    non_dup = []
    len_longest_s_feqs = []
    
    for i in x:
        feq = 0
        if i not in non_dup:
            feq += 1 
            non_dup.append(i)
            len_longest_s_feqs.append(feq)  
        else:
            feq = 0
            duplicates.append(i)
            
    return max(len_longest_s_feqs)        
            
            
        
    #     if i not in non_dup :
    #         non_dup.append(i)
    #     else :
    #         duplicates.append(i)
            
    # return len(non_dup)
    
    
    
    
print(analyzer('abcadabcbb'))