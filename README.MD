<!--
Location: SF
-->

![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)


# Merge Sort


### Why is this important?
<!-- framing the "why" in big-picture/real world examples -->
*This workshop is important because:*

Merge sort is the first fast, powerful sorting algorithm that you will encounter in the wilds of the real world (it's baked into Safari and Firefox!).  It uses an extremely efficient application of the 'Divide and Conquer' concept to sort lists of elements.  It's also a great chance to practice recursion.

### What are the objectives?
<!-- specific/measurable goal for students to achieve -->
*After this workshop, developers will be able to:*

- explain three steps to create a recursive algorithm.
- describe the merge sort algorithm and a merge algorithm.
- write a pseudocode version of merge sort and a Python version of merge sort.
- determine the runtime (in big-`O()` notation) for merge sort.

### Where should we be now?
<!-- call out the skills that are prerequisites -->
*Before this workshop, developers should already be able to:*

- iterate through an array using a `for` loop, `forEach`, or other iterators.
- describe the purpose of big-`O()` notation.



## Merge Sort


Take a look at [this video](https://youtu.be/cDNqk4tdvqQ?t=11s).  Can you see how merge sort works?

Merge sort works on the basic principal of divide and conquer - dividing your list into sub-lists (recursively) until your sub-lists are of length one or zero.  Once your sub-lists are at that size, you merge with a neighboring sub-list.  When you merge them, you merge them in sorted order.

![Merge Sort visualization](https://webdocs.cs.ualberta.ca/~holte/T26/Lecture6Fig6.gif)


There are usually TWO algorithms that work together to accomplish a merge sort:

-  A merging algorithm that takes two sorted arrays and combined them into one large sorted array pushing the lowest to highest valued elements. The merge algorithm is not recursive.

-  A merge sort algorithm that takes an array, splits it into two halves, recursively merge sorts both halves, and finally uses the merge algorithm to put them back together into one sorted array.

> Note: iterative merge sort is possible, but it's *much* harder. Please work on a recursive version!

### Make your own merge sort implementation!

Clone this repository and open the file structure in your IDE. You will see a folder labeled `merge_sort` and a folder labeled `tests`.  Run this command in your terminal:

```bash
$ python3 tests/test_merge_sort.py 
```
 Witness many tests fail!  We need to get all of these to pass!


**Goal**: Write a `merge` function and a `merge_sort` function to implement recursive merge sort as described above.  Save your work in the `merge_sort/merge_sort.py` file.



1. Start with the recursive `merge_sort` -- assume you have a working `merge` function. Consider:  
  *  What base case(s) do you need for `merge_sort`?  
  *  What smaller subproblems can you solve recursively?  
  *  How will you go from the solutions for subproblems, to a solution for the overall problem?

2. Next, tackle `merge`. This isn't recursive, but edge cases can make it tricky!

<!--
## Recursion Trees

When dealing with recursion, we often use a tree structure to make an educated guess about Big O runtime.  Here's one for `factorial`:

<img width=25% src="https://copingwithcomputers.files.wordpress.com/2013/11/factorialrecursion-e1384837049546.png">

Each node in the tree represents a subproblem. The root node is the original problem. Base cases are the leaves - the nodes at the bottom of the tree that don't have any children. 

Once we have our tree, the total runtime can be calculated by summing up the work required for every node. We can do this by finding the total work at each level of the tree, then summing up the levels of the tree.  If the work at each level is the same, this can be simplified to multiplying the work at each level by the number of levels in the tree. 

Here's a merge sort recursion tree:

<img src="http://intra.oxido.tv/wp-admin/includes/recursion-tree-method-for-solving-recurrences-examples-i0.png">

The number of levels is log<sub>2</sub>n, and the work required at each level adds up to O(n).  Recursion trees aren't foolproof - this is a "hand wavey" way to show that the Big O runtime of merge sort is `O(n log(n))`.   Since the work at each level is very, very similar, the recursion tree gives us the correct big O for merge sort!

-->
## Additional Resources

* [Merge sort on wikipedia](https://en.wikipedia.org/wiki/Merge_sort)
* [Calculating Big O for recursion from MIT](
https://courses.csail.mit.edu/6.006/spring11/rec/rec08.pdf)
* [Graphical comparison of sorting algorithms](http://www.sorting-algorithms.com/)
