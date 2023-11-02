# Problem Statement 
Maximum Value But Limited Neighbors:
You are given an array a[1..n] of positive numbers and an integer k. You have to produce an array b[1..n], such that: (i) For each j, b[j] is 0 or 1, (ii) Array b has adjacent 1s at most k times, and (iii) sum_{j=1 to n} a[j]*b[j] is maximized. For example, given an array [100, 300, 400, 50] and integer k = 1, the array b can be: [0 1 1 0], which maximizes the sum to be 700. Or, given an array [10, 100, 300, 400, 50, 4500, 200, 30, 90] and k = 2, the array b can be [1, 0, 1, 1, 0, 1, 1, 0, 1] which maximizes the sum to 5500.
To be precise about the definition of adjacency: sequence [0, 1, 0, 1, 0, 1, 1, 1] has two adjacent 1s. Sequence [0, 1, 0, 0, 1, 1, 1, 1] has 3 adjacent 1s. Sequence [1, 0, 1, 1, 0, 1, 1, 1] also has 3 adjacent 1s.


# How to Run
Download the source code and run it in any python IDE.
