from collections import Counter

class Solution(object):
    def one_away(self, a, b):
        a_counts = Counter(a)
        b_counts = Counter(b)

        diff = 0
        for a_key in a_counts.keys():
            a_count = a_counts[a_key]
            b_count = b_counts[a_key]
            diff += abs(a_count - b_count)
        
        for b_key in b_counts.keys():
            b_count = b_counts[b_key]
            a_count = a_counts[b_key]
            diff += abs(a_count - b_count)
            
        return diff <= 2

if __name__ == '__main__':
    solution = Solution()
    for a, b in [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('pale', 'bake')]:
        print(solution.one_away(a, b))
