import RubicsCube
from RubicsCube import *
import time
from collections import deque

def shortest_path(start, end):

    visited = {}
    visited[start] = (start, -1)
    config = []
    nodes = deque()
    nodes.append(start)
    while nodes:
        node = nodes.popleft()
        if node == end:
            break
        else:
            for i in RubicsCube.twists:
                temp_node = RubicsCube.perm_apply(node, i)
                if (not (visited.__contains__(temp_node))):
                    visited[temp_node] = (node, RubicsCube.twists_names[i])
                    nodes.append(temp_node)
                else:
                    continue

    if (len(visited) == 1):
        return []
    if (visited.__contains__(end)):
        rev_config = deque()
        config = []
        temp_node = end
        while (temp_node != start):
            temp_node, temp = visited[temp_node]
            rev_config.append(temp)
        while (rev_config):
            config.append(rev_config.pop())
        return config
    else:
        return None

start = time.time()
path = shortest_path((6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),
                     (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
end = time.time()

print("PATH found by Breadth First Search:" + str(path))
print("Time it took in seconds:" + str(end - start))