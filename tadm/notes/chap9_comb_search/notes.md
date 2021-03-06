#### 1. simple example of backtracking

[Recursion and Backtracking](https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/)

```
is_attacked( x, y, board[][], N)
    //checking for row and column
    if any cell in xth row is 1
        return true
    if any cell in yth column is 1
        return true

    //checking for diagonals
    if any cell (p, q) having p+q = x+y is 1          
        return true
    if any cell (p, q) having p-q = x-y is 1
        return true
    return false


N-Queens( board[][], N )
    if N is 0                     //All queens have been placed
        return true
    for i = 1 to N {
        for j = 1 to N {
            if is_attacked(i, j, board, N) is true
                skip it and move to next cell
            board[i][j] = 1            //Place current queen at cell (i,j)
            if N-Queens( board, N-1) is true    // Solve subproblem
                return true                   // if solution is found return true
            board[i][j] = 0            /* if solution is not found undo whatever changes 
                                       were made i.e., remove  current queen from (i,j)*/
        }
    }
    return false
```

![image](https://user-images.githubusercontent.com/2216435/150488071-acbdfbe1-d1af-4447-bdf4-7bb44db42c4b.png)

![](https://user-images.githubusercontent.com/2216435/150488692-68c5fc9e-53c1-4b48-b9c6-eee945676e68.png)



![](https://user-images.githubusercontent.com/2216435/151654511-7d64fdaf-5983-45b0-8ff4-2a5c6b02a942.png)

