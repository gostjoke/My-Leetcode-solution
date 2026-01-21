# 2026/01/20
class Solution:
    def simplifyPath(self, path: str) -> str:
        c = path.split("/")
        st = []
        for i in c:
            if i == '' or i =='.':
                continue
            if i == "..":
                if st:
                    st.pop()
            else:
                st.append(i)
        return "/" + '/'.join(st)
