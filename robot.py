class Robot:
    x = int
    y = int
    face = ""

    def __init__(self, x, y, face):
       self.x = x
       self.y = y
       self.face = face

    def show(self):
        print(self.x, self.y)
    
    def change_direction(self, direction): #THIS FUNCTION CAHNGES THE DIRECTION OF THE BOT'S FACE
        if direction == "left":#IF THE ROBOT IS FACING NORTH AND WE SAY TO MOVE LEFT, SO IT FACES WEST
            if self.face == "north":
                self.face = "west"
            elif self.face == "south":
                self.face = "east"
            elif self.face == "west":
                self.face = "south"
            elif self.face == "east":
                self.face = "north"
        elif direction == "right":
            if self.face == "north":
                self.face = "east"
            elif self.face == "south":
                self.face = "west"
            elif self.face == "west":
                self.face = "north"
            elif self.face == "east":
                self.face = "south"

    def move_bot(self):
        if self.face == "north":
            if self.y + 1 < 5:  # to keep the robot on the table (avoid the falling)
               self.y = self.y +  1# IF THE BOTS IS FACING NORTH THEN WE INCREASE THE Y- AXIS
        elif self.face == "south":
            if self.y - 1 >= 0:  
               self.y = self.y - 1
        elif self.face == "west":#IF WE MOVE THE BOT TOWARDS LEFT
            if self.x - 1 >= 0:  
               self.x = self.x - 1
        elif self.face == "east":
            if self.x + 1 < 5:  
               self.x = self.x + 1

    def give_instruction(self, instruction):
        if instruction == "move":
            self.move_bot()
        else:
            self.change_direction(instruction)

    def print_state(self):
        print(str(self.x) + "," + str(self.y) + "," + self.face.upper())



robot = []
index = 0
num_of_bots = 0
while(True):
    instruction = input().lower()
    if instruction.find("place") == 0:
        words = instruction.split(" ")
        values = words[1].split(",")
        robot.append(Robot(int(values[0]), int(values[1]), values[2].lower()))
        num_of_bots = num_of_bots + 1 #INCREASE THE NUMBER OF BOTS CAN ONLY PLACED 25 BOTS
    elif instruction == "report":
        break
    elif instruction.find("robot") == 0:
        words = instruction.split(" ")
        index = int(words[1])
    else:
        robot[index].give_instruction(instruction)

print("Robots on table: ", num_of_bots)
print("Bot active: Robot ", index)
x = 0
for bot in robot:
    print("State of Robot: ", x)#stats shown for Robot 1/Robot 2..
    bot.print_state()#THIS IS FOR FIRST POSTION OF THE ROBOT IS IN.
    x += 1




