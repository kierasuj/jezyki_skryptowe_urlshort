from decorators import singleton
import string

@singleton
class IdGenerator:
    def __init__(self, length) -> None:
        self.CHARS = string.digits + string.ascii_uppercase
        self.id = "0" * length
        self.length = length
    
    def next_id(self) -> str:
        num = self.__str_to_int(self.id) + 1
        self.id = self.__int_to_str(num)
        return self.id 
    
    def is_valid_id(self, id: str) -> bool:
        if len(id) != self.length:
            return False
        allowed_characters = set(string.ascii_letters + string.digits)
        return all(c in allowed_characters for c in id)
    
    def __str_to_int(self, s):
        base = len(self.CHARS)
        num = 0
        for char in s:
            num = num * base + self.CHARS.index(char)
        return num

    def __int_to_str(self, num):
        base = len(self.CHARS)
        chars = []
        while num > 0:
            num, rem = divmod(num, base)
            chars.append(self.CHARS[rem])
        s = "".join(reversed(chars))
        return s.zfill(self.length)