f = open("./Day 5/input.txt", "r")

score = 0
topPartOfInput = []

class Storage:
    

    def __init__(self, schema: list):

        self.stacks = {}

        numeration = schema[-2].strip(' ').split(' ')
        schemaPopped = schema
        schemaPopped.pop()
        schemaPopped.pop()
        for stackIndex in range(int(numeration[0]), int(numeration[-1])+1):
            self.stacks[stackIndex] = Stack(schemaPopped, stackIndex)
        

    def move(self, ammount, stackIndex, targetIndex):

        crates = self.stacks[stackIndex].take_crates(ammount)
        self.stacks[targetIndex].add_crates(crates)


    def __str__(self) -> str:
        
        ret = ""

        for stack in self.stacks.values():

            ret+=str(stack)

        return ret
        
        

class Stack:

    def __init__(self, schema: list, index: int):

        self.crates = []
        
        for line in schema:
            # print(line)
            if line[1+((index-1)*4)] != " ": self.crates.append(line[1+((index-1)*4)])
        
        self.crates.reverse()

    def take_crates(self, ammount):

        res = []
        
        for i in range(ammount):
            res.append(self.crates.pop())

        return res

    def add_crates(self, deposit: list):

        #A2
        deposit.reverse()

        for crate in deposit:
            self.crates.append(crate)
        

    def __str__(self) -> str:
        if self.crates: return self.crates[-1]
        return ""

            

        

for line in f:
    line = line.strip('\n')
    topPartOfInput.append(line)
    if line == "":
        break;

warhouse = Storage(topPartOfInput)

for line in f:
    line = line.strip('\n')
    line = line.split(' ')

    warhouse.move(int(line[1]), int(line[3]), int(line[5]))

print(warhouse)
    