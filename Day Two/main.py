import os, re


class Bag(object):
    
    def __init__(self) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0
        
    def __str__(self) -> str:
        return f"Red: {self.red}, Green: {self.green}, Blue: {self.blue}"
    
    

with open(os.path.join("Day Two","data.txt")) as f:
    file = [line.rstrip() for line in f]
 
def partOne():  
    total = 0     

    for line in file:
        lineData = line.split(":")
        id = int(re.findall(r'\d+', lineData[0])[0])
        
        red = [int(a) for a in re.findall(r'(\d+)\s+red', lineData[1])]
        green = [int(a) for a in re.findall(r'(\d+)\s+green', lineData[1])]
        blue = [int(a) for a in re.findall(r'(\d+)\s+blue', lineData[1])]
        
        if any(num > 12 for num in red):
            continue
        if any(num > 13 for num in green):
            continue
        if any(num > 14 for num in blue):
            continue
        
        total += id
        
    return total


def partTwo():
    powers = []
        
    for line in file:
        lineData = line.split(":")
        
        red = [int(a) for a in re.findall(r'(\d+)\s+red', lineData[1])]
        green = [int(a) for a in re.findall(r'(\d+)\s+green', lineData[1])]
        blue = [int(a) for a in re.findall(r'(\d+)\s+blue', lineData[1])]
        
        redMax = max(red) if red else 1
        greenMax = max(green) if green else 1
        blueMax = max(blue) if blue else 1
        
        powers.append(redMax*greenMax*blueMax)
        
    return sum(powers)

print(f"Part One: {partOne()}")
print(f"Part Two: {partTwo()}")