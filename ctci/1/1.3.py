class Solution(object):
    def urlify(self, url):
        return url.replace(' ', '%20')
    
    def urlify_without_replace(self, url):
        chars = list(url)
        for i in range(len(chars)):
            char = url[i]
            if char == ' ':
                chars[i] = '%20'
        
        return ''.join(chars)


if __name__ == '__main__':
    solution = Solution()
    for url in ['jamming to sweet tunes', '', 'a b c d', 'abcd', ' ', '    a    ', '  ']:
        print(solution.urlify(url))

    print('===URLIFY without replace()')
    for url in ['jamming to sweet tunes', '', 'a b c d', 'abcd', ' ', '    a    ', '  ']:
        print(solution.urlify_without_replace(url))