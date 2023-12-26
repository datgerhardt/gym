
class Machine:
    def __init__(self, code: str):
        self.memory = [ 0 for _ in range(30000)]
        print("len of memory: ", len(self.memory))
        self.ip = 0 
        self.dp = 0 

        self.code = code
        self.buf = []
        
    
    def execute(self):
        while self.ip < len(self.code):
            match self.code[self.ip]:
                case '+':
                    self.memory[self.dp] += 1
                case '-':
                    self.memory[self.dp] -= 1
                case '>':
                    self.dp += 1
                case '<':
                    self.dp -= 1
                case '.':
                    self.print()
                case ',':
                    self.read()
                case '[':
                    if self.memory[self.dp] == 0:
                        depth = 1
                        while depth != 0:
                            self.ip += 1
                            if self.code[self.ip] == '[':
                                depth += 1
                            if self.code[self.ip] == ']':
                                depth -= 1
                case ']':
                    if self.memory[self.dp] == 0:
                        depth = 1
                        while depth != 0:
                            self.ip += 1
                            if self.code[self.ip] == ']':
                                depth += 1
                            if self.code[self.ip] == '[':
                                depth -= 1

            self.ip += 1


    def print(self):
        s = self
        print(s.dp, s.ip)

    def read(self):
        s = self
        print(s.dp, s.ip)


        
if __name__ == "__main__":
    code = """
        ++++++++[>++++[>++>+++>+++>+<<
        <<-]>+>+>->>+[<]<-]>>.>---.+++
        ++++..+++.>>.<-.<.+++.------.-
        -------.>>+.>++.
    """
    mac = Machine(code.strip())
    mac.execute()