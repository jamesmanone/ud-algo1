# Problem 4: Dutch National Flag

When an array had only 3 discrete values sorting them on a single traversal is rather trivial.
1. Establish indices for the start and end of the middle value (1). (traversing all 0's and 2's on the end once with while loops)
2. Traverse the middle section, swapping 0's and 2's with your start and end indices respectively.
3. When your search index exceeds your middle->end index you have traversed each item once and sorted the array

This could be done by moving values to 3 different arrays and returning `zeros + ones + twos` but this would cause a copy which could be viewed as a second traversal.
