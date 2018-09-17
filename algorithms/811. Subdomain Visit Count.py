#use dic to save the times


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        res = []
        for domain in cpdomains:
            n = int(domain.split()[0])
            name = domain.split()[-1]
            nameList = name.split('.')
            for i in range(len(nameList)):
                cur = '.'.join(nameList[i:])
                dic[cur] = dic.get(cur,0) + n
        for k,v in dic.items():
            res.append(str(v) + ' ' + k)
        return res 
