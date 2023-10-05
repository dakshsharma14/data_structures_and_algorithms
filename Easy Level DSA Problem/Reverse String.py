from typing import List


class Solution:
    # The -> None indicates that the method doesn't return any value but instead modifies the list in-place.
    def reverseString(self, s: List[str]) -> None:
        """
        s.reverse(): The second implementation uses the reverse() method, which reverses the list in-place by
        modifying the original list. This method also has a time complexity of O(n) but may involve more
        operations internally, including iterating through the list to perform the reversal. Additionally,
        it may not be as efficient in terms of memory allocation and deallocation as the first approach.
        """
        # s.reverse()

        """
        Two-Pointer Approach: The first implementation iterates through the list once, swapping characters at 
        the left and right pointers until they meet in the middle. It has a time complexity of O(n/2) (where n is 
        the length of the list), which simplifies to O(n), and it doesn't involve creating a new list. This is a 
        very efficient way to reverse a list.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# created an instance of a class
solution = Solution()

input_list = ["a", "b", "c"]
solution.reverseString(input_list)

print(input_list)
