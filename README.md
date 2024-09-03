To prove the correctness of selection sort, we need to show three things about a loop invariant:

1. **Initialization**
2. **Maintenance**
3. **Termination**

**Initialization** — At the start, when \( i = 0 \), the subarray from the beginning up to index \( i \) is trivially sorted (it is either empty or contains just one element). Therefore, the loop invariant holds initially, as the subarray on the left is sorted.

**Maintenance** — At the start of each iteration, the subarray from \( 0 \) to \( i-1 \) is sorted, and none of these elements will be disturbed in future iterations. The inner loop identifies the smallest element in the unsorted portion of the array (from index \( i \) to \( n-1 \)) and swaps it with the element at index \( i \). After this swap, the subarray from \( 0 \) to \( i \) is sorted. The new element at index \( i \) is guaranteed to be greater than or equal to all the elements to its left, ensuring that the loop invariant is maintained throughout each iteration.

**Termination** — When the algorithm terminates, the loop counter reaches \( n-1 \). At this point, the entire array is sorted. The loop invariant ensures that the subarray to the left of the current element is sorted, and since there are no remaining elements to compare, the entire array is in sorted order.

Thus, selection sort is correct.
