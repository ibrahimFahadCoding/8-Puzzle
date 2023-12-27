from graph import Graph
import time

graph = Graph([['3', '6', '8'],
               ['1', ' ', '4'],
               ['7', '2', '5']])


start_time = time.perf_counter()
a_star_path, numNodes = graph.aStar()
end_time = time.perf_counter()



for node in a_star_path:
    print("\033c", end="")
    print("A-Star Search\n")
    print(node)
    time.sleep(1)
print(f'Moves Taken: {len(a_star_path)}\nNumber of Nodes Searched: {numNodes}')
print(f'Time Elapsed: {end_time - start_time: .3}')

start_time = time.perf_counter()
bfs_path, numNodes = graph.bfs()
end_time = time.perf_counter()
for node in bfs_path:
    print("\033c", end="")
    print("BFS Search\n")
    print(node)
    time.sleep(1)
print(f'Moves Taken: {len(bfs_path)}\nNumber of Nodes Searched: {numNodes}')
print(f'Time Elapsed: {end_time - start_time: .3}')



