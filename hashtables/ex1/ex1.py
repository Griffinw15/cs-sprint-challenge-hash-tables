def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    d = {}

    for k, v in weights:
        if v < limit:
            d[k] = v
        for k, v in d:
            if v + v


    return None
