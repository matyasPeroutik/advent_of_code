f = open("./Day 6/input.txt", "r")

score = 0

class Signal:

    def __init__(self, signal):
        self.signal = signal


    def packet_start(self, beginning):
        for i in range(len(self.signal)-(beginning-1)):
            count = 0
            for j, letter in enumerate(self.signal[i : i+beginning]):
                substr = self.signal[int(i)+int(j)+1 : int(i)+beginning]
                if not (letter in substr): count+=1
                if(count == beginning): return i+beginning

            


for line in f:
    line = line.strip(' \n')
    print(Signal(line).packet_start(4))
    print(Signal(line).packet_start(14))