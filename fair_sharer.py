def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """

    for i in range(num_iterations):
        max_index = values.index(max(values))
        share_value = int(max(values)*share)
        
        if max_index is len(values)-1:
            values[max_index-1] += share_value
            values[0] += share_value
            values[max_index] -= 2*share_value
            
        else:
            values[max_index-1] += share_value
            values[max_index+1] += share_value
            values[max_index] -= 2*share_value
            
    return values

#fair_sharer([0, 1000, 800, 0], 1) # --> [100, 800, 900, 0]
#fair_sharer([0, 0, 0, 1000], 2) # --> [180, 0, 180, 640]

if __name__ == "__main__":
    values = [0, 1000, 1000, 1000]
    num_iterations = 2
    print(fair_sharer(values, num_iterations, share=0.1))




