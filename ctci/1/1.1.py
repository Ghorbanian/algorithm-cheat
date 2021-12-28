class Solution(object):
    def is_unique(self, string):
        return len(string) == len(set(string))

if __name__ == '__main__':
    solution = Solution()
    for string in ['math', 'banana', '', 'a']:
        print(solution.is_unique(string))
