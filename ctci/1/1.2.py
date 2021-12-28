from collections import Counter
from itertools import permutations

class Solution(object):
    def check_permutations(self, string_a, string_b):
        if len(string_a) != len(string_b):
            return False

        # strings should have identical character counts
        counter_a = Counter(string_a)
        counter_b = Counter(string_b)

        for count_a, count_b in zip(sorted(counter_a.elements()), sorted(counter_b.elements())):      
            if count_a != count_b:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    for string_a, string_b in [('dog', 'god'), ('jinja', 'vininger'), ('', ''), ('banana', 'nnaaab')]:
        print(solution.check_permutations(string_a, string_b))

    print('===STRESS TESTING===')
    example_string = 'abcd'
    for perm in permutations(example_string):
        print(solution.check_permutations(example_string, perm))