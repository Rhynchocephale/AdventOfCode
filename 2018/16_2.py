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

data2 = '''14 3 3 2
14 3 3 0
14 2 2 1
13 0 2 1
4 1 2 1
1 3 1 3
14 2 3 1
14 2 0 0
6 0 2 0
4 0 3 0
1 0 3 3
14 2 3 0
6 0 2 2
4 2 2 2
1 3 2 3
5 3 0 0
14 3 2 1
4 2 0 2
9 2 1 2
4 1 0 3
9 3 2 3
13 1 2 1
4 1 3 1
1 1 0 0
5 0 1 2
14 0 0 3
14 2 1 0
4 0 0 1
9 1 3 1
2 1 0 1
4 1 2 1
1 1 2 2
5 2 3 3
14 3 1 1
14 1 0 0
14 3 1 2
9 0 1 1
4 1 3 1
4 1 3 1
1 3 1 3
5 3 1 0
14 2 0 1
14 0 2 3
15 1 3 2
4 2 3 2
1 2 0 0
5 0 0 1
14 1 1 2
14 2 1 3
14 2 2 0
8 0 3 2
4 2 3 2
1 1 2 1
14 3 3 0
14 0 2 2
14 3 1 3
14 2 3 0
4 0 1 0
1 0 1 1
5 1 3 3
14 2 0 1
14 3 1 2
14 1 0 0
12 1 2 1
4 1 1 1
1 1 3 3
5 3 3 0
4 1 0 1
9 1 0 1
14 0 0 2
14 2 1 3
3 2 3 3
4 3 3 3
1 3 0 0
5 0 2 3
4 0 0 2
9 2 3 2
4 1 0 0
9 0 1 0
14 3 3 1
13 1 2 0
4 0 3 0
1 3 0 3
5 3 1 0
14 3 3 3
13 3 2 3
4 3 2 3
4 3 2 3
1 3 0 0
5 0 2 2
14 2 3 0
14 2 3 3
7 0 1 3
4 3 2 3
1 3 2 2
5 2 1 1
14 1 0 3
14 2 2 2
1 3 3 3
4 3 2 3
1 1 3 1
5 1 2 2
4 1 0 1
9 1 0 1
14 3 0 3
14 1 3 3
4 3 1 3
1 2 3 2
14 3 1 1
4 3 0 0
9 0 3 0
14 1 0 3
9 3 1 3
4 3 1 3
1 3 2 2
5 2 0 1
4 1 0 2
9 2 1 2
14 2 3 3
4 3 0 0
9 0 2 0
8 0 3 0
4 0 2 0
4 0 3 0
1 1 0 1
14 1 0 0
14 0 2 3
14 2 3 2
5 0 2 3
4 3 1 3
1 1 3 1
5 1 2 0
4 2 0 1
9 1 1 1
14 2 0 3
15 2 3 2
4 2 1 2
4 2 2 2
1 0 2 0
5 0 1 2
4 0 0 3
9 3 1 3
14 0 1 0
14 3 0 0
4 0 2 0
1 2 0 2
5 2 0 0
14 2 0 2
4 0 0 1
9 1 3 1
7 2 1 3
4 3 3 3
1 3 0 0
14 1 1 3
9 3 1 3
4 3 3 3
1 3 0 0
5 0 2 3
14 1 1 0
7 2 1 0
4 0 1 0
4 0 2 0
1 0 3 3
5 3 1 1
4 1 0 3
9 3 3 3
4 0 0 0
9 0 2 0
4 3 0 2
9 2 3 2
14 2 3 2
4 2 1 2
1 1 2 1
5 1 0 3
14 0 0 2
14 3 0 0
14 0 1 1
6 2 0 0
4 0 1 0
1 0 3 3
5 3 1 2
14 1 3 1
14 2 0 3
4 2 0 0
9 0 3 0
0 1 3 1
4 1 2 1
1 2 1 2
5 2 3 0
14 3 3 2
14 1 3 3
14 1 3 1
1 1 3 3
4 3 2 3
1 0 3 0
5 0 0 1
14 3 2 3
14 3 0 0
13 3 2 3
4 3 2 3
1 1 3 1
5 1 0 3
14 2 0 2
14 1 1 0
14 1 3 1
5 0 2 1
4 1 2 1
1 3 1 3
5 3 3 1
14 3 0 2
14 1 3 3
14 3 0 0
1 3 3 2
4 2 1 2
4 2 1 2
1 2 1 1
14 3 2 2
14 2 1 0
6 0 2 0
4 0 1 0
1 1 0 1
14 1 3 0
14 1 1 2
14 3 2 3
14 2 3 3
4 3 2 3
1 3 1 1
5 1 1 2
4 2 0 0
9 0 2 0
4 3 0 1
9 1 1 1
14 0 2 3
15 0 3 3
4 3 1 3
1 3 2 2
5 2 1 1
14 0 1 2
4 2 0 3
9 3 1 3
11 0 3 3
4 3 1 3
1 3 1 1
14 0 2 3
14 2 0 2
15 0 3 0
4 0 3 0
1 0 1 1
5 1 3 2
14 2 1 3
4 0 0 1
9 1 3 1
14 2 0 0
8 0 3 0
4 0 3 0
1 0 2 2
5 2 1 3
14 3 2 0
14 0 3 2
14 0 3 1
6 2 0 2
4 2 1 2
1 3 2 3
5 3 3 0
4 0 0 2
9 2 2 2
4 2 0 3
9 3 3 3
14 1 2 2
4 2 1 2
1 0 2 0
14 1 2 2
14 1 0 3
14 3 1 1
1 3 3 1
4 1 2 1
1 0 1 0
5 0 3 2
14 1 0 0
14 0 3 1
1 0 0 3
4 3 2 3
1 3 2 2
5 2 0 1
14 2 3 2
14 1 3 3
5 0 2 2
4 2 3 2
1 2 1 1
5 1 0 2
14 2 1 0
14 0 3 1
9 3 1 3
4 3 1 3
4 3 1 3
1 3 2 2
5 2 2 3
14 2 3 1
14 3 0 2
14 3 1 0
2 0 1 2
4 2 1 2
1 2 3 3
5 3 3 2
14 1 2 1
14 2 2 0
14 1 2 3
11 0 3 3
4 3 2 3
1 3 2 2
5 2 3 1
14 1 1 0
14 2 2 2
14 2 2 3
5 0 2 0
4 0 3 0
4 0 2 0
1 1 0 1
14 3 1 3
14 3 2 0
7 2 0 2
4 2 2 2
1 2 1 1
5 1 3 2
14 2 2 0
14 1 1 3
14 2 2 1
11 0 3 1
4 1 1 1
1 1 2 2
5 2 1 3
14 1 2 1
4 0 0 0
9 0 1 0
14 2 1 2
5 0 2 0
4 0 2 0
1 0 3 3
5 3 1 1
4 1 0 0
9 0 1 0
14 2 3 3
4 0 0 2
9 2 1 2
0 0 3 0
4 0 1 0
4 0 2 0
1 1 0 1
14 0 2 0
14 2 0 2
14 3 2 2
4 2 1 2
1 2 1 1
5 1 3 2
14 1 0 1
14 2 2 0
15 0 3 0
4 0 1 0
1 0 2 2
5 2 3 3
4 3 0 1
9 1 3 1
14 2 0 2
4 1 0 0
9 0 0 0
7 2 1 0
4 0 2 0
1 3 0 3
5 3 1 0
4 2 0 2
9 2 3 2
14 0 0 3
14 1 0 1
3 3 2 3
4 3 2 3
1 0 3 0
14 3 2 1
14 1 0 2
14 1 0 3
1 3 3 2
4 2 2 2
4 2 2 2
1 0 2 0
5 0 2 3
4 0 0 0
9 0 1 0
14 2 2 1
14 3 3 2
12 1 2 2
4 2 2 2
1 2 3 3
5 3 1 2
14 2 1 3
14 1 0 1
0 1 3 1
4 1 1 1
1 1 2 2
5 2 0 1
14 2 1 2
14 0 3 3
14 3 0 0
10 3 2 0
4 0 3 0
1 1 0 1
5 1 3 0
4 2 0 2
9 2 3 2
4 1 0 1
9 1 3 1
3 3 2 2
4 2 2 2
4 2 3 2
1 0 2 0
5 0 3 3
14 1 0 1
4 0 0 0
9 0 0 0
14 3 3 2
4 1 2 0
4 0 3 0
1 0 3 3
4 0 0 1
9 1 2 1
14 1 0 0
14 2 1 2
5 0 2 0
4 0 1 0
1 3 0 3
5 3 1 0
14 1 3 3
14 3 1 1
7 2 1 1
4 1 2 1
4 1 3 1
1 0 1 0
5 0 3 3
14 3 0 0
14 1 1 1
4 2 0 2
9 2 3 2
13 0 2 1
4 1 2 1
4 1 1 1
1 1 3 3
5 3 3 2
14 1 1 1
14 1 1 3
14 1 2 0
14 3 1 0
4 0 2 0
1 2 0 2
14 0 3 1
14 2 1 0
4 2 0 3
9 3 2 3
8 0 3 1
4 1 1 1
1 1 2 2
5 2 1 1
14 1 3 3
14 3 0 2
14 3 2 0
4 3 2 0
4 0 2 0
1 1 0 1
14 2 1 2
4 1 0 0
9 0 0 0
14 0 2 3
15 2 3 2
4 2 1 2
4 2 3 2
1 2 1 1
5 1 1 0
14 3 1 1
14 2 3 2
10 3 2 2
4 2 3 2
1 0 2 0
5 0 0 2
4 2 0 0
9 0 2 0
15 0 3 1
4 1 3 1
4 1 1 1
1 2 1 2
5 2 2 3
14 1 2 0
14 2 3 2
14 0 0 1
5 0 2 1
4 1 1 1
4 1 2 1
1 3 1 3
5 3 0 1
14 1 2 3
5 0 2 3
4 3 2 3
1 1 3 1
14 3 0 2
14 2 1 0
14 0 0 3
6 0 2 0
4 0 3 0
1 0 1 1
14 3 2 0
14 2 3 3
14 1 2 2
13 0 2 0
4 0 3 0
1 1 0 1
5 1 3 3
14 2 2 1
14 3 1 0
12 1 0 2
4 2 2 2
1 3 2 3
5 3 2 1
4 1 0 2
9 2 1 2
4 1 0 3
9 3 1 3
14 1 3 0
1 0 3 0
4 0 1 0
1 1 0 1
5 1 1 3
14 3 1 2
14 2 1 0
14 0 3 1
6 0 2 0
4 0 1 0
1 3 0 3
5 3 0 1
14 2 1 0
14 3 3 3
6 0 2 0
4 0 1 0
1 1 0 1
5 1 2 0
4 0 0 1
9 1 1 1
14 2 1 2
14 2 1 3
15 2 3 1
4 1 3 1
1 1 0 0
5 0 1 2
14 1 3 1
14 2 1 0
14 1 0 3
11 0 3 1
4 1 3 1
4 1 1 1
1 2 1 2
5 2 0 0
14 2 0 2
14 2 1 1
14 0 0 3
15 1 3 3
4 3 3 3
1 3 0 0
5 0 1 1
4 1 0 0
9 0 3 0
14 2 1 3
14 0 1 2
13 0 2 0
4 0 1 0
1 1 0 1
5 1 3 0
14 2 0 2
14 2 2 1
4 0 0 3
9 3 0 3
14 3 2 2
4 2 1 2
1 0 2 0
5 0 3 1
14 2 1 3
14 2 2 0
4 0 0 2
9 2 0 2
8 0 3 3
4 3 1 3
1 3 1 1
14 2 2 2
4 2 0 3
9 3 2 3
14 1 0 0
1 0 0 0
4 0 3 0
1 1 0 1
5 1 0 0
14 1 0 2
4 1 0 1
9 1 0 1
4 3 0 3
9 3 0 3
14 3 2 1
4 1 3 1
1 0 1 0
5 0 1 3
14 0 2 2
14 3 0 1
14 3 2 0
6 2 0 2
4 2 2 2
1 3 2 3
5 3 3 1
14 1 3 3
14 0 2 2
6 2 0 2
4 2 3 2
1 2 1 1
5 1 1 2
14 1 0 0
4 1 0 3
9 3 0 3
14 0 1 1
9 0 1 3
4 3 2 3
4 3 1 3
1 2 3 2
14 2 3 3
14 2 2 1
14 2 1 0
8 0 3 1
4 1 2 1
1 1 2 2
14 2 3 1
14 1 1 0
0 0 3 1
4 1 2 1
1 1 2 2
5 2 0 1
14 1 1 3
14 2 3 0
14 0 0 2
11 0 3 2
4 2 2 2
4 2 1 2
1 1 2 1
5 1 3 3
4 3 0 2
9 2 2 2
14 2 3 1
14 3 2 0
12 1 0 1
4 1 3 1
1 3 1 3
14 3 0 2
4 2 0 1
9 1 1 1
14 2 3 0
0 1 0 2
4 2 3 2
1 3 2 3
14 3 1 0
14 2 3 1
14 1 2 2
13 0 2 2
4 2 3 2
1 3 2 3
5 3 1 1
14 1 3 3
4 3 0 0
9 0 2 0
14 1 3 2
11 0 3 0
4 0 2 0
1 0 1 1
5 1 2 2
14 0 1 3
14 2 2 0
14 1 3 1
0 1 0 0
4 0 1 0
1 0 2 2
14 1 2 3
14 2 1 0
0 1 0 0
4 0 2 0
1 2 0 2
4 1 0 1
9 1 3 1
14 1 0 0
1 3 3 0
4 0 3 0
1 2 0 2
5 2 3 1
4 2 0 3
9 3 2 3
14 1 3 0
4 1 0 2
9 2 2 2
5 0 2 3
4 3 3 3
4 3 2 3
1 1 3 1
4 0 0 0
9 0 3 0
14 0 1 3
7 2 0 3
4 3 2 3
1 1 3 1
5 1 1 3
14 1 1 1
7 2 0 2
4 2 2 2
1 3 2 3
14 2 0 0
4 0 0 2
9 2 3 2
14 2 1 1
12 1 2 2
4 2 2 2
1 3 2 3
5 3 1 2
14 1 1 0
14 1 2 1
14 1 1 3
1 1 0 1
4 1 1 1
1 2 1 2
5 2 3 1
14 3 3 0
14 0 1 2
14 3 3 3
6 2 0 0
4 0 3 0
1 1 0 1
5 1 0 0
14 3 0 1
4 3 0 2
9 2 2 2
4 1 0 3
9 3 0 3
10 3 2 3
4 3 2 3
1 0 3 0
5 0 1 1
4 2 0 3
9 3 3 3
4 0 0 0
9 0 1 0
5 0 2 2
4 2 2 2
4 2 1 2
1 2 1 1
5 1 0 3
14 2 0 2
4 1 0 1
9 1 0 1
9 0 1 1
4 1 1 1
1 1 3 3
5 3 1 0
14 0 0 3
14 1 0 1
10 3 2 2
4 2 2 2
4 2 3 2
1 0 2 0
5 0 0 1
14 2 2 0
14 0 1 2
14 2 3 3
8 0 3 0
4 0 1 0
4 0 1 0
1 0 1 1
4 2 0 2
9 2 2 2
4 2 0 0
9 0 1 0
5 0 2 2
4 2 3 2
1 1 2 1
5 1 0 3
4 1 0 1
9 1 3 1
14 2 2 2
14 0 1 0
7 2 1 2
4 2 1 2
1 2 3 3
5 3 3 1
4 2 0 0
9 0 2 0
14 3 2 2
14 2 1 3
8 0 3 2
4 2 2 2
4 2 3 2
1 2 1 1
5 1 0 0
14 0 2 3
4 2 0 1
9 1 2 1
14 1 3 2
14 3 2 3
4 3 2 3
4 3 1 3
1 0 3 0
14 3 2 3
4 0 0 1
9 1 3 1
14 2 2 2
7 2 1 1
4 1 1 1
1 0 1 0
5 0 3 3
14 1 0 0
14 2 0 1
5 0 2 2
4 2 3 2
1 3 2 3
5 3 0 0
14 0 0 1
14 2 3 2
14 2 3 3
15 2 3 2
4 2 3 2
1 2 0 0
5 0 2 2
14 2 2 1
14 0 0 0
14 3 3 3
2 3 1 1
4 1 1 1
4 1 3 1
1 2 1 2
5 2 2 3
4 0 0 0
9 0 1 0
14 0 0 2
4 1 0 1
9 1 1 1
1 1 0 2
4 2 3 2
1 3 2 3
5 3 2 1
14 3 2 3
14 3 1 2
4 0 2 0
4 0 3 0
1 0 1 1
5 1 3 2
14 3 3 0
14 3 2 1
4 3 0 3
9 3 1 3
1 3 3 1
4 1 3 1
1 2 1 2
5 2 2 0
4 3 0 3
9 3 0 3
14 2 1 2
14 0 3 1
15 2 3 3
4 3 2 3
1 0 3 0
5 0 1 1
14 2 3 0
14 1 3 2
14 2 3 3
8 0 3 3
4 3 3 3
1 1 3 1
5 1 1 3
14 2 3 2
14 2 1 1
14 3 3 0
2 0 1 0
4 0 1 0
1 3 0 3
5 3 2 1
14 1 0 0
14 2 0 3
14 0 1 2
3 2 3 3
4 3 2 3
1 3 1 1
4 1 0 3
9 3 3 3
14 1 0 2
4 2 0 0
9 0 2 0
13 3 2 3
4 3 3 3
1 1 3 1
5 1 0 3
14 3 0 0
14 1 1 1
14 0 2 2
13 0 2 0
4 0 1 0
1 3 0 3
14 1 2 0
4 1 2 1
4 1 2 1
4 1 1 1
1 1 3 3
5 3 3 1
14 3 2 0
14 2 1 3
2 0 3 3
4 3 1 3
4 3 3 3
1 3 1 1
14 3 1 2
14 2 2 0
14 1 0 3
11 0 3 2
4 2 2 2
1 2 1 1
5 1 0 2
14 2 0 1
14 1 3 0
14 2 0 3
0 0 3 3
4 3 2 3
4 3 2 3
1 2 3 2
14 2 3 0
14 1 1 3
14 0 3 1
11 0 3 1
4 1 3 1
1 1 2 2
4 1 0 1
9 1 0 1
4 0 0 3
9 3 3 3
2 3 0 0
4 0 3 0
1 2 0 2
5 2 2 3
14 0 2 2
14 3 0 1
14 2 3 0
7 0 1 1
4 1 3 1
1 3 1 3
5 3 2 0'''

data = data.split('\n\n')
for i in range(len(data)):
	bloc = data[i].replace('Before: ', '').replace('After: ', '').split('\n')
	bloc = [eval(bloc[0]), eval('['+bloc[1].replace(' ',',')+']'), eval(bloc[2])]
	data[i] = bloc
	
data2 = data2.split('\n')
for i in range(len(data2)):
	data2[i] = [int(x) for x in data2[i].split()]
	
import copy

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

def etir(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = a == r[b]
	return r
	
def etri(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] == b
	return r

def etrr(a, b, c, registers):
	r = copy.deepcopy(registers)
	r[c] = r[a] == r[b]
	return r
	
functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, etir, etri, etrr]

opcodes = []
for _ in range(16):
	opcodes.append([x for x in functions])

count = 0
for i in range(len(data)):
	possible = []
	for f in functions:
		if data[i][2] == f(data[i][1][1], data[i][1][2], data[i][1][3], data[i][0]):
			possible.append(f)
		else:
			try:
				opcodes[data[i][1][0]].remove(f)
			except ValueError:
				pass
	if len(possible) >= 3:
		count += 1

finalOpcodes = []

while len(finalOpcodes) < 16:
	for x in range(len(opcodes)):
		if len(opcodes[x]) == 1:
			toRemove = opcodes[x][0]
			finalOpcodes.append([x, toRemove])
			for y in range(len(opcodes)):
				try:
					opcodes[y].remove(toRemove)
				except ValueError:
					pass

finalOpcodes = sorted(finalOpcodes)
finalOpcodes = [x[1] for x in finalOpcodes]

registers = [0, 0, 0, 0]

for line in data2:
	registers = finalOpcodes[line[0]](line[1], line[2], line[3], registers)
print(registers)
