# https://leetcode.com/problems/unique-email-addresses/

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []

        for email in emails:
            local, domain = email.split("@")

            i = 0
            uniqueLocal = []

            while (i < len(local)):
                if local[i] == "+":
                    break
                if local[i] != ".":
                    uniqueLocal.append(local[i])
                i += 1
            uniqueEmail = "".join(uniqueLocal) + "@" + domain

            if uniqueEmail not in result:
                result.append(uniqueEmail)

        return len(result)

A = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leet+code.com", 
"test.this.email+wow@lee.tcode.com", "testemail+david@lee.tcode.com", "test.this.email+gyyyy@lee.tcode.com"]
# A = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
test = Solution()
print(test.numUniqueEmails(A))