#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    table = {}

    for s, d in tickets:
        if s == "NONE":
            table[s] = d
        elif d == s:
            table[s] = d
        elif d == "NONE":
            table[s] = d
    
    route = [table]
    return route
