import itertools

class PhonePad(object):

    def __init__(self):
        self.dic = {'2':'abc', '3':'def', '4':'ghi',
                        '5':'jkl', '6':'mno', '7':'pqrs',
                        '8':'tuv', '9':'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        res = ['']
        for d in digits:
            newResult = []
            for x in self.dic[d]:
                for string in res:
                    newResult.append(string + x)
            res = newResult
        return res

    def letterCombinations1(self, digits):
        if not digits:
            return []

        res, line = [], []
        self.helper(digits, 0, res, line)
        return res

    def helper(self, digits, cur, res, line):
        if len(line) == len(digits):
            res.append(''.join(line[:]))
            return

        for x in self.dic[digits[cur]]:
            line.append(x)
            self.helper(digits, cur + 1, res, line)
            line.pop()

    def possible_words(self, digits):
        letters_to_combine = (self.dic[x] for x in digits)
        for letters_group in itertools.product(*letters_to_combine):
            yield ''.join(letters_group)

    """
    usage: list(possible_words("234"))
    """

