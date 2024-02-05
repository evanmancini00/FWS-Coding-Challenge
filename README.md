# FWS-Coding-Challenge
2025 Coding Challenge FWS IPaC - Directed Acyclic Graphs

Longest Directed Path in a Directed Acyclic Graph (DAG)

Introduction
My goal in completing this challenge was to independently develop a solution that calculates the longest path in a Directed Acyclic Graph (DAG), and implement it in a simple, robust python script. I chose not to use any mathematical libraries that would generate or evaluate DAGs for me, and did not consult any previously published solutions or AI tools. This way, I fully attacked the applied math at the core of this challenge, and demonstrated my coding processes in the language I use most frequently. 

My solution involved representing DAG’s as upper-triangular matrices. Given a number (n) nodes inputted by the user, an nxn matrix is generated with zeros along the diagonal. Each vertex in the graph is represented by a dimension of the array (0,1,2,…,n). If a node shared a directed edge with another, a nonzero entry would be located at their corresponding element (i.e. if node 2 shared an edge of length 5 with node 4, the entry at matrix element 2,4 would be ‘5’). The values along and below the diagonal are always zero, as in a DAG nodes do not loop back on themselves and paths are oriented in the same direction. 

I used python’s native ‘random’ package to generate the edge-length values variably placed in each matrix element. If an element’s value was zero, that meant that the corresponding vertices did not share an edge and it was a ‘dead-end’ in the DAG. To ensure a significant number of zeros were present, I employed a weighted Bernoulli distribution that generated either a zero, or random integers within a set range for each matrix element. 

DAG’s therefore originate as nxn arrays, before being stored as organized namedtuples and further operated on as python dictionaries and sets to organize, measure, and sort paths by the combined value of each connecting node’s length. 

Script Overview
The following functions were implemented into one main argument to execute my solution:

create_dag(num_v, edgemin, edgemax, PRINT_DAG)
* Purpose: Generates a random Directed Acyclic Graph (DAG) with variable edge lengths.
    * Parameters:
    * num_v: Number of vertices in the graph, size of num_v x num_v matrix.
    * edgemin: Minimum edge length.
    * edgemax: Maximum edge length.
    * PRINT_DAG: Flag to print the generated graph in array format.
    * Returns:
    * Graph: Dictionary representing the graph structure.
    * Edges: List of edges in the graph storing each pair of vertices and length between them.
find_paths(graph, start, end, path=None, visited=None)
* Purpose: Finds all possible paths from a given starting vertex to an ending vertex using depth-first search (DFS).
    * Parameters:
    * graph: Directed graph represented as a dictionary.
    * start: Starting vertex for the search.
    * end: Ending vertex for the search.
    * path: Current path being explored (default is None).
    * visited: Set of visited vertices to avoid cycles (default is None).
    * Returns:
    * List of all possible paths from start to end.
couple_str(xs)
* Purpose: Creates pairs of vertices from a list of vertices.
    * Parameters:
    * xs: List of vertices.
    * Returns:
    * List of vertex pairs.
measure_paths(paths, edges)
* Purpose: Ranks the found paths by their total length.
    * Parameters:
    * paths: List of all possible paths in the graph.
    * edges: List of edges in the graph.
    * Returns:
    * List of paths sorted by total length in descending order.

Main Execution Logic
* 		Create DAG: Generates a random Directed Acyclic Graph (DAG) in array format and presents the graph in a structured searchable dictionary of edges
* 		Find Paths: Utilizes depth-first search (DFS) to find all possible paths from a specified starting vertex to any vertex in the graph, stores each path in DAG as chains of connected vertices.
* 		Measure Paths: Takes in the paths lists, creates a flat, efficiently searchable dictionary of paths, ranks each by total length.  
* 		Output: Prints the longest directed path starting from the specified starting vertex, along with its total length.



Optimization
There were a number of different optimizations that allowed this solution to work for higher orders DAGs:

Depth-First Search (DFS): In early iterations, the find_paths function was the largest bottleneck. To speed things up, I restructured the indexing of the graph dictionary and simplified the recursive DFS so that it found each path in three core steps. The function begins with the user-inputted starting vertex and an empty path before explores the graph recursively. The algorithm visits adjacent vertices one by one, and if/when  a dead-end is reached (no integer edge length) , the algorithm backtracks to the previous vertex to explore other paths.


Data Structures: I used dictionaries, lists, and sets to represent the original DAG, its edges, and calculated paths in a manner that minimizes storage complexity and overall runtime of the program.

* The ‘graph’ dictionary is used to represent the DAG and its connecting nodes, with each vertex as a key and the lists of edges originated from a given vertex as the corresponding value. This allows for  easy and efficient access to vertices and their corresponding edges. 
* ’ path’ lists organizes chains of vertices. Vertices are stored in the order they are traversed, and the list provides access to elements by index
* ‘visited’ set keeps tracked of vertices visited in the DFS offering efficient membership testing and preventing duplicate entries, and avoiding cycles in the graph.


These optimizations enable the program to handle moderately sized DAG’s (1-30 vertices) in a matter of microseconds, and much larger graphs (40-70) in a matter of minutes. Much larger DAGs (70+ nodes) are still solved, but runtimes increase to the 10-15 minute range. 


I chose to complete this challenge in python, because it the language I have been using most frequently and allowed me to work with as little outside help as possible. I took advantage of python’s flexibility and straightforward syntax to implement my algorithm elegantly and in a short time-frame. Had I chosen to use Java, the script likely would have compiled faster with JIT and slightly better memory management, however, it would have required more lines of code and a greater degree of difficulty translating my mathematical solution into executable code. 
