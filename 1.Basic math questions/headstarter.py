# Here is the problem that you will be solving:
# Construct an algorithm that, given a set of unique positive integers named 'candidates' and a positive integer named 'target', finds every possible combination of the numbers from 'candidates' that can be summed up to equal the 'target' value.
# The same element from 'candidates' can be selected multiple times to form a combination, but the final list must only include unique combinations, differing by at least one element's frequency.
# Ensure your solution can efficiently handle combinations leading to a total of fewer than 150 unique solutions for the provided 'target'.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation: There are two combinations using the numbers 2, 3, and 7 that sum up to 7.
# Notice the number 2 is reused in one combination.


def combinationSum(candidates, target):
    # Sort the candidates to help with pruning
    candidates.sort()
    result = []

    def findCombinations(target, current_combination, index):
        # Base case: if target becomes zero, we found a combination
        if target == 0:
            result.append(list(current_combination))
            return

        # Explore further
        for i in range(index, len(candidates)):
            # If the current candidate exceeds the target, stop exploring further
            if candidates[i] > target:
                break

            # Include the candidate and continue the search with reduced target
            current_combination.append(candidates[i])
            findCombinations(
                target - candidates[i], current_combination, i
            )  # 'i' instead of 'i+1' to reuse the same element

            # Backtrack: remove the last added candidate to try the next one
            current_combination.pop()

    # Start backtracking with an empty combination and starting index of 0
    findCombinations(target, [], 0)

    return result


# Test cases
print(combinationSum([2, 3, 6, 7], 7))  # Output: [[2, 2, 3], [7]]
print(combinationSum([2, 3, 5], 8))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
print(combinationSum([2], 1))  # Output: []
