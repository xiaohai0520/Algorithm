class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        
        
        res = set()
        for email in emails:
            local,domain = email.split('@')
            local = local[:local.index('+')].replace('.','')
            res.add(local + "@" + domain)
        return len(res)
    
    
    
    
        # emails = [email.split('@') for email in emails]
        # for email in emails:
        #     email[0] = email[0].replace('.','')
        #     if '+' in email[0]:
        #         email[0] = email[0][:email[0].index('+')]
        # emails = [tuple(email) for email in emails]
        # res = set(emails)
        # return len(res)
