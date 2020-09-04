from collections import Counter

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = [i.strip(-) for i in a]

    for i in results:
        if Counter(i) < 2:
            result.pop(i)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
