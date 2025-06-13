# DAA Algorithm Implementations in Python


This repository contains Python implementations of key algorithms commonly studied in **Design and Analysis of Algorithms (DAA)**. Each file demonstrates a well-known algorithm with clean, concise, and readable code.

---

## 📂 File List & Descriptions

| 🔢 Filename              | 📝 Description |
|-------------------------|----------------|
| `floyd_warshall.py`     | All-pairs shortest path using Floyd-Warshall algorithm (Dynamic Programming based). |
| `prim_mst.py`           | Prim’s algorithm to find the Minimum Spanning Tree (MST) using a priority queue. |
| `kruskal_mst.py`        | Kruskal’s algorithm to construct MST using Union-Find (Disjoint Set Union). |
| `bellman_ford.py`       | Bellman-Ford algorithm for Single-Source Shortest Paths; detects negative weight cycles. |
| `topological_sort.py`   | Performs topological sort of a Directed Acyclic Graph (DAG) using DFS. |
| `graph_coloring.py`     | Solves the Graph Coloring problem using backtracking. |
| `hamiltonian_cycle.py`  | Uses backtracking to find a Hamiltonian Cycle in a graph (if it exists). |
| `subset_sum.py`         | Determines if a subset with a given sum exists using recursion + dynamic programming. |
| `job_sequencing.py`     | Greedy algorithm for the Job Sequencing Problem with deadlines and profits. |

---

## 🧪 How to Run

Each Python file is self-contained and can be tested independently. Example usage:
```bash
python floyd_warshall.py
