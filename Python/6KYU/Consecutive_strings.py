def longest_consec(strarr, k):
    if(len(strarr) == 0 or k <= 0) or len(strarr) < k:
        return ""
    lst = ["".join(strarr[i:i+k]) for i in range(len(strarr))]
    return max(lst, key= lambda x: len(x))
        
