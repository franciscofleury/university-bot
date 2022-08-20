
def read_token():
    with open("token.txt",'r') as f:
        lines = f.readlines()
        f.close()
        return lines[0].strip()