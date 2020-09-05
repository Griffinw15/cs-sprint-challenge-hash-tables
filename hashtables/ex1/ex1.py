def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    d = {}

    for i in range(len(weights)):
        if i < limit:
            d[weights[i]] = i

    for i in range(len(weights)):
        target = limit - weights[i]
        if target in d:
            return(max(i, d[target]), min(i, d[target]))

    return None
