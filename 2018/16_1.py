data = '''Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]'''

data = '''Before: [0, 2, 2, 2]
11 3 3 3
After:  [0, 2, 2, 0]

Before: [3, 2, 1, 1]
11 2 3 3
After:  [3, 2, 1, 0]

Before: [1, 2, 2, 1]
5 3 2 2
After:  [1, 2, 1, 1]

Before: [1, 0, 2, 2]
14 0 2 2
After:  [1, 0, 0, 2]

Before: [3, 2, 3, 3]
10 1 3 3
After:  [3, 2, 3, 0]

Before: [1, 1, 2, 1]
14 0 2 3
After:  [1, 1, 2, 0]

Before: [2, 1, 2, 0]
6 2 2 0
After:  [1, 1, 2, 0]

Before: [1, 1, 3, 1]
13 1 2 0
After:  [0, 1, 3, 1]

Before: [1, 1, 1, 3]
10 2 3 1
After:  [1, 0, 1, 3]

Before: [3, 3, 0, 2]
3 2 3 0
After:  [1, 3, 0, 2]

Before: [2, 1, 1, 0]
4 1 0 2
After:  [2, 1, 0, 0]

Before: [2, 3, 3, 2]
7 3 1 0
After:  [1, 3, 3, 2]

Before: [1, 0, 2, 1]
12 0 1 0
After:  [1, 0, 2, 1]

Before: [0, 1, 0, 0]
0 0 3 3
After:  [0, 1, 0, 0]

Before: [0, 1, 2, 1]
0 0 1 0
After:  [0, 1, 2, 1]

Before: [0, 2, 1, 0]
0 0 1 0
After:  [0, 2, 1, 0]

Before: [3, 0, 3, 2]
7 3 0 1
After:  [3, 1, 3, 2]

Before: [1, 3, 2, 2]
7 3 1 2
After:  [1, 3, 1, 2]

Before: [0, 3, 1, 3]
9 0 0 2
After:  [0, 3, 0, 3]

Before: [0, 1, 1, 3]
0 0 3 0
After:  [0, 1, 1, 3]

Before: [1, 1, 2, 3]
2 1 2 1
After:  [1, 0, 2, 3]

Before: [3, 3, 3, 2]
7 3 0 1
After:  [3, 1, 3, 2]

Before: [1, 1, 2, 3]
2 1 2 3
After:  [1, 1, 2, 0]

Before: [1, 0, 2, 1]
5 3 2 1
After:  [1, 1, 2, 1]

Before: [3, 1, 1, 1]
1 2 2 0
After:  [2, 1, 1, 1]

Before: [1, 2, 2, 0]
14 0 2 1
After:  [1, 0, 2, 0]

Before: [0, 3, 1, 1]
1 2 2 0
After:  [2, 3, 1, 1]

Before: [3, 3, 2, 2]
11 3 3 3
After:  [3, 3, 2, 0]

Before: [0, 1, 3, 3]
8 3 2 3
After:  [0, 1, 3, 1]

Before: [0, 3, 2, 0]
0 0 3 3
After:  [0, 3, 2, 0]

Before: [0, 3, 3, 2]
0 0 2 2
After:  [0, 3, 0, 2]

Before: [3, 1, 3, 3]
10 1 3 1
After:  [3, 0, 3, 3]

Before: [1, 1, 1, 1]
11 3 3 2
After:  [1, 1, 0, 1]

Before: [0, 1, 1, 1]
0 0 2 1
After:  [0, 0, 1, 1]

Before: [1, 0, 0, 3]
12 0 1 2
After:  [1, 0, 1, 3]

Before: [0, 0, 3, 2]
15 3 2 0
After:  [2, 0, 3, 2]

Before: [3, 0, 1, 1]
12 3 1 0
After:  [1, 0, 1, 1]

Before: [3, 1, 0, 2]
3 2 3 3
After:  [3, 1, 0, 1]

Before: [0, 2, 0, 3]
0 0 1 2
After:  [0, 2, 0, 3]

Before: [3, 2, 0, 2]
3 2 3 3
After:  [3, 2, 0, 1]

Before: [2, 1, 0, 0]
4 1 0 1
After:  [2, 0, 0, 0]

Before: [1, 1, 2, 1]
14 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 3, 2, 3]
14 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 2, 2, 3]
9 0 0 3
After:  [0, 2, 2, 0]

Before: [1, 1, 2, 0]
2 1 2 1
After:  [1, 0, 2, 0]

Before: [3, 0, 1, 2]
1 2 2 0
After:  [2, 0, 1, 2]

Before: [0, 1, 2, 1]
2 1 2 3
After:  [0, 1, 2, 0]

Before: [0, 3, 3, 2]
7 3 1 0
After:  [1, 3, 3, 2]

Before: [3, 3, 2, 1]
5 3 2 0
After:  [1, 3, 2, 1]

Before: [2, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 1, 2, 3]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 2, 2, 3]
10 2 3 0
After:  [0, 2, 2, 3]

Before: [3, 3, 2, 1]
5 3 2 2
After:  [3, 3, 1, 1]

Before: [2, 1, 0, 3]
4 1 0 0
After:  [0, 1, 0, 3]

Before: [2, 1, 2, 3]
4 1 0 2
After:  [2, 1, 0, 3]

Before: [3, 3, 0, 3]
8 3 0 3
After:  [3, 3, 0, 1]

Before: [2, 1, 0, 3]
4 1 0 3
After:  [2, 1, 0, 0]

Before: [3, 1, 2, 1]
2 1 2 2
After:  [3, 1, 0, 1]

Before: [3, 3, 0, 2]
3 2 3 3
After:  [3, 3, 0, 1]

Before: [2, 2, 0, 1]
11 3 3 2
After:  [2, 2, 0, 1]

Before: [1, 1, 2, 0]
14 0 2 0
After:  [0, 1, 2, 0]

Before: [3, 2, 1, 3]
10 1 3 1
After:  [3, 0, 1, 3]

Before: [2, 1, 2, 3]
2 1 2 2
After:  [2, 1, 0, 3]

Before: [3, 2, 3, 3]
15 1 2 2
After:  [3, 2, 2, 3]

Before: [1, 1, 3, 0]
3 3 2 0
After:  [1, 1, 3, 0]

Before: [3, 3, 3, 3]
8 3 2 1
After:  [3, 1, 3, 3]

Before: [0, 1, 1, 1]
9 0 0 3
After:  [0, 1, 1, 0]

Before: [3, 0, 0, 2]
3 2 3 2
After:  [3, 0, 1, 2]

Before: [0, 2, 2, 2]
9 0 0 1
After:  [0, 0, 2, 2]

Before: [2, 1, 2, 1]
2 1 2 2
After:  [2, 1, 0, 1]

Before: [0, 1, 1, 3]
0 0 3 2
After:  [0, 1, 0, 3]

Before: [3, 2, 1, 3]
8 3 0 1
After:  [3, 1, 1, 3]

Before: [3, 1, 3, 3]
13 1 2 3
After:  [3, 1, 3, 0]

Before: [2, 1, 3, 2]
6 2 1 1
After:  [2, 0, 3, 2]

Before: [2, 3, 2, 3]
8 2 0 3
After:  [2, 3, 2, 1]

Before: [0, 0, 1, 3]
0 0 1 3
After:  [0, 0, 1, 0]

Before: [2, 1, 2, 1]
8 2 0 0
After:  [1, 1, 2, 1]

Before: [1, 0, 3, 3]
12 0 1 3
After:  [1, 0, 3, 1]

Before: [3, 2, 2, 1]
5 3 2 2
After:  [3, 2, 1, 1]

Before: [3, 3, 2, 2]
7 3 1 1
After:  [3, 1, 2, 2]

Before: [2, 2, 2, 1]
8 2 0 1
After:  [2, 1, 2, 1]

Before: [1, 3, 2, 0]
14 0 2 0
After:  [0, 3, 2, 0]

Before: [2, 3, 3, 2]
15 3 2 3
After:  [2, 3, 3, 2]

Before: [2, 0, 2, 3]
10 2 3 1
After:  [2, 0, 2, 3]

Before: [0, 3, 2, 2]
7 3 1 2
After:  [0, 3, 1, 2]

Before: [3, 0, 2, 2]
7 3 0 2
After:  [3, 0, 1, 2]

Before: [1, 0, 2, 3]
10 2 3 1
After:  [1, 0, 2, 3]

Before: [0, 0, 3, 2]
11 3 3 3
After:  [0, 0, 3, 0]

Before: [1, 0, 2, 1]
12 0 1 2
After:  [1, 0, 1, 1]

Before: [1, 0, 2, 1]
5 3 2 3
After:  [1, 0, 2, 1]

Before: [1, 3, 2, 2]
11 3 3 3
After:  [1, 3, 2, 0]

Before: [2, 2, 3, 0]
15 1 2 0
After:  [2, 2, 3, 0]

Before: [2, 3, 3, 2]
15 3 2 2
After:  [2, 3, 2, 2]

Before: [3, 3, 0, 3]
8 3 0 1
After:  [3, 1, 0, 3]

Before: [2, 2, 2, 3]
6 3 1 0
After:  [0, 2, 2, 3]

Before: [3, 1, 2, 3]
2 1 2 1
After:  [3, 0, 2, 3]

Before: [2, 1, 2, 0]
8 2 0 1
After:  [2, 1, 2, 0]

Before: [1, 1, 2, 3]
14 0 2 2
After:  [1, 1, 0, 3]

Before: [0, 2, 1, 2]
9 0 0 1
After:  [0, 0, 1, 2]

Before: [0, 1, 0, 3]
10 1 3 1
After:  [0, 0, 0, 3]

Before: [1, 3, 2, 0]
14 0 2 1
After:  [1, 0, 2, 0]

Before: [2, 0, 2, 3]
10 2 3 3
After:  [2, 0, 2, 0]

Before: [0, 3, 1, 1]
0 0 1 2
After:  [0, 3, 0, 1]

Before: [1, 3, 2, 3]
14 0 2 2
After:  [1, 3, 0, 3]

Before: [0, 2, 1, 1]
6 0 0 0
After:  [1, 2, 1, 1]

Before: [2, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [0, 1, 2, 0]
2 1 2 0
After:  [0, 1, 2, 0]

Before: [0, 0, 3, 1]
11 3 3 0
After:  [0, 0, 3, 1]

Before: [3, 0, 2, 1]
12 3 1 1
After:  [3, 1, 2, 1]

Before: [3, 0, 0, 1]
12 3 1 1
After:  [3, 1, 0, 1]

Before: [3, 0, 2, 1]
12 3 1 2
After:  [3, 0, 1, 1]

Before: [0, 0, 2, 1]
5 3 2 0
After:  [1, 0, 2, 1]

Before: [2, 1, 1, 0]
4 1 0 0
After:  [0, 1, 1, 0]

Before: [0, 2, 1, 0]
6 0 0 0
After:  [1, 2, 1, 0]

Before: [2, 0, 2, 1]
5 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 3, 1, 3]
1 2 2 2
After:  [3, 3, 2, 3]

Before: [0, 0, 1, 1]
12 3 1 2
After:  [0, 0, 1, 1]

Before: [1, 0, 3, 0]
3 3 2 3
After:  [1, 0, 3, 1]

Before: [1, 0, 1, 2]
12 2 1 3
After:  [1, 0, 1, 1]

Before: [0, 1, 1, 3]
10 2 3 3
After:  [0, 1, 1, 0]

Before: [3, 3, 0, 2]
7 3 0 0
After:  [1, 3, 0, 2]

Before: [0, 1, 2, 1]
2 1 2 2
After:  [0, 1, 0, 1]

Before: [2, 1, 3, 3]
4 1 0 0
After:  [0, 1, 3, 3]

Before: [2, 1, 3, 3]
4 1 0 1
After:  [2, 0, 3, 3]

Before: [3, 2, 1, 1]
11 2 3 1
After:  [3, 0, 1, 1]

Before: [0, 1, 2, 0]
2 1 2 1
After:  [0, 0, 2, 0]

Before: [2, 2, 0, 3]
6 3 3 3
After:  [2, 2, 0, 1]

Before: [2, 1, 2, 2]
2 1 2 1
After:  [2, 0, 2, 2]

Before: [0, 1, 3, 2]
15 3 2 0
After:  [2, 1, 3, 2]

Before: [0, 1, 2, 2]
2 1 2 3
After:  [0, 1, 2, 0]

Before: [1, 3, 2, 3]
10 2 3 2
After:  [1, 3, 0, 3]

Before: [1, 2, 3, 0]
3 3 2 3
After:  [1, 2, 3, 1]

Before: [0, 2, 1, 1]
1 2 2 2
After:  [0, 2, 2, 1]

Before: [2, 3, 2, 1]
5 3 2 2
After:  [2, 3, 1, 1]

Before: [1, 0, 0, 2]
3 2 3 2
After:  [1, 0, 1, 2]

Before: [2, 1, 0, 2]
3 2 3 3
After:  [2, 1, 0, 1]

Before: [0, 3, 3, 2]
15 3 2 1
After:  [0, 2, 3, 2]

Before: [3, 0, 3, 0]
3 3 2 2
After:  [3, 0, 1, 0]

Before: [0, 0, 2, 1]
11 3 3 1
After:  [0, 0, 2, 1]

Before: [0, 2, 0, 1]
0 0 3 1
After:  [0, 0, 0, 1]

Before: [2, 1, 0, 3]
4 1 0 1
After:  [2, 0, 0, 3]

Before: [2, 2, 1, 3]
1 2 2 0
After:  [2, 2, 1, 3]

Before: [0, 2, 2, 3]
10 1 3 1
After:  [0, 0, 2, 3]

Before: [1, 1, 1, 0]
1 2 2 2
After:  [1, 1, 2, 0]

Before: [0, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 3, 2, 1]
5 3 2 1
After:  [2, 1, 2, 1]

Before: [1, 1, 3, 2]
15 3 2 1
After:  [1, 2, 3, 2]

Before: [3, 2, 2, 3]
8 3 0 3
After:  [3, 2, 2, 1]

Before: [2, 2, 2, 3]
10 2 3 3
After:  [2, 2, 2, 0]

Before: [0, 0, 1, 3]
0 0 3 3
After:  [0, 0, 1, 0]

Before: [0, 0, 2, 1]
0 0 3 0
After:  [0, 0, 2, 1]

Before: [3, 2, 2, 3]
10 1 3 0
After:  [0, 2, 2, 3]

Before: [0, 1, 2, 3]
9 0 0 0
After:  [0, 1, 2, 3]

Before: [0, 0, 2, 3]
10 2 3 0
After:  [0, 0, 2, 3]

Before: [3, 2, 3, 1]
8 2 3 2
After:  [3, 2, 0, 1]

Before: [0, 1, 3, 1]
13 1 2 3
After:  [0, 1, 3, 0]

Before: [2, 2, 3, 1]
15 1 2 0
After:  [2, 2, 3, 1]

Before: [2, 1, 2, 3]
6 3 1 2
After:  [2, 1, 0, 3]

Before: [0, 2, 3, 3]
0 0 1 1
After:  [0, 0, 3, 3]

Before: [0, 1, 0, 2]
0 0 3 1
After:  [0, 0, 0, 2]

Before: [2, 0, 1, 3]
10 2 3 1
After:  [2, 0, 1, 3]

Before: [1, 1, 2, 1]
2 1 2 3
After:  [1, 1, 2, 0]

Before: [2, 1, 3, 1]
13 1 2 1
After:  [2, 0, 3, 1]

Before: [1, 0, 2, 0]
14 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 1, 2, 2]
2 1 2 2
After:  [0, 1, 0, 2]

Before: [1, 2, 0, 2]
3 2 3 0
After:  [1, 2, 0, 2]

Before: [2, 1, 1, 1]
11 2 3 2
After:  [2, 1, 0, 1]

Before: [1, 3, 3, 2]
15 3 2 2
After:  [1, 3, 2, 2]

Before: [1, 2, 3, 3]
10 1 3 0
After:  [0, 2, 3, 3]

Before: [0, 1, 3, 2]
9 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 1, 2, 3]
6 3 2 2
After:  [2, 1, 0, 3]

Before: [0, 2, 1, 3]
6 3 3 3
After:  [0, 2, 1, 1]

Before: [0, 2, 2, 1]
8 2 1 0
After:  [1, 2, 2, 1]

Before: [0, 2, 3, 3]
10 1 3 2
After:  [0, 2, 0, 3]

Before: [0, 3, 2, 0]
0 0 1 2
After:  [0, 3, 0, 0]

Before: [1, 0, 3, 0]
3 3 2 1
After:  [1, 1, 3, 0]

Before: [0, 0, 1, 2]
12 2 1 0
After:  [1, 0, 1, 2]

Before: [0, 3, 3, 3]
9 0 0 0
After:  [0, 3, 3, 3]

Before: [1, 0, 2, 1]
14 0 2 0
After:  [0, 0, 2, 1]

Before: [2, 0, 3, 2]
11 3 3 1
After:  [2, 0, 3, 2]

Before: [0, 2, 2, 1]
8 2 1 3
After:  [0, 2, 2, 1]

Before: [0, 1, 1, 0]
9 0 0 0
After:  [0, 1, 1, 0]

Before: [1, 1, 2, 0]
14 0 2 3
After:  [1, 1, 2, 0]

Before: [0, 3, 0, 1]
9 0 0 0
After:  [0, 3, 0, 1]

Before: [1, 0, 3, 1]
8 2 3 0
After:  [0, 0, 3, 1]

Before: [3, 1, 2, 3]
8 3 0 1
After:  [3, 1, 2, 3]

Before: [0, 1, 2, 1]
0 0 1 2
After:  [0, 1, 0, 1]

Before: [2, 1, 2, 1]
4 1 0 0
After:  [0, 1, 2, 1]

Before: [2, 3, 3, 0]
3 3 2 2
After:  [2, 3, 1, 0]

Before: [0, 3, 2, 3]
9 0 0 1
After:  [0, 0, 2, 3]

Before: [3, 3, 1, 0]
1 2 2 3
After:  [3, 3, 1, 2]

Before: [3, 0, 1, 0]
1 2 2 2
After:  [3, 0, 2, 0]

Before: [0, 1, 2, 0]
2 1 2 2
After:  [0, 1, 0, 0]

Before: [2, 1, 0, 1]
4 1 0 1
After:  [2, 0, 0, 1]

Before: [0, 0, 1, 0]
12 2 1 0
After:  [1, 0, 1, 0]

Before: [2, 0, 0, 2]
3 2 3 2
After:  [2, 0, 1, 2]

Before: [2, 2, 3, 1]
15 0 2 1
After:  [2, 2, 3, 1]

Before: [0, 1, 1, 0]
0 0 1 1
After:  [0, 0, 1, 0]

Before: [1, 1, 1, 3]
10 2 3 2
After:  [1, 1, 0, 3]

Before: [0, 1, 2, 0]
2 1 2 3
After:  [0, 1, 2, 0]

Before: [2, 3, 3, 0]
3 3 2 3
After:  [2, 3, 3, 1]

Before: [3, 1, 3, 2]
13 1 2 1
After:  [3, 0, 3, 2]

Before: [0, 1, 1, 3]
1 2 2 3
After:  [0, 1, 1, 2]

Before: [2, 0, 3, 1]
8 2 3 1
After:  [2, 0, 3, 1]

Before: [0, 1, 1, 0]
0 0 3 3
After:  [0, 1, 1, 0]

Before: [1, 2, 3, 1]
15 1 2 2
After:  [1, 2, 2, 1]

Before: [1, 1, 2, 2]
2 1 2 3
After:  [1, 1, 2, 0]

Before: [1, 0, 2, 1]
11 3 3 3
After:  [1, 0, 2, 0]

Before: [2, 0, 2, 1]
5 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 3, 1, 2]
11 3 3 2
After:  [1, 3, 0, 2]

Before: [1, 0, 2, 2]
12 0 1 1
After:  [1, 1, 2, 2]

Before: [2, 1, 3, 0]
13 1 2 0
After:  [0, 1, 3, 0]

Before: [2, 2, 2, 1]
5 3 2 2
After:  [2, 2, 1, 1]

Before: [3, 2, 3, 2]
7 3 0 0
After:  [1, 2, 3, 2]

Before: [1, 2, 3, 1]
8 2 3 3
After:  [1, 2, 3, 0]

Before: [3, 3, 0, 2]
7 3 0 3
After:  [3, 3, 0, 1]

Before: [0, 0, 3, 0]
3 3 2 2
After:  [0, 0, 1, 0]

Before: [1, 2, 2, 2]
14 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 1, 1, 3]
10 2 3 0
After:  [0, 1, 1, 3]

Before: [1, 1, 3, 0]
13 1 2 2
After:  [1, 1, 0, 0]

Before: [0, 0, 2, 3]
9 0 0 2
After:  [0, 0, 0, 3]

Before: [0, 3, 2, 1]
5 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 1, 0, 3]
10 1 3 1
After:  [2, 0, 0, 3]

Before: [0, 0, 3, 3]
8 3 2 2
After:  [0, 0, 1, 3]

Before: [2, 1, 2, 1]
11 3 3 1
After:  [2, 0, 2, 1]

Before: [3, 1, 2, 2]
7 3 0 0
After:  [1, 1, 2, 2]

Before: [0, 2, 1, 1]
11 3 3 2
After:  [0, 2, 0, 1]

Before: [2, 1, 2, 0]
4 1 0 3
After:  [2, 1, 2, 0]

Before: [3, 2, 3, 1]
15 1 2 0
After:  [2, 2, 3, 1]

Before: [2, 0, 3, 2]
15 0 2 3
After:  [2, 0, 3, 2]

Before: [2, 3, 1, 2]
7 3 1 0
After:  [1, 3, 1, 2]

Before: [2, 1, 2, 1]
11 3 3 0
After:  [0, 1, 2, 1]

Before: [0, 3, 2, 1]
5 3 2 2
After:  [0, 3, 1, 1]

Before: [0, 1, 3, 1]
13 1 2 2
After:  [0, 1, 0, 1]

Before: [3, 3, 3, 0]
3 3 2 1
After:  [3, 1, 3, 0]

Before: [0, 1, 2, 3]
2 1 2 2
After:  [0, 1, 0, 3]

Before: [2, 1, 1, 1]
1 2 2 0
After:  [2, 1, 1, 1]

Before: [2, 1, 1, 2]
1 2 2 1
After:  [2, 2, 1, 2]

Before: [0, 2, 2, 0]
6 0 0 3
After:  [0, 2, 2, 1]

Before: [0, 3, 3, 0]
9 0 0 0
After:  [0, 3, 3, 0]

Before: [2, 1, 3, 2]
11 3 3 2
After:  [2, 1, 0, 2]

Before: [0, 0, 0, 1]
12 3 1 2
After:  [0, 0, 1, 1]

Before: [2, 1, 3, 3]
15 0 2 2
After:  [2, 1, 2, 3]

Before: [0, 1, 3, 0]
3 3 2 3
After:  [0, 1, 3, 1]

Before: [2, 1, 2, 0]
4 1 0 1
After:  [2, 0, 2, 0]

Before: [0, 2, 0, 1]
9 0 0 3
After:  [0, 2, 0, 0]

Before: [1, 2, 2, 0]
14 0 2 0
After:  [0, 2, 2, 0]

Before: [0, 0, 2, 1]
9 0 0 1
After:  [0, 0, 2, 1]

Before: [3, 2, 2, 1]
5 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 1, 2, 3]
14 0 2 0
After:  [0, 1, 2, 3]

Before: [0, 3, 2, 2]
7 3 1 0
After:  [1, 3, 2, 2]

Before: [2, 1, 3, 0]
4 1 0 0
After:  [0, 1, 3, 0]

Before: [2, 1, 0, 1]
11 3 3 3
After:  [2, 1, 0, 0]

Before: [2, 0, 3, 0]
15 0 2 1
After:  [2, 2, 3, 0]

Before: [3, 0, 0, 2]
3 2 3 3
After:  [3, 0, 0, 1]

Before: [3, 1, 2, 0]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 1, 2, 1]
2 1 2 1
After:  [0, 0, 2, 1]

Before: [1, 0, 2, 3]
6 2 2 1
After:  [1, 1, 2, 3]

Before: [2, 1, 3, 2]
13 1 2 3
After:  [2, 1, 3, 0]

Before: [2, 1, 1, 1]
4 1 0 0
After:  [0, 1, 1, 1]

Before: [0, 1, 1, 2]
0 0 2 0
After:  [0, 1, 1, 2]

Before: [3, 0, 0, 1]
12 3 1 2
After:  [3, 0, 1, 1]

Before: [0, 2, 1, 3]
0 0 2 1
After:  [0, 0, 1, 3]

Before: [1, 1, 2, 3]
14 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 3, 2, 2]
7 3 1 1
After:  [1, 1, 2, 2]

Before: [0, 1, 3, 0]
3 3 2 2
After:  [0, 1, 1, 0]

Before: [1, 2, 3, 0]
15 1 2 3
After:  [1, 2, 3, 2]

Before: [1, 0, 1, 3]
12 2 1 0
After:  [1, 0, 1, 3]

Before: [3, 3, 1, 3]
8 3 0 3
After:  [3, 3, 1, 1]

Before: [0, 2, 2, 1]
5 3 2 2
After:  [0, 2, 1, 1]

Before: [1, 3, 2, 1]
14 0 2 2
After:  [1, 3, 0, 1]

Before: [3, 0, 3, 0]
3 3 2 1
After:  [3, 1, 3, 0]

Before: [0, 0, 2, 1]
5 3 2 2
After:  [0, 0, 1, 1]

Before: [1, 1, 2, 3]
14 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [2, 1, 2, 1]
4 1 0 3
After:  [2, 1, 2, 0]

Before: [0, 0, 1, 3]
10 2 3 0
After:  [0, 0, 1, 3]

Before: [2, 2, 1, 1]
1 2 2 1
After:  [2, 2, 1, 1]

Before: [2, 1, 3, 3]
13 1 2 2
After:  [2, 1, 0, 3]

Before: [0, 2, 2, 3]
0 0 2 0
After:  [0, 2, 2, 3]

Before: [2, 1, 2, 3]
4 1 0 0
After:  [0, 1, 2, 3]

Before: [2, 1, 3, 2]
4 1 0 3
After:  [2, 1, 3, 0]

Before: [0, 3, 0, 3]
9 0 0 2
After:  [0, 3, 0, 3]

Before: [2, 0, 1, 0]
1 2 2 2
After:  [2, 0, 2, 0]

Before: [1, 0, 3, 2]
11 3 3 3
After:  [1, 0, 3, 0]

Before: [1, 0, 2, 2]
6 2 2 1
After:  [1, 1, 2, 2]

Before: [0, 2, 0, 3]
9 0 0 3
After:  [0, 2, 0, 0]

Before: [2, 0, 1, 1]
12 2 1 3
After:  [2, 0, 1, 1]

Before: [2, 1, 0, 2]
4 1 0 2
After:  [2, 1, 0, 2]

Before: [0, 1, 2, 2]
2 1 2 1
After:  [0, 0, 2, 2]

Before: [3, 0, 3, 2]
15 3 2 0
After:  [2, 0, 3, 2]

Before: [3, 1, 3, 3]
13 1 2 0
After:  [0, 1, 3, 3]

Before: [1, 1, 2, 2]
2 1 2 1
After:  [1, 0, 2, 2]

Before: [1, 2, 1, 3]
10 2 3 3
After:  [1, 2, 1, 0]

Before: [0, 2, 2, 1]
8 2 1 1
After:  [0, 1, 2, 1]

Before: [0, 3, 2, 1]
5 3 2 3
After:  [0, 3, 2, 1]

Before: [3, 0, 2, 1]
12 3 1 3
After:  [3, 0, 2, 1]

Before: [1, 3, 3, 2]
15 3 2 3
After:  [1, 3, 3, 2]

Before: [2, 3, 0, 2]
3 2 3 2
After:  [2, 3, 1, 2]

Before: [3, 3, 2, 2]
6 2 2 2
After:  [3, 3, 1, 2]

Before: [3, 3, 2, 2]
7 3 0 0
After:  [1, 3, 2, 2]

Before: [2, 1, 0, 2]
4 1 0 3
After:  [2, 1, 0, 0]

Before: [1, 2, 2, 2]
14 0 2 1
After:  [1, 0, 2, 2]

Before: [0, 1, 0, 3]
0 0 1 1
After:  [0, 0, 0, 3]

Before: [2, 1, 1, 3]
4 1 0 0
After:  [0, 1, 1, 3]

Before: [2, 0, 1, 1]
12 3 1 0
After:  [1, 0, 1, 1]

Before: [2, 1, 2, 0]
2 1 2 1
After:  [2, 0, 2, 0]

Before: [3, 1, 2, 3]
10 1 3 2
After:  [3, 1, 0, 3]

Before: [2, 1, 1, 0]
4 1 0 1
After:  [2, 0, 1, 0]

Before: [2, 1, 3, 3]
10 1 3 3
After:  [2, 1, 3, 0]

Before: [1, 0, 0, 1]
12 0 1 3
After:  [1, 0, 0, 1]

Before: [3, 0, 1, 3]
12 2 1 3
After:  [3, 0, 1, 1]

Before: [1, 1, 3, 1]
8 2 3 1
After:  [1, 0, 3, 1]

Before: [1, 2, 2, 3]
14 0 2 0
After:  [0, 2, 2, 3]

Before: [0, 1, 1, 3]
9 0 0 1
After:  [0, 0, 1, 3]

Before: [0, 2, 2, 1]
11 3 3 3
After:  [0, 2, 2, 0]

Before: [2, 1, 2, 2]
2 1 2 2
After:  [2, 1, 0, 2]

Before: [0, 1, 3, 1]
13 1 2 1
After:  [0, 0, 3, 1]

Before: [1, 1, 3, 0]
3 3 2 1
After:  [1, 1, 3, 0]

Before: [3, 2, 0, 1]
11 3 3 2
After:  [3, 2, 0, 1]

Before: [2, 2, 3, 2]
15 0 2 0
After:  [2, 2, 3, 2]

Before: [1, 3, 2, 3]
14 0 2 0
After:  [0, 3, 2, 3]

Before: [1, 2, 3, 3]
10 1 3 2
After:  [1, 2, 0, 3]

Before: [1, 0, 1, 2]
1 2 2 2
After:  [1, 0, 2, 2]

Before: [3, 3, 1, 3]
8 3 0 0
After:  [1, 3, 1, 3]

Before: [1, 3, 3, 3]
8 3 2 0
After:  [1, 3, 3, 3]

Before: [3, 3, 2, 2]
7 3 0 1
After:  [3, 1, 2, 2]

Before: [1, 2, 3, 3]
15 1 2 2
After:  [1, 2, 2, 3]

Before: [3, 1, 2, 0]
2 1 2 2
After:  [3, 1, 0, 0]

Before: [2, 2, 2, 1]
5 3 2 3
After:  [2, 2, 2, 1]

Before: [0, 1, 1, 2]
9 0 0 2
After:  [0, 1, 0, 2]

Before: [0, 2, 0, 3]
0 0 2 2
After:  [0, 2, 0, 3]

Before: [0, 3, 1, 1]
9 0 0 1
After:  [0, 0, 1, 1]

Before: [3, 1, 2, 3]
10 2 3 0
After:  [0, 1, 2, 3]

Before: [3, 0, 3, 1]
12 3 1 3
After:  [3, 0, 3, 1]

Before: [1, 3, 2, 2]
7 3 1 3
After:  [1, 3, 2, 1]

Before: [0, 2, 3, 0]
3 3 2 3
After:  [0, 2, 3, 1]

Before: [3, 1, 1, 2]
11 3 3 3
After:  [3, 1, 1, 0]

Before: [1, 0, 2, 3]
14 0 2 1
After:  [1, 0, 2, 3]

Before: [1, 2, 3, 0]
3 3 2 1
After:  [1, 1, 3, 0]

Before: [3, 0, 1, 3]
10 2 3 3
After:  [3, 0, 1, 0]

Before: [2, 0, 3, 1]
12 3 1 2
After:  [2, 0, 1, 1]

Before: [3, 1, 3, 2]
11 3 3 1
After:  [3, 0, 3, 2]

Before: [0, 3, 2, 0]
9 0 0 3
After:  [0, 3, 2, 0]

Before: [1, 0, 2, 3]
12 0 1 2
After:  [1, 0, 1, 3]

Before: [3, 3, 1, 3]
10 2 3 0
After:  [0, 3, 1, 3]

Before: [3, 3, 2, 0]
6 2 2 3
After:  [3, 3, 2, 1]

Before: [0, 1, 3, 0]
3 3 2 1
After:  [0, 1, 3, 0]

Before: [1, 2, 2, 0]
8 2 1 1
After:  [1, 1, 2, 0]

Before: [1, 1, 3, 2]
13 1 2 0
After:  [0, 1, 3, 2]

Before: [2, 1, 2, 3]
10 1 3 1
After:  [2, 0, 2, 3]

Before: [1, 3, 2, 0]
14 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 2, 3, 2]
15 1 2 1
After:  [0, 2, 3, 2]

Before: [1, 3, 0, 2]
3 2 3 1
After:  [1, 1, 0, 2]

Before: [3, 1, 2, 0]
2 1 2 1
After:  [3, 0, 2, 0]

Before: [1, 1, 2, 2]
14 0 2 1
After:  [1, 0, 2, 2]

Before: [1, 3, 3, 0]
3 3 2 0
After:  [1, 3, 3, 0]

Before: [0, 3, 0, 2]
7 3 1 1
After:  [0, 1, 0, 2]

Before: [3, 1, 3, 3]
13 1 2 2
After:  [3, 1, 0, 3]

Before: [3, 2, 1, 3]
10 2 3 1
After:  [3, 0, 1, 3]

Before: [1, 1, 3, 2]
13 1 2 2
After:  [1, 1, 0, 2]

Before: [1, 2, 2, 3]
14 0 2 3
After:  [1, 2, 2, 0]

Before: [0, 1, 1, 2]
11 3 3 3
After:  [0, 1, 1, 0]

Before: [3, 1, 3, 1]
13 1 2 1
After:  [3, 0, 3, 1]

Before: [2, 1, 1, 3]
1 2 2 2
After:  [2, 1, 2, 3]

Before: [0, 1, 1, 0]
1 2 2 3
After:  [0, 1, 1, 2]

Before: [1, 1, 3, 3]
13 1 2 0
After:  [0, 1, 3, 3]

Before: [1, 3, 1, 2]
7 3 1 3
After:  [1, 3, 1, 1]

Before: [1, 0, 3, 2]
12 0 1 0
After:  [1, 0, 3, 2]

Before: [2, 1, 3, 0]
4 1 0 1
After:  [2, 0, 3, 0]

Before: [2, 1, 1, 3]
4 1 0 2
After:  [2, 1, 0, 3]

Before: [2, 2, 3, 3]
10 1 3 2
After:  [2, 2, 0, 3]

Before: [2, 1, 3, 2]
15 0 2 0
After:  [2, 1, 3, 2]

Before: [2, 1, 0, 1]
4 1 0 2
After:  [2, 1, 0, 1]

Before: [3, 0, 0, 1]
11 3 3 1
After:  [3, 0, 0, 1]

Before: [1, 0, 2, 3]
6 3 3 0
After:  [1, 0, 2, 3]

Before: [1, 1, 2, 1]
2 1 2 1
After:  [1, 0, 2, 1]

Before: [2, 1, 0, 0]
4 1 0 0
After:  [0, 1, 0, 0]

Before: [0, 0, 0, 3]
6 3 3 1
After:  [0, 1, 0, 3]

Before: [1, 3, 0, 2]
7 3 1 1
After:  [1, 1, 0, 2]

Before: [2, 2, 1, 2]
11 3 3 2
After:  [2, 2, 0, 2]

Before: [1, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [0, 0, 0, 2]
11 3 3 2
After:  [0, 0, 0, 2]

Before: [2, 1, 3, 3]
4 1 0 3
After:  [2, 1, 3, 0]

Before: [2, 2, 0, 3]
10 1 3 3
After:  [2, 2, 0, 0]

Before: [2, 1, 2, 0]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [1, 0, 2, 0]
14 0 2 1
After:  [1, 0, 2, 0]

Before: [2, 1, 2, 3]
6 3 1 1
After:  [2, 0, 2, 3]

Before: [0, 0, 3, 2]
0 0 1 1
After:  [0, 0, 3, 2]

Before: [0, 1, 3, 0]
9 0 0 2
After:  [0, 1, 0, 0]

Before: [0, 1, 3, 1]
0 0 3 2
After:  [0, 1, 0, 1]

Before: [0, 2, 3, 2]
15 3 2 2
After:  [0, 2, 2, 2]

Before: [3, 0, 1, 2]
7 3 0 3
After:  [3, 0, 1, 1]

Before: [3, 1, 1, 2]
7 3 0 1
After:  [3, 1, 1, 2]

Before: [2, 1, 2, 0]
8 2 0 0
After:  [1, 1, 2, 0]

Before: [2, 1, 3, 0]
13 1 2 3
After:  [2, 1, 3, 0]

Before: [0, 3, 0, 0]
9 0 0 3
After:  [0, 3, 0, 0]

Before: [3, 1, 1, 2]
1 2 2 2
After:  [3, 1, 2, 2]

Before: [0, 0, 1, 0]
9 0 0 1
After:  [0, 0, 1, 0]

Before: [0, 2, 2, 1]
11 3 3 0
After:  [0, 2, 2, 1]

Before: [2, 3, 1, 2]
11 3 3 3
After:  [2, 3, 1, 0]

Before: [3, 3, 3, 2]
7 3 0 2
After:  [3, 3, 1, 2]

Before: [2, 1, 3, 2]
15 0 2 2
After:  [2, 1, 2, 2]

Before: [3, 1, 1, 2]
7 3 0 3
After:  [3, 1, 1, 1]

Before: [0, 0, 3, 1]
11 3 3 1
After:  [0, 0, 3, 1]

Before: [0, 3, 2, 1]
5 3 2 0
After:  [1, 3, 2, 1]

Before: [2, 1, 3, 0]
3 3 2 1
After:  [2, 1, 3, 0]

Before: [2, 0, 0, 1]
12 3 1 0
After:  [1, 0, 0, 1]

Before: [1, 3, 2, 1]
5 3 2 3
After:  [1, 3, 2, 1]

Before: [1, 3, 2, 1]
14 0 2 0
After:  [0, 3, 2, 1]

Before: [1, 3, 1, 2]
7 3 1 1
After:  [1, 1, 1, 2]

Before: [2, 0, 2, 1]
12 3 1 3
After:  [2, 0, 2, 1]

Before: [3, 0, 1, 0]
1 2 2 3
After:  [3, 0, 1, 2]

Before: [1, 3, 0, 2]
7 3 1 0
After:  [1, 3, 0, 2]

Before: [0, 0, 3, 1]
8 2 3 0
After:  [0, 0, 3, 1]

Before: [2, 0, 3, 1]
15 0 2 3
After:  [2, 0, 3, 2]

Before: [0, 0, 0, 1]
0 0 3 1
After:  [0, 0, 0, 1]

Before: [0, 3, 1, 3]
1 2 2 2
After:  [0, 3, 2, 3]

Before: [2, 1, 1, 3]
10 1 3 0
After:  [0, 1, 1, 3]

Before: [0, 2, 1, 2]
11 3 3 1
After:  [0, 0, 1, 2]

Before: [3, 2, 2, 1]
5 3 2 3
After:  [3, 2, 2, 1]

Before: [3, 3, 2, 2]
7 3 1 2
After:  [3, 3, 1, 2]

Before: [0, 2, 2, 2]
0 0 3 3
After:  [0, 2, 2, 0]

Before: [2, 1, 2, 1]
4 1 0 1
After:  [2, 0, 2, 1]

Before: [3, 1, 2, 2]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [1, 0, 1, 2]
12 0 1 0
After:  [1, 0, 1, 2]

Before: [0, 0, 3, 0]
3 3 2 3
After:  [0, 0, 3, 1]

Before: [1, 1, 2, 1]
5 3 2 3
After:  [1, 1, 2, 1]

Before: [3, 3, 1, 1]
11 3 3 1
After:  [3, 0, 1, 1]

Before: [1, 0, 0, 2]
12 0 1 3
After:  [1, 0, 0, 1]

Before: [1, 2, 1, 3]
1 2 2 2
After:  [1, 2, 2, 3]

Before: [3, 0, 2, 1]
5 3 2 1
After:  [3, 1, 2, 1]

Before: [0, 0, 0, 1]
0 0 2 3
After:  [0, 0, 0, 0]

Before: [3, 1, 3, 3]
13 1 2 1
After:  [3, 0, 3, 3]

Before: [1, 2, 1, 0]
1 2 2 2
After:  [1, 2, 2, 0]

Before: [0, 3, 2, 1]
9 0 0 0
After:  [0, 3, 2, 1]

Before: [0, 3, 3, 1]
8 2 3 0
After:  [0, 3, 3, 1]

Before: [2, 1, 2, 0]
2 1 2 0
After:  [0, 1, 2, 0]

Before: [2, 1, 1, 2]
4 1 0 1
After:  [2, 0, 1, 2]

Before: [1, 1, 1, 3]
10 2 3 3
After:  [1, 1, 1, 0]

Before: [3, 0, 1, 0]
12 2 1 0
After:  [1, 0, 1, 0]

Before: [3, 2, 1, 2]
7 3 0 3
After:  [3, 2, 1, 1]

Before: [1, 1, 3, 2]
11 3 3 3
After:  [1, 1, 3, 0]

Before: [0, 3, 3, 2]
15 3 2 2
After:  [0, 3, 2, 2]

Before: [0, 0, 0, 0]
9 0 0 2
After:  [0, 0, 0, 0]

Before: [1, 1, 3, 0]
13 1 2 0
After:  [0, 1, 3, 0]

Before: [0, 1, 3, 3]
9 0 0 3
After:  [0, 1, 3, 0]

Before: [0, 0, 1, 2]
1 2 2 0
After:  [2, 0, 1, 2]

Before: [1, 2, 3, 3]
8 3 2 3
After:  [1, 2, 3, 1]

Before: [3, 3, 3, 2]
15 3 2 1
After:  [3, 2, 3, 2]

Before: [0, 1, 3, 0]
13 1 2 1
After:  [0, 0, 3, 0]

Before: [2, 0, 2, 1]
5 3 2 2
After:  [2, 0, 1, 1]

Before: [3, 2, 0, 3]
10 1 3 2
After:  [3, 2, 0, 3]

Before: [3, 3, 1, 2]
1 2 2 0
After:  [2, 3, 1, 2]

Before: [3, 1, 2, 3]
6 3 2 0
After:  [0, 1, 2, 3]

Before: [0, 2, 2, 3]
6 2 2 3
After:  [0, 2, 2, 1]

Before: [3, 3, 3, 2]
7 3 0 0
After:  [1, 3, 3, 2]

Before: [0, 1, 1, 2]
6 0 0 3
After:  [0, 1, 1, 1]

Before: [0, 0, 3, 0]
0 0 2 0
After:  [0, 0, 3, 0]

Before: [3, 1, 2, 2]
2 1 2 2
After:  [3, 1, 0, 2]

Before: [0, 1, 2, 1]
5 3 2 1
After:  [0, 1, 2, 1]

Before: [1, 1, 1, 1]
1 2 2 2
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 2]
14 0 2 2
After:  [1, 1, 0, 2]

Before: [2, 1, 1, 1]
4 1 0 2
After:  [2, 1, 0, 1]

Before: [2, 2, 2, 1]
5 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 1, 2, 3]
2 1 2 2
After:  [1, 1, 0, 3]

Before: [3, 1, 2, 1]
2 1 2 0
After:  [0, 1, 2, 1]

Before: [0, 2, 3, 1]
6 0 0 3
After:  [0, 2, 3, 1]

Before: [0, 2, 3, 2]
15 3 2 0
After:  [2, 2, 3, 2]

Before: [2, 1, 3, 1]
4 1 0 2
After:  [2, 1, 0, 1]

Before: [3, 1, 3, 1]
13 1 2 0
After:  [0, 1, 3, 1]

Before: [2, 1, 3, 3]
13 1 2 0
After:  [0, 1, 3, 3]

Before: [1, 0, 2, 3]
12 0 1 0
After:  [1, 0, 2, 3]

Before: [3, 0, 2, 3]
8 3 0 0
After:  [1, 0, 2, 3]

Before: [0, 0, 1, 1]
12 2 1 0
After:  [1, 0, 1, 1]

Before: [0, 0, 3, 0]
0 0 1 2
After:  [0, 0, 0, 0]

Before: [0, 3, 1, 2]
7 3 1 1
After:  [0, 1, 1, 2]

Before: [2, 1, 1, 2]
4 1 0 2
After:  [2, 1, 0, 2]

Before: [0, 2, 3, 1]
0 0 2 0
After:  [0, 2, 3, 1]

Before: [3, 1, 2, 1]
5 3 2 3
After:  [3, 1, 2, 1]

Before: [3, 3, 1, 2]
7 3 1 2
After:  [3, 3, 1, 2]

Before: [0, 1, 0, 1]
0 0 3 2
After:  [0, 1, 0, 1]

Before: [2, 2, 2, 3]
10 2 3 1
After:  [2, 0, 2, 3]

Before: [0, 1, 1, 3]
1 2 2 1
After:  [0, 2, 1, 3]

Before: [3, 2, 2, 1]
11 3 3 3
After:  [3, 2, 2, 0]

Before: [0, 1, 0, 3]
9 0 0 0
After:  [0, 1, 0, 3]

Before: [2, 0, 2, 2]
8 2 0 3
After:  [2, 0, 2, 1]

Before: [3, 0, 1, 1]
12 2 1 0
After:  [1, 0, 1, 1]

Before: [3, 2, 2, 3]
10 2 3 2
After:  [3, 2, 0, 3]

Before: [1, 0, 3, 2]
15 3 2 1
After:  [1, 2, 3, 2]

Before: [1, 3, 1, 2]
11 3 3 3
After:  [1, 3, 1, 0]

Before: [3, 0, 2, 1]
5 3 2 2
After:  [3, 0, 1, 1]

Before: [2, 0, 1, 2]
12 2 1 3
After:  [2, 0, 1, 1]

Before: [2, 1, 3, 3]
13 1 2 3
After:  [2, 1, 3, 0]

Before: [2, 1, 2, 2]
4 1 0 2
After:  [2, 1, 0, 2]

Before: [0, 2, 2, 0]
0 0 2 0
After:  [0, 2, 2, 0]

Before: [3, 2, 2, 1]
6 2 2 0
After:  [1, 2, 2, 1]

Before: [1, 3, 2, 1]
5 3 2 0
After:  [1, 3, 2, 1]

Before: [1, 2, 2, 1]
5 3 2 3
After:  [1, 2, 2, 1]

Before: [3, 1, 3, 3]
10 1 3 3
After:  [3, 1, 3, 0]

Before: [0, 1, 1, 3]
0 0 2 1
After:  [0, 0, 1, 3]

Before: [3, 0, 3, 3]
6 3 3 3
After:  [3, 0, 3, 1]

Before: [1, 3, 3, 2]
7 3 1 1
After:  [1, 1, 3, 2]

Before: [2, 1, 3, 1]
4 1 0 1
After:  [2, 0, 3, 1]

Before: [3, 2, 2, 3]
10 1 3 3
After:  [3, 2, 2, 0]

Before: [2, 0, 3, 1]
12 3 1 1
After:  [2, 1, 3, 1]

Before: [0, 2, 0, 3]
10 1 3 2
After:  [0, 2, 0, 3]

Before: [2, 3, 1, 3]
10 2 3 0
After:  [0, 3, 1, 3]

Before: [1, 1, 2, 3]
10 2 3 0
After:  [0, 1, 2, 3]

Before: [2, 1, 2, 0]
4 1 0 2
After:  [2, 1, 0, 0]

Before: [2, 3, 3, 3]
15 0 2 0
After:  [2, 3, 3, 3]

Before: [2, 2, 3, 3]
15 1 2 2
After:  [2, 2, 2, 3]

Before: [0, 3, 1, 2]
7 3 1 0
After:  [1, 3, 1, 2]

Before: [0, 1, 1, 3]
6 3 3 0
After:  [1, 1, 1, 3]

Before: [1, 0, 1, 1]
11 2 3 0
After:  [0, 0, 1, 1]

Before: [2, 1, 2, 1]
5 3 2 3
After:  [2, 1, 2, 1]

Before: [0, 3, 0, 2]
3 2 3 1
After:  [0, 1, 0, 2]

Before: [2, 0, 1, 3]
10 2 3 0
After:  [0, 0, 1, 3]

Before: [0, 3, 0, 1]
9 0 0 2
After:  [0, 3, 0, 1]

Before: [3, 2, 2, 1]
5 3 2 1
After:  [3, 1, 2, 1]

Before: [0, 1, 1, 1]
11 3 3 2
After:  [0, 1, 0, 1]

Before: [2, 3, 3, 2]
7 3 1 2
After:  [2, 3, 1, 2]

Before: [2, 1, 2, 1]
5 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 0, 2, 1]
5 3 2 3
After:  [2, 0, 2, 1]

Before: [3, 0, 1, 1]
12 3 1 2
After:  [3, 0, 1, 1]

Before: [3, 0, 1, 1]
12 3 1 3
After:  [3, 0, 1, 1]

Before: [3, 0, 1, 0]
1 2 2 1
After:  [3, 2, 1, 0]

Before: [3, 0, 2, 1]
11 3 3 1
After:  [3, 0, 2, 1]

Before: [2, 1, 1, 3]
4 1 0 1
After:  [2, 0, 1, 3]

Before: [0, 2, 2, 3]
0 0 3 1
After:  [0, 0, 2, 3]

Before: [0, 1, 2, 1]
5 3 2 0
After:  [1, 1, 2, 1]

Before: [0, 1, 3, 1]
13 1 2 0
After:  [0, 1, 3, 1]

Before: [1, 0, 1, 3]
1 2 2 3
After:  [1, 0, 1, 2]

Before: [1, 3, 2, 1]
14 0 2 1
After:  [1, 0, 2, 1]

Before: [3, 1, 2, 2]
2 1 2 1
After:  [3, 0, 2, 2]

Before: [0, 1, 3, 2]
15 3 2 1
After:  [0, 2, 3, 2]

Before: [2, 1, 0, 1]
4 1 0 3
After:  [2, 1, 0, 0]

Before: [0, 0, 2, 3]
6 0 0 3
After:  [0, 0, 2, 1]

Before: [1, 3, 0, 2]
3 2 3 2
After:  [1, 3, 1, 2]

Before: [2, 1, 1, 0]
1 2 2 0
After:  [2, 1, 1, 0]

Before: [0, 2, 0, 2]
6 0 0 0
After:  [1, 2, 0, 2]

Before: [3, 1, 3, 3]
8 3 0 3
After:  [3, 1, 3, 1]

Before: [2, 1, 3, 2]
4 1 0 1
After:  [2, 0, 3, 2]

Before: [2, 1, 1, 2]
4 1 0 3
After:  [2, 1, 1, 0]

Before: [0, 0, 2, 1]
12 3 1 3
After:  [0, 0, 2, 1]

Before: [3, 0, 1, 3]
12 2 1 0
After:  [1, 0, 1, 3]

Before: [2, 2, 2, 3]
6 3 2 1
After:  [2, 0, 2, 3]

Before: [1, 2, 2, 3]
14 0 2 2
After:  [1, 2, 0, 3]

Before: [2, 1, 2, 0]
2 1 2 2
After:  [2, 1, 0, 0]

Before: [0, 2, 2, 2]
0 0 1 2
After:  [0, 2, 0, 2]

Before: [1, 0, 1, 3]
10 2 3 2
After:  [1, 0, 0, 3]

Before: [1, 1, 3, 3]
13 1 2 2
After:  [1, 1, 0, 3]

Before: [2, 2, 3, 2]
15 1 2 2
After:  [2, 2, 2, 2]

Before: [0, 0, 0, 1]
6 0 0 2
After:  [0, 0, 1, 1]

Before: [1, 1, 0, 2]
3 2 3 1
After:  [1, 1, 0, 2]

Before: [2, 1, 0, 2]
4 1 0 0
After:  [0, 1, 0, 2]

Before: [1, 1, 3, 0]
13 1 2 1
After:  [1, 0, 3, 0]

Before: [1, 3, 3, 2]
15 3 2 1
After:  [1, 2, 3, 2]

Before: [1, 2, 1, 1]
1 2 2 2
After:  [1, 2, 2, 1]

Before: [1, 3, 2, 2]
6 2 2 2
After:  [1, 3, 1, 2]

Before: [0, 3, 3, 1]
8 2 3 3
After:  [0, 3, 3, 0]

Before: [3, 2, 3, 3]
10 1 3 2
After:  [3, 2, 0, 3]

Before: [1, 1, 3, 1]
13 1 2 3
After:  [1, 1, 3, 0]

Before: [2, 2, 2, 1]
6 2 2 1
After:  [2, 1, 2, 1]

Before: [1, 2, 2, 1]
14 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 0, 1, 1]
9 0 0 2
After:  [0, 0, 0, 1]

Before: [0, 1, 2, 1]
9 0 0 1
After:  [0, 0, 2, 1]

Before: [0, 2, 2, 0]
8 2 1 2
After:  [0, 2, 1, 0]

Before: [3, 0, 0, 3]
8 3 0 2
After:  [3, 0, 1, 3]

Before: [2, 1, 2, 1]
2 1 2 1
After:  [2, 0, 2, 1]

Before: [1, 1, 1, 3]
6 3 2 1
After:  [1, 0, 1, 3]

Before: [0, 1, 2, 1]
5 3 2 2
After:  [0, 1, 1, 1]

Before: [3, 0, 0, 2]
7 3 0 1
After:  [3, 1, 0, 2]

Before: [2, 1, 0, 3]
4 1 0 2
After:  [2, 1, 0, 3]

Before: [0, 2, 1, 2]
1 2 2 3
After:  [0, 2, 1, 2]

Before: [2, 0, 1, 1]
1 2 2 1
After:  [2, 2, 1, 1]

Before: [1, 1, 2, 0]
2 1 2 0
After:  [0, 1, 2, 0]

Before: [0, 1, 2, 1]
11 3 3 1
After:  [0, 0, 2, 1]

Before: [2, 0, 1, 0]
12 2 1 0
After:  [1, 0, 1, 0]

Before: [2, 1, 0, 3]
10 1 3 3
After:  [2, 1, 0, 0]

Before: [2, 2, 2, 3]
10 1 3 0
After:  [0, 2, 2, 3]

Before: [0, 1, 2, 2]
9 0 0 1
After:  [0, 0, 2, 2]

Before: [1, 2, 2, 1]
14 0 2 0
After:  [0, 2, 2, 1]

Before: [3, 2, 0, 2]
7 3 0 0
After:  [1, 2, 0, 2]

Before: [3, 3, 0, 2]
7 3 1 3
After:  [3, 3, 0, 1]

Before: [1, 1, 2, 2]
2 1 2 2
After:  [1, 1, 0, 2]

Before: [3, 2, 3, 3]
6 3 3 2
After:  [3, 2, 1, 3]

Before: [1, 0, 3, 0]
3 3 2 0
After:  [1, 0, 3, 0]

Before: [2, 3, 0, 1]
11 3 3 3
After:  [2, 3, 0, 0]

Before: [1, 1, 1, 3]
6 3 2 0
After:  [0, 1, 1, 3]

Before: [2, 1, 3, 2]
4 1 0 0
After:  [0, 1, 3, 2]

Before: [0, 1, 1, 2]
11 3 3 2
After:  [0, 1, 0, 2]

Before: [1, 0, 1, 1]
12 3 1 1
After:  [1, 1, 1, 1]

Before: [2, 0, 0, 1]
12 3 1 3
After:  [2, 0, 0, 1]

Before: [3, 1, 3, 2]
15 3 2 2
After:  [3, 1, 2, 2]

Before: [2, 2, 3, 3]
15 0 2 2
After:  [2, 2, 2, 3]

Before: [0, 0, 2, 3]
6 2 2 2
After:  [0, 0, 1, 3]

Before: [3, 2, 2, 2]
11 3 3 1
After:  [3, 0, 2, 2]

Before: [2, 0, 3, 1]
15 0 2 0
After:  [2, 0, 3, 1]

Before: [3, 1, 3, 0]
3 3 2 1
After:  [3, 1, 3, 0]

Before: [2, 1, 2, 2]
4 1 0 3
After:  [2, 1, 2, 0]

Before: [2, 0, 3, 0]
3 3 2 3
After:  [2, 0, 3, 1]

Before: [1, 1, 0, 2]
3 2 3 0
After:  [1, 1, 0, 2]

Before: [0, 1, 0, 1]
9 0 0 1
After:  [0, 0, 0, 1]

Before: [3, 0, 1, 0]
12 2 1 3
After:  [3, 0, 1, 1]

Before: [2, 1, 0, 1]
11 3 3 1
After:  [2, 0, 0, 1]

Before: [3, 1, 2, 0]
2 1 2 0
After:  [0, 1, 2, 0]

Before: [2, 1, 2, 1]
5 3 2 1
After:  [2, 1, 2, 1]

Before: [0, 2, 2, 1]
9 0 0 0
After:  [0, 2, 2, 1]

Before: [3, 2, 3, 0]
3 3 2 3
After:  [3, 2, 3, 1]

Before: [0, 1, 3, 0]
13 1 2 0
After:  [0, 1, 3, 0]

Before: [3, 0, 3, 2]
11 3 3 1
After:  [3, 0, 3, 2]

Before: [1, 2, 2, 3]
10 1 3 0
After:  [0, 2, 2, 3]

Before: [2, 1, 3, 3]
13 1 2 1
After:  [2, 0, 3, 3]

Before: [1, 2, 2, 1]
5 3 2 1
After:  [1, 1, 2, 1]

Before: [0, 1, 2, 2]
11 3 3 0
After:  [0, 1, 2, 2]

Before: [0, 0, 0, 2]
3 2 3 1
After:  [0, 1, 0, 2]

Before: [1, 0, 2, 0]
14 0 2 0
After:  [0, 0, 2, 0]

Before: [2, 2, 1, 1]
11 3 3 3
After:  [2, 2, 1, 0]

Before: [0, 2, 1, 0]
0 0 2 0
After:  [0, 2, 1, 0]

Before: [2, 3, 3, 3]
6 3 3 0
After:  [1, 3, 3, 3]

Before: [1, 2, 3, 2]
15 3 2 3
After:  [1, 2, 3, 2]

Before: [2, 2, 2, 3]
10 1 3 1
After:  [2, 0, 2, 3]

Before: [3, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 1, 1, 3]
8 3 0 0
After:  [1, 1, 1, 3]

Before: [3, 2, 3, 1]
15 1 2 2
After:  [3, 2, 2, 1]

Before: [2, 1, 2, 3]
10 2 3 2
After:  [2, 1, 0, 3]

Before: [2, 3, 1, 0]
1 2 2 2
After:  [2, 3, 2, 0]

Before: [0, 1, 3, 2]
13 1 2 2
After:  [0, 1, 0, 2]

Before: [0, 2, 0, 1]
9 0 0 0
After:  [0, 2, 0, 1]

Before: [0, 1, 3, 1]
6 0 0 1
After:  [0, 1, 3, 1]

Before: [1, 3, 1, 2]
7 3 1 0
After:  [1, 3, 1, 2]

Before: [0, 3, 1, 3]
10 2 3 3
After:  [0, 3, 1, 0]

Before: [2, 0, 1, 0]
12 2 1 2
After:  [2, 0, 1, 0]

Before: [1, 1, 2, 1]
5 3 2 2
After:  [1, 1, 1, 1]

Before: [1, 3, 2, 0]
14 0 2 2
After:  [1, 3, 0, 0]

Before: [0, 1, 3, 3]
10 1 3 2
After:  [0, 1, 0, 3]

Before: [1, 0, 2, 1]
5 3 2 2
After:  [1, 0, 1, 1]

Before: [2, 1, 0, 0]
4 1 0 3
After:  [2, 1, 0, 0]

Before: [0, 0, 2, 2]
0 0 3 1
After:  [0, 0, 2, 2]

Before: [0, 1, 0, 0]
0 0 1 3
After:  [0, 1, 0, 0]

Before: [0, 2, 3, 2]
15 1 2 2
After:  [0, 2, 2, 2]

Before: [0, 2, 2, 1]
5 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 2, 2, 0]
9 0 0 0
After:  [0, 2, 2, 0]

Before: [3, 1, 3, 0]
13 1 2 2
After:  [3, 1, 0, 0]

Before: [0, 0, 3, 0]
3 3 2 0
After:  [1, 0, 3, 0]

Before: [0, 3, 2, 2]
6 0 0 0
After:  [1, 3, 2, 2]

Before: [3, 2, 3, 0]
15 1 2 0
After:  [2, 2, 3, 0]

Before: [3, 1, 3, 0]
3 3 2 0
After:  [1, 1, 3, 0]

Before: [2, 0, 2, 1]
12 3 1 0
After:  [1, 0, 2, 1]

Before: [0, 0, 0, 1]
0 0 2 1
After:  [0, 0, 0, 1]

Before: [0, 0, 3, 1]
12 3 1 3
After:  [0, 0, 3, 1]

Before: [3, 1, 3, 3]
8 3 2 0
After:  [1, 1, 3, 3]

Before: [2, 1, 0, 1]
11 3 3 2
After:  [2, 1, 0, 1]

Before: [0, 3, 1, 3]
9 0 0 0
After:  [0, 3, 1, 3]

Before: [1, 2, 1, 2]
1 2 2 0
After:  [2, 2, 1, 2]

Before: [0, 1, 2, 2]
2 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 2, 0, 3]
10 1 3 0
After:  [0, 2, 0, 3]

Before: [1, 2, 0, 2]
11 3 3 2
After:  [1, 2, 0, 2]

Before: [0, 1, 1, 1]
11 2 3 2
After:  [0, 1, 0, 1]

Before: [3, 1, 2, 3]
10 2 3 2
After:  [3, 1, 0, 3]

Before: [2, 1, 2, 1]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 1, 0]
9 0 0 2
After:  [0, 3, 0, 0]

Before: [2, 1, 3, 1]
4 1 0 0
After:  [0, 1, 3, 1]

Before: [1, 2, 3, 3]
15 1 2 0
After:  [2, 2, 3, 3]

Before: [0, 0, 2, 0]
9 0 0 3
After:  [0, 0, 2, 0]

Before: [2, 1, 3, 0]
4 1 0 2
After:  [2, 1, 0, 0]

Before: [0, 3, 1, 2]
7 3 1 2
After:  [0, 3, 1, 2]

Before: [0, 3, 0, 0]
0 0 3 3
After:  [0, 3, 0, 0]

Before: [3, 1, 2, 1]
2 1 2 3
After:  [3, 1, 2, 0]

Before: [2, 1, 1, 3]
4 1 0 3
After:  [2, 1, 1, 0]

Before: [2, 1, 2, 0]
8 2 0 3
After:  [2, 1, 2, 1]

Before: [0, 3, 2, 2]
6 0 0 2
After:  [0, 3, 1, 2]

Before: [1, 0, 1, 2]
1 2 2 3
After:  [1, 0, 1, 2]

Before: [3, 3, 3, 2]
7 3 1 1
After:  [3, 1, 3, 2]

Before: [2, 1, 2, 3]
2 1 2 1
After:  [2, 0, 2, 3]

Before: [1, 2, 3, 1]
11 3 3 3
After:  [1, 2, 3, 0]

Before: [1, 0, 2, 1]
11 3 3 1
After:  [1, 0, 2, 1]

Before: [0, 1, 3, 0]
9 0 0 1
After:  [0, 0, 3, 0]

Before: [3, 0, 2, 2]
7 3 0 3
After:  [3, 0, 2, 1]

Before: [2, 0, 3, 2]
15 3 2 0
After:  [2, 0, 3, 2]

Before: [3, 3, 3, 3]
8 3 0 1
After:  [3, 1, 3, 3]

Before: [1, 0, 2, 2]
14 0 2 0
After:  [0, 0, 2, 2]

Before: [2, 0, 2, 2]
11 3 3 2
After:  [2, 0, 0, 2]

Before: [2, 0, 3, 0]
15 0 2 2
After:  [2, 0, 2, 0]

Before: [2, 2, 3, 3]
8 3 2 2
After:  [2, 2, 1, 3]

Before: [1, 1, 2, 1]
14 0 2 2
After:  [1, 1, 0, 1]

Before: [2, 2, 3, 2]
15 0 2 3
After:  [2, 2, 3, 2]

Before: [2, 2, 2, 0]
8 2 1 0
After:  [1, 2, 2, 0]

Before: [3, 2, 0, 2]
7 3 0 3
After:  [3, 2, 0, 1]

Before: [0, 3, 1, 0]
0 0 1 0
After:  [0, 3, 1, 0]

Before: [3, 0, 0, 2]
7 3 0 0
After:  [1, 0, 0, 2]

Before: [3, 3, 0, 2]
3 2 3 2
After:  [3, 3, 1, 2]

Before: [2, 0, 2, 0]
8 2 0 2
After:  [2, 0, 1, 0]

Before: [2, 1, 0, 0]
4 1 0 2
After:  [2, 1, 0, 0]

Before: [1, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [2, 1, 3, 2]
15 3 2 1
After:  [2, 2, 3, 2]

Before: [3, 2, 0, 2]
7 3 0 2
After:  [3, 2, 1, 2]

Before: [1, 2, 2, 2]
14 0 2 2
After:  [1, 2, 0, 2]

Before: [2, 1, 3, 1]
13 1 2 0
After:  [0, 1, 3, 1]

Before: [1, 3, 3, 2]
7 3 1 3
After:  [1, 3, 3, 1]

Before: [1, 0, 0, 2]
12 0 1 2
After:  [1, 0, 1, 2]

Before: [0, 0, 3, 3]
6 3 3 2
After:  [0, 0, 1, 3]

Before: [3, 1, 3, 2]
13 1 2 0
After:  [0, 1, 3, 2]

Before: [1, 3, 2, 2]
14 0 2 3
After:  [1, 3, 2, 0]

Before: [2, 2, 3, 0]
3 3 2 2
After:  [2, 2, 1, 0]

Before: [3, 1, 3, 0]
13 1 2 1
After:  [3, 0, 3, 0]

Before: [2, 1, 1, 2]
4 1 0 0
After:  [0, 1, 1, 2]

Before: [0, 1, 3, 0]
13 1 2 3
After:  [0, 1, 3, 0]

Before: [0, 2, 3, 3]
8 3 2 3
After:  [0, 2, 3, 1]

Before: [0, 2, 2, 1]
5 3 2 3
After:  [0, 2, 2, 1]

Before: [0, 2, 2, 3]
10 1 3 3
After:  [0, 2, 2, 0]

Before: [1, 1, 2, 1]
14 0 2 0
After:  [0, 1, 2, 1]

Before: [2, 1, 3, 1]
13 1 2 2
After:  [2, 1, 0, 1]

Before: [0, 3, 3, 0]
0 0 2 2
After:  [0, 3, 0, 0]

Before: [2, 3, 1, 1]
1 2 2 0
After:  [2, 3, 1, 1]

Before: [2, 1, 2, 3]
4 1 0 3
After:  [2, 1, 2, 0]

Before: [2, 2, 2, 2]
8 2 0 0
After:  [1, 2, 2, 2]

Before: [1, 0, 0, 1]
12 0 1 0
After:  [1, 0, 0, 1]

Before: [2, 1, 3, 2]
13 1 2 2
After:  [2, 1, 0, 2]

Before: [0, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [2, 2, 1, 1]
1 2 2 0
After:  [2, 2, 1, 1]

Before: [3, 3, 1, 2]
7 3 1 1
After:  [3, 1, 1, 2]

Before: [3, 3, 1, 2]
1 2 2 3
After:  [3, 3, 1, 2]

Before: [0, 0, 2, 0]
0 0 3 3
After:  [0, 0, 2, 0]

Before: [1, 1, 3, 1]
11 3 3 2
After:  [1, 1, 0, 1]

Before: [3, 0, 3, 0]
3 3 2 0
After:  [1, 0, 3, 0]

Before: [2, 2, 3, 0]
3 3 2 3
After:  [2, 2, 3, 1]

Before: [0, 1, 0, 2]
3 2 3 1
After:  [0, 1, 0, 2]

Before: [3, 1, 2, 3]
2 1 2 0
After:  [0, 1, 2, 3]

Before: [0, 1, 3, 3]
8 3 2 1
After:  [0, 1, 3, 3]

Before: [0, 0, 3, 0]
3 3 2 1
After:  [0, 1, 3, 0]

Before: [3, 0, 3, 1]
12 3 1 2
After:  [3, 0, 1, 1]

Before: [3, 1, 3, 2]
13 1 2 3
After:  [3, 1, 3, 0]

Before: [2, 1, 2, 0]
4 1 0 0
After:  [0, 1, 2, 0]

Before: [3, 3, 3, 2]
15 3 2 2
After:  [3, 3, 2, 2]

Before: [3, 0, 3, 2]
7 3 0 0
After:  [1, 0, 3, 2]

Before: [3, 0, 2, 1]
5 3 2 3
After:  [3, 0, 2, 1]

Before: [2, 2, 3, 2]
15 0 2 1
After:  [2, 2, 3, 2]

Before: [0, 2, 2, 2]
9 0 0 3
After:  [0, 2, 2, 0]

Before: [3, 1, 3, 3]
8 3 2 3
After:  [3, 1, 3, 1]

Before: [0, 0, 1, 3]
12 2 1 1
After:  [0, 1, 1, 3]

Before: [1, 0, 1, 3]
12 2 1 2
After:  [1, 0, 1, 3]

Before: [2, 1, 2, 2]
2 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 1, 3, 1]
4 1 0 3
After:  [2, 1, 3, 0]

Before: [3, 1, 2, 3]
2 1 2 2
After:  [3, 1, 0, 3]

Before: [1, 1, 3, 3]
13 1 2 3
After:  [1, 1, 3, 0]

Before: [2, 2, 3, 1]
15 1 2 3
After:  [2, 2, 3, 2]

Before: [3, 1, 2, 2]
11 3 3 0
After:  [0, 1, 2, 2]

Before: [3, 1, 3, 3]
8 3 2 2
After:  [3, 1, 1, 3]

Before: [0, 3, 3, 3]
0 0 3 3
After:  [0, 3, 3, 0]

Before: [0, 1, 2, 3]
2 1 2 1
After:  [0, 0, 2, 3]

Before: [0, 1, 3, 3]
13 1 2 2
After:  [0, 1, 0, 3]

Before: [3, 2, 3, 1]
11 3 3 2
After:  [3, 2, 0, 1]

Before: [0, 2, 3, 3]
8 3 2 2
After:  [0, 2, 1, 3]

Before: [3, 1, 3, 0]
3 3 2 2
After:  [3, 1, 1, 0]

Before: [3, 0, 0, 2]
7 3 0 3
After:  [3, 0, 0, 1]

Before: [0, 1, 3, 3]
9 0 0 1
After:  [0, 0, 3, 3]

Before: [2, 1, 2, 1]
4 1 0 2
After:  [2, 1, 0, 1]

Before: [2, 1, 3, 2]
4 1 0 2
After:  [2, 1, 0, 2]

Before: [0, 3, 3, 3]
8 3 2 3
After:  [0, 3, 3, 1]

Before: [1, 2, 0, 3]
10 1 3 2
After:  [1, 2, 0, 3]

Before: [1, 2, 2, 2]
14 0 2 0
After:  [0, 2, 2, 2]

Before: [0, 3, 2, 2]
7 3 1 3
After:  [0, 3, 2, 1]

Before: [1, 1, 2, 1]
5 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 2, 1, 1]
11 3 3 0
After:  [0, 2, 1, 1]

Before: [2, 1, 0, 1]
4 1 0 0
After:  [0, 1, 0, 1]

Before: [3, 2, 2, 3]
8 2 1 3
After:  [3, 2, 2, 1]

Before: [3, 1, 2, 2]
7 3 0 3
After:  [3, 1, 2, 1]

Before: [2, 1, 1, 3]
1 2 2 1
After:  [2, 2, 1, 3]

Before: [0, 0, 2, 0]
0 0 1 2
After:  [0, 0, 0, 0]

Before: [0, 3, 0, 1]
0 0 3 2
After:  [0, 3, 0, 1]

Before: [0, 2, 1, 3]
0 0 3 1
After:  [0, 0, 1, 3]

Before: [1, 3, 3, 0]
3 3 2 3
After:  [1, 3, 3, 1]

Before: [0, 0, 3, 1]
9 0 0 2
After:  [0, 0, 0, 1]

Before: [0, 0, 2, 1]
12 3 1 1
After:  [0, 1, 2, 1]

Before: [0, 1, 2, 2]
9 0 0 2
After:  [0, 1, 0, 2]

Before: [2, 0, 3, 2]
15 0 2 0
After:  [2, 0, 3, 2]

Before: [0, 1, 2, 1]
0 0 1 3
After:  [0, 1, 2, 0]

Before: [1, 2, 2, 0]
14 0 2 2
After:  [1, 2, 0, 0]

Before: [0, 2, 0, 3]
9 0 0 2
After:  [0, 2, 0, 3]

Before: [1, 2, 2, 3]
6 3 1 1
After:  [1, 0, 2, 3]

Before: [1, 0, 2, 0]
6 2 2 1
After:  [1, 1, 2, 0]

Before: [0, 0, 2, 1]
5 3 2 1
After:  [0, 1, 2, 1]

Before: [0, 3, 0, 1]
0 0 2 1
After:  [0, 0, 0, 1]

Before: [3, 3, 2, 1]
6 2 2 1
After:  [3, 1, 2, 1]

Before: [1, 0, 3, 0]
3 3 2 2
After:  [1, 0, 1, 0]

Before: [1, 2, 2, 0]
14 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 2, 2, 2]
7 3 0 0
After:  [1, 2, 2, 2]

Before: [0, 1, 3, 0]
13 1 2 2
After:  [0, 1, 0, 0]

Before: [1, 1, 3, 1]
8 2 3 2
After:  [1, 1, 0, 1]

Before: [2, 1, 1, 1]
4 1 0 3
After:  [2, 1, 1, 0]

Before: [0, 1, 2, 1]
5 3 2 3
After:  [0, 1, 2, 1]

Before: [0, 1, 0, 3]
6 3 3 0
After:  [1, 1, 0, 3]

Before: [0, 0, 3, 1]
12 3 1 0
After:  [1, 0, 3, 1]

Before: [0, 3, 0, 2]
9 0 0 1
After:  [0, 0, 0, 2]

Before: [2, 2, 2, 1]
5 3 2 1
After:  [2, 1, 2, 1]

Before: [2, 3, 3, 1]
15 0 2 1
After:  [2, 2, 3, 1]

Before: [2, 2, 2, 2]
8 2 0 3
After:  [2, 2, 2, 1]

Before: [1, 2, 3, 1]
8 2 3 2
After:  [1, 2, 0, 1]

Before: [0, 1, 3, 0]
9 0 0 3
After:  [0, 1, 3, 0]

Before: [1, 2, 3, 2]
15 3 2 1
After:  [1, 2, 3, 2]

Before: [1, 1, 2, 0]
2 1 2 2
After:  [1, 1, 0, 0]

Before: [3, 1, 1, 3]
10 1 3 1
After:  [3, 0, 1, 3]

Before: [3, 3, 2, 3]
10 2 3 3
After:  [3, 3, 2, 0]

Before: [2, 1, 3, 3]
4 1 0 2
After:  [2, 1, 0, 3]

Before: [0, 1, 0, 2]
0 0 1 2
After:  [0, 1, 0, 2]

Before: [2, 1, 1, 0]
4 1 0 3
After:  [2, 1, 1, 0]

Before: [3, 2, 1, 0]
1 2 2 1
After:  [3, 2, 1, 0]

Before: [2, 1, 0, 2]
4 1 0 1
After:  [2, 0, 0, 2]

Before: [0, 0, 3, 3]
0 0 3 3
After:  [0, 0, 3, 0]

Before: [3, 1, 3, 2]
6 2 1 0
After:  [0, 1, 3, 2]

Before: [3, 3, 1, 2]
7 3 0 0
After:  [1, 3, 1, 2]

Before: [1, 1, 3, 2]
13 1 2 3
After:  [1, 1, 3, 0]'''

data = data.split('\n\n')
for i in range(len(data)):
	bloc = data[i].replace('Before: ', '').replace('After: ', '').split('\n')
	bloc = [eval(bloc[0]), eval('['+bloc[1].replace(' ',',')+']'), eval(bloc[2])]
	data[i] = bloc

import copy

registers = [0, 0, 0, 0]

def addr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] + r[b]
	return r
	
def addi(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] + b
	return r
	
def mulr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] * r[b]
	return r
	
def muli(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] * b
	return r

def banr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] & r[b]
	return r
	
def bani(a, b, c, registers):
	r = copy.deepcopy(registers)	
	r[c] = r[a] & b
	return r

def borr(a, b, c, registers):
	r = copy.deepcopy(registers)	
	r[c] = r[a] | r[b]
	return r
	
def bori(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] | b
	return r

def setr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a]
	return r

def seti(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = a
	return r
	
def gtir(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = a > r[b]
	return r
	
def gtri(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] > b
	return r

def gtrr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] > r[b]
	return r

def gtir(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = a == r[b]
	return r
	
def gtri(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] == b
	return r

def gtrr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] == r[b]
	return r
	
functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, gtir, gtri, gtrr]

opcodes = []

count = 0
for i in range(len(data)):
	possible = 0
	for f in functions:
		'''print(f)
		print("input", data[i][1][1], data[i][1][2], data[i][1][3])
		print("output", f(data[i][1][1], data[i][1][2], data[i][1][3], data[i][0]))
		print("theori", data[i][2])
		print()'''
		if data[i][2] == f(data[i][1][1], data[i][1][2], data[i][1][3], data[i][0]):
			possible += 1
	if possible >= 3:
		count += 1
print(count)
