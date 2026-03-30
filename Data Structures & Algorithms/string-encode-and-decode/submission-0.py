class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            count_str = str(len(i))
            encoded+= count_str+"#"+i
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded_str =[]
        number = ""
        while len(s)>0:
            
            if s[0] != "#":
                number+=s[0] 
                s=s[1:]
            if s[0]  == "#":
                s=s[1:]
                str_len = int(number)
                decoded_str.append(s[:str_len])
                s = s[str_len:]
                number = ""
        return decoded_str
