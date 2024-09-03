To prove the correctness of selection sort, we need to show three things about a loop invariant:

1. **Initialization**
2. **Maintenance**
3. **Termination**

**Initialization** — At the start, when \( i = 0 \), the subarray from the beginning up to index \( i \) is trivially sorted (it is either empty or contains just one element). Therefore, the loop invariant holds initially, as the subarray on the left is sorted.

**Maintenance** — At the start of each iteration, the subarray from \( 0 \) to \( i-1 \) is sorted, and none of these elements will be disturbed in future iterations. The inner loop identifies the smallest element in the unsorted portion of the array (from index \( i \) to \( n-1 \)) and swaps it with the element at index \( i \). After this swap, the subarray from \( 0 \) to \( i \) is sorted. The new element at index \( i \) is guaranteed to be greater than or equal to all the elements to its left, ensuring that the loop invariant is maintained throughout each iteration.

**Termination** — When the algorithm terminates, the loop counter reaches \( n-1 \). At this point, the entire array is sorted. The loop invariant ensures that the subarray to the left of the current element is sorted, and since there are no remaining elements to compare, the entire array is in sorted order.

Thus, selection sort is correct.

Question- Benchmark the runtime of each algorithm. Your benchmarks should include information about your computer (ram, cpu etc.) and be run with various input sizes; from small (array of size 5,10,20) all the way up to large arrays (where your computer is struggling). I should at the very least see a plot of time vs input size n. Feel free to use benchmarking software.

Insertion Sort - Array Size: 5, Time: 0.000010 seconds
Selection Sort - Array Size: 5, Time: 0.000013 seconds
Bubble Sort - Array Size: 5, Time: 0.000008 seconds
Insertion Sort - Array Size: 10, Time: 0.000011 seconds
Selection Sort - Array Size: 10, Time: 0.000011 seconds
Bubble Sort - Array Size: 10, Time: 0.000015 seconds
Insertion Sort - Array Size: 50, Time: 0.000097 seconds
Selection Sort - Array Size: 50, Time: 0.000140 seconds
Bubble Sort - Array Size: 50, Time: 0.000298 seconds
Insertion Sort - Array Size: 100, Time: 0.000630 seconds
Selection Sort - Array Size: 100, Time: 0.000464 seconds
Bubble Sort - Array Size: 100, Time: 0.000823 seconds
Insertion Sort - Array Size: 200, Time: 0.001580 seconds
Selection Sort - Array Size: 200, Time: 0.001550 seconds
Bubble Sort - Array Size: 200, Time: 0.003130 seconds
Insertion Sort - Array Size: 500, Time: 0.012403 seconds
Selection Sort - Array Size: 500, Time: 0.011406 seconds
Bubble Sort - Array Size: 500, Time: 0.021706 seconds
Insertion Sort - Array Size: 700, Time: 0.021237 seconds
Selection Sort - Array Size: 700, Time: 0.021711 seconds
Bubble Sort - Array Size: 700, Time: 0.044368 seconds
Insertion Sort - Array Size: 1000, Time: 0.044810 seconds
Selection Sort - Array Size: 1000, Time: 0.049152 seconds
Bubble Sort - Array Size: 1000, Time: 0.092372 seconds
Insertion Sort - Array Size: 1500, Time: 0.110046 seconds
Selection Sort - Array Size: 1500, Time: 0.111769 seconds
Bubble Sort - Array Size: 1500, Time: 0.222025 seconds

![image](https://github.com/user-attachments/assets/bf169e11-ed11-4fc7-ba75-56c43da33958)

