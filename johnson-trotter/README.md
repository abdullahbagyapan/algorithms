# Johnson–Trotter Algorithm

The Johnson-Trotter algorithm is a method used to generate all permutations of a set. It was developed by Selmer M. Johnson and Hale F. Trotter in 1962.

The algorithm efficiently generates permutations without any repeated elements, and it ensures that adjacent permutations differ by only swapping two adjacent elements. This makes it useful in various applications such as combinatorial problems, sorting algorithms, and generating permutations for puzzles like the 15-puzzle.

Here's a basic overview of how the algorithm works:

1. Start with an initial permutation, typically in ascending order. For example, if we want to generate permutations of the numbers 1 to n, the initial permutation would be [1, 2, 3, ..., n].

2. Initialize an array to keep track of the direction of each element. Initially, all elements point to the left.

3. Find the largest mobile element in the permutation. An element is considered "mobile" if its neighboring element in the direction it points is smaller than itself.

4. Swap the mobile element with its adjacent neighbor in the direction it points.

5. Reverse the direction of all elements larger than the swapped element.

6. Repeat steps 3-5 until no more mobile elements exist.

7. Output the generated permutation.

8. Repeat steps 3-7 until all permutations are generated.

The key idea behind the Johnson-Trotter algorithm is to efficiently generate permutations by focusing only on swapping adjacent elements and updating the direction of elements. This ensures that all permutations are generated and that adjacent permutations are obtained by only a single swap, making it an efficient method for generating permutations.