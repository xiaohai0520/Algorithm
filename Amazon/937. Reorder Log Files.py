class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        l = [log for log in logs if log[-1].isalpha()]
        d = [log for log in logs if log[-1].isdigit()]
        return sorted(l, key = lambda x: (x[x.find(" "):], x[:x.find(" ")])) + d
