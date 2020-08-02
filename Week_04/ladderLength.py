class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        l = len(beginWord)

        dic = defaultdict(list)
        for word in wordList:
            for i in range(l):
                dic[word[:i] + '*' + word[i+1:]].append(word)

        quene = [(beginWord, 1)]
        use_dict = {beginWord: True}
        while quene:
            cur_word, level = quene.pop(0)
            for i in range(l):
                key = cur_word[:i] + '*' + cur_word[i+1:]
                for word in dic[key]:
                    if word == endWord:
                        return level + 1
                    if word not in use_dict:
                        use_dict[word] = True
                        quene.append((word, level+1))
        return 0