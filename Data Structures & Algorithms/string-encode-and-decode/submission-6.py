class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for each in strs:
            encoded_string += str(each)
            encoded_string += "~"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        new_s = list(s)
        index_cut = []
        decoded_strs = []
        i = 0
        for char in new_s:
            if char == "~":
                index_cut.append(i)
            i += 1
        i = 0
        for j in (index_cut):
            decoded_strs.append(s[i:j])
            i = j + 1
        return decoded_strs