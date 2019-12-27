# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
  # Open brackets must be closed by the same type of brackets.
  # Open brackets must be closed in the correct order.

# Example 1:
# Input: "()[]{}"
# Output: true

# Example 2:
# Input: "(]"
# Output: false

# Example 3:
# Input: "([)]"
# Output: false


def isValid(self, s: str) -> bool:
    paranthesis_dict = { '(' : ')', '[' :']', '{' :'}'}
    visited = []

    if len(s) % 2 != 0:
        return False

    else:
        for par in s:
            if par in paranthesis_dict:
                visited.append(par)
            else:

                # If we encounter closed paratheses and the length of the visited list is 0
                if len(visited) == 0:
                    return False

                # pop the latest element from the visited stack
                ele = visited.pop()

                # check if the associated paranthesis of the pop element is correct or not 
                if par != paranthesis_dict.get(ele):
                    return False
                else:
                    continue

        # At the end of the loop, all the visited nodes should be popped out
        # Hence the length of the list would be 0
        return len(visited) == 0
