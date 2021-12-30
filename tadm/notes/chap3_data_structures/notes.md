关于本章的一些思考，看的时候想重点看看tree，skiena的书在这块比较简陋，遂看sedgewick，虽然每个细节点非常清晰，但过于细密，容易绕进去，最终从网上找了一些参考



#### 1. 2-3 tree

本部分看的sedgewick，事实上可以看普渡大学的cs251- [(2,4) TREES](https://www.cs.purdue.edu/homes/ayg/CS251/slides/chap13a.pdf)

2-3 tree是red-black 树的基础



#### 2. red-black tree

A **red-black tree** is a binary search tree in which

- each node has a color (red or black) associated with it (in addition to its key and left and right children)
- the following 3 properties hold:
  1. (**root property**) The root of the red-black tree is black
  2. (**red property**) The children of a red node are black.
  3. (**black property**) For each node with at least one null child, the number of black nodes on the path from the root to the null child is the same.

[Red-Black Trees](http://pages.cs.wisc.edu/~cs400/readings/Red-Black-Trees/)



#### 3. 2-3 tree <-> red-black tree

[Mapping 2-3-4 Trees into Red-Black Trees](https://azrael.digipen.edu/~mmead/www/Courses/CS280/Trees-Mapping2-3-4IntoRB.html)

![](https://user-images.githubusercontent.com/2216435/147741062-88fccfae-f17a-4000-98ea-72f32ba65080.png)

[2-3-4 Trees and RedBlack Trees](https://www.cs.purdue.edu/homes/ayg/CS251/slides/chap13b.pdf)



#### 4. 插入过程

[visualization](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

[Datastructure](http://www.btechsmartclass.com/data_structures/red-black-trees.html)

