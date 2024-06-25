def reverse(s, start, stop):
    """Reverse elements in implicit slice s[start:stop]"""
    # In case if we dont specify start and stop
    # start = 0
    # stop = len(s)    
    if start < stop - 1:
       s[start], s[stop - 1] = s[stop - 1], s[start] 
       reverse(s , start+1, stop-1)


s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse(s, 0, len(s))
print(s)