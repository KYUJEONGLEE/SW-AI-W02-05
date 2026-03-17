# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         dictionary = {}
#         for str in strs:
#             str = sorted(str)

if __name__ == "__main__":
    dictionary = dict()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    for str in strs:
        key = ''.join(sorted(str))

        if key not in dictionary:
            dictionary[key] = []

        dictionary[key].append(str)

print(dictionary.values())
