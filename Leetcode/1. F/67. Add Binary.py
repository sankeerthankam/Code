# Add two binary string and return the result in binary 
def addBinary(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
