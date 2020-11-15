# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []
        
        tracks = collections.defaultdict(int)
        for cp in cpdomains:
            splitted = cp.split()
            count, domain = int(splitted[0]), splitted[1]
            tracks[domain] += count
            # process the rest of the domain
            for i in range(len(domain)):
                if domain[i] == '.':
                    tracks[domain[i+1:]] += count
        return [str(v) + ' ' + k for k, v in tracks.items()]
