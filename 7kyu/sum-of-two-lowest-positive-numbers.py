# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like[19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.


# need to account for negative numbers as inputs, if only positive numbers are in the input, then the following one-liner works: return sum(sorted(numbers)[:2])

def sum_two_smallest_numbers(numbers):
  result = []
  for num in sorted(numbers):
    if num >= 0:
      result.append(num)
    if len(result) >= 2:
      break
  return sum(result)



print(sum_two_smallest_numbers([-10, -5, -100, 7, 15, 12, 18, 22]))
