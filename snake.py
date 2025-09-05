import random

class snake:
    def __init__(self, size):
        self.size = size

        self.reset()


    def reset(self):
        """Resets the game to its initial state."""
        start_row, start_col = 0, 0
        self.l = [['-' for _ in range(self.size)] for _ in range(self.size)]
        
        self.hr = start_row
        self.hc = start_col
        self.egg = 0
        self.body = [(start_row, start_col)]
        

        self.l[self.hr][self.hc] = 'X'

    def display(self):
        k = 0
        for i in range(self.size):
            print("\t\t", end="")
            for j in range(self.size):
                print(self.l[i][j], "", end=" ")
                k += 1
            print("\n")
        print("COUNT :", self.egg)
        print("\n")

    def move(self, action):

        if (self.hr, self.hc) in self.body:
             self.l[self.hr][self.hc] = "-"

        if(action in ("W","w")):
            self.hr -= 1
        elif(action in ("S","s")):
            self.hr += 1
        elif(action in ("D","d")):
            self.hc += 1
        elif(action in ("a","A")):
            self.hc -= 1

        if self.collision_check():
            print("\n\n\t\tGAME OVER! Snake collided. !\n\n")
            return 1

        self.body.insert(0, (self.hr, self.hc)) # insert new head
        self.l[self.hr][self.hc] = "X"

        if len(self.body) > self.egg + 1:  # remove tail
            tr, tc = self.body.pop()
            # Only erase the tail if it's not where the head is moving to
            if (tr, tc) not in self.body:
                self.l[tr][tc] = "-"

        for r, c in self.body[1:]:  # redraw body
            self.l[r][c] = "o"

    def g_food(self):
        while(True):
            self.r_row = random.randint(0, self.size - 1)
            self.r_column = random.randint(0, self.size - 1)
            if (self.r_row, self.r_column) in self.body:
                continue
            else:
                self.l[self.r_row][self.r_column] = "V"
                break

    def collision_check(self):
        if (self.hr < 0 or self.hr >= self.size) or (self.hc < 0 or self.hc >= self.size):
            return True
        if (self.hr, self.hc) in self.body[1:]:
            return True
        return False

    def food_check(self):
        if(self.r_row == self.hr and self.r_column == self.hc):
            self.egg += 1
            return 1
        else:
            return 0

# Main game loop
a = int(input("enter 1 to start Game ,0 to exit :"))
if a == 1:
    board_size = int(input("\n\t\tEnter the Board Size : "))
    p1 = snake(board_size)

    while(a == 1):
        print("\n\n\t\t SNAKE GAME ! \n\n")
        b_o = 0 
        c = 0   
        
        p1.g_food()
        
        while(c == 0):
            p1.display()
            b = input("enter (WASD) to MOVE :  ")
            if(p1.move(b) == 1):
                b_o = 1
                break
            
            if p1.food_check() == 1:
                p1.g_food()

        if(b_o == 1):
            p1.display() 
            a = int(input("\n\t\tenter 1 to play again on the same board, 0 to exit :"))
            if a == 1:
                p1.reset()