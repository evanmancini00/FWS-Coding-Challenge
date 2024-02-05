#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:39:17 2024
@author: evanmancini

PUBLISH VERSION

USFW Coding Challenge: Given a directed acyclic graph (DAG) with variable edge lengths, calculate
the directed path of the greatest length for any vertex
"""
import random
from collections import namedtuple,defaultdict

Edge = namedtuple('Edge',['vertice','length'])
Path = namedtuple('Path',['route','tot_length'])

def create_dag(num_v,edgemin,edgemax,PRINT_DAG):
    print(f"Generating {num_v}-node DAG...")
    Edges = []

    dag = [[0]*num_v for _ in range(num_v)]

    for i in range(num_v):
        for j in range(i + 1,num_v):
            dag[i][j] = random.choices([0, random.randint(1, 100)], weights=[0.4, 0.6])[0]

            if dag [i][j] > 0:
                Edges.append(Edge((f'{i}',f'{j}'),dag[i][j]))

    if PRINT_DAG:
        for row in dag:
                print(row)

    Graph = defaultdict(list)
    for edge in Edges:
        Graph[edge.vertice[0]].append(edge)

    return Graph,Edges

def find_paths_optimized(graph,start,end, path = None, visited = None):
    print("Finding paths using depth-first search...")
    if path is None:
        path = [start]

    if visited is None:
        visited = set()

    if start == end:
        return [path]

    paths = []
    visited.add(start)

    if start in graph:
        for edge in graph[start]:
            new_start = edge.vertice[1]
            if new_start not in visited:
                new_path = path + [new_start]

                new_paths = find_paths_optimized(graph, new_start, end,new_path,visited)
                paths.extend(new_paths)

    visited.remove(start)

    return paths

def couple_str(xs):
    return [(f'{xs[i]}',f'{xs[i+1]}') for i in range(len(xs)-1)]

def measure_paths_optimized(paths,edges):
    print("Ranking found paths by length...")
    meas_paths = []

    path_dict = {(edge.vertice[0],edge.vertice[1]): edge.length for edge in edges}

    for path in paths:
        tot_path_length = sum([path_dict[(pair[0], pair[1])] for pair in couple_str(path)])
        meas_paths.append(Path(path,tot_path_length))

    return sorted(meas_paths,key = lambda Path: Path.tot_length, reverse = True)


if __name__ == '__main__':

    num_v = 100 #number of vertices
    edgemin,edgemax = 0,100
    starting_vertex = 0 #Starting node for DFS search


    Graph,edges = create_dag(num_v, edgemin, edgemax, PRINT_DAG = False)

    paths= find_paths_optimized(Graph,str(starting_vertex),str(len(Graph)))

    meas_paths = measure_paths_optimized(paths,edges)

    print(f"Longest directed path starting from vertext {starting_vertex}: \n {meas_paths[0].route} \n Total Length: {meas_paths[0].tot_length} ")







