from enum import Enum
import random

#create enum for grass situation
class Situation(Enum):
    GOOD = 1
    BAD = 2
    VERYBAD = 3

#create a enum for job class
class JobClass(Enum):
    S = 0
    A = 1 #max 500 to 2000 tree
    B = 2 #max 200 to 500 tree
    C = 3 #max 100 to 200
    D = 4 #max 50 to 100 tree
    E = 5 #max 50 tree
    UNDEFINED = 6

class Job:
    def __init__(self, number, job_class,period_of_time):
        self.number = number
        self.generate_job_dimension(job_class)

        self.tot_area= self.width * self.height
        self.generate_matrix(self.width, self.height)
        #self.print_matrix()
        self.calculate_average_situation_trees()
        self.calculate_average_situation_grass()
        self.set_todo_list(period_of_time)
        self.accepted = False
        self.to_accept = False
        self.accept_at=-1

        #print(str(self.width) + " x " + str(self.height))
        #print("number of trees: " + str(self.n_olive_tree))
        #print("total area: " + str(self.tot_area))
        #print("average situation of the tree is: " + str(self.average_situation_trees))
        #print("average situation of the grass is: " + str(self.average_situation_grass))
    def check_if_completed(self):
        for todo in self.todo_list:
            if todo == "PRUNE":
                for i in range(self.width):
                    for j in range(self.height):
                        if self.matrix[i][j] == "O":
                            if(self.matrix[i][j] > 0):
                                return False
            if todo == "CLEAN":
                for i in range(self.width):
                    for j in range(self.height):
                        if self.matrix[i][j] == "G":
                            if(self.matrix[i][j] > 0):
                                return False
            return True
                
    def set_price(self,price,current_time):
        self.to_accept=True
        self.price = price
        self.accept_at = current_time + random.randint(10,20)
    def set_todo_list(self,period_of_time):
        self.todo_list = []
        
        if period_of_time == "prune":
            self.todo_list.append("PRUNE")
            perc_clean = 60
        elif period_of_time == "harvest":
            self.todo_list.append("HARVEST")
            perc_clean = 20

        if random.randint(1, 100) < perc_clean:
            self.todo_list.append("CLEAN")


    def generate_job_dimension(self,job_class):
        self.job_class = JobClass.UNDEFINED
        while job_class != self.job_class:
            self.width= random.randint(3, 50)
            if self.width % 2 == 1:
                self.width = self.width
            else:
                self.width = self.width + 1
            self.height= random.randint(3, 50)
            if self.height % 2 == 1:
                self.height = self.height
            else:
                self.height = self.height + 1
            self.n_olive_tree = (self.width-1)/2 * (self.height-1)/2
            if self.n_olive_tree <= 50 :
                self.job_class = JobClass.E
            elif self.n_olive_tree <= 100 :
                self.job_class = JobClass.D
            elif self.n_olive_tree <= 200 :
                self.job_class = JobClass.C
            elif self.n_olive_tree <= 500 :
                self.job_class = JobClass.B
            elif self.n_olive_tree <= 2000 :
                self.job_class = JobClass.A
            elif self.n_olive_tree > 2000 :
                self.job_class = JobClass.S

    def generate_matrix(self, width, height):
        self.matrix = []

        for i in range(width):
            self.matrix.append([])
            for j in range(height):
                self.matrix[i].append(0)
        for i in range(width):
            for j in range(height):
                if j % 2 == 0:
                    if random.randint(0, 1) == 1:
                        self.matrix[i][j] = Terrain()
                    else:
                        self.matrix[i][j] = Grass()
                else:
                    if i % 2 == 0:
                        if random.randint(0, 1) == 1:
                            self.matrix[i][j] = Terrain()
                        else:
                            self.matrix[i][j] = Grass()
                    else:
                        self.matrix[i][j] = Tree()
    #print the matrix type
    def print_matrix(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.matrix[i][j].type)
            print()
    #calculate the average situation of the trees
    def calculate_average_situation_trees(self):
        sum = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.matrix[i][j].type == "O":
                    sum = sum + self.matrix[i][j].situation
        self.average_situation_trees = round(sum / self.n_olive_tree)
        #caluculate the average situation of the grass
    def calculate_average_situation_grass(self):
        sum = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.matrix[i][j].type == "G":
                    sum = sum + self.matrix[i][j].situation
        self.average_situation_grass = round(sum / (self.tot_area - self.n_olive_tree))
    def get_tree_situation(self):
        if self.average_situation_trees == 1:
            return "GOOD"
        elif self.average_situation_trees == 2:
            return "BAD"
        elif self.average_situation_trees == 3:
            return "VERY BAD"
    def get_grass_situation(self):
        if self.average_situation_grass == 1:
            return "GOOD"
        elif self.average_situation_grass == 2:
            return "BAD"
        elif self.average_situation_grass == 3:
            return "VERY BAD"
            


#create a class called tree
#this class will be used to create a tree object
#his properties are type of tree, production, situation
class Terrain:
    def __init__(self, type = "T"):
        self.type = type

class Tree(Terrain):
    def __init__(self):
        super().__init__("O")
        self.nolive=random.randint(1000, 5000)
        self.kgolive=self.nolive * 3 / 1000
        self.situation = random.randint(1, 3)

        

class Grass(Terrain):
    def __init__(self):
        super().__init__("G")
        self.situation = random.randint(1, 3)


class Item():
    def __init__(self, name, image, position,interact_on_top,visible=True,hide_to_pick=True):
        self.name = name
        self.image = image
        self.position = position
        self.interact_on_top = interact_on_top
        self.visible = visible
        self.hide_to_pick = hide_to_pick
    def pickup(self):
        if(self.hide_to_pick):
            self.visible = False
    def drop(self, position):
        if(self.hide_to_pick):
            self.visible = True
            self.position = position

class Player():
    def __init__(self, name, position,draw_game):
        self.name = name
        self.position = position
        self.inventory = None
        self.draw_game = draw_game
    def move(self, direction):
        if direction == 'n':
            if self.draw_game.positionallowed(self.matrix,self.position[0], self.position[1]-1):
                self.position = self.position[0], self.position[1]-1
        elif direction == 's':
            if self.draw_game.positionallowed(self.matrix,self.position[0], self.position[1]+1):
                self.position = self.position[0], self.position[1]+1
        elif direction == 'o':
            if self.draw_game.positionallowed(self.matrix,self.position[0]-1, self.position[1]):
                self.position = self.position[0] -1, self.position[1]
        elif direction == 'e':
            if self.draw_game.positionallowed(self.matrix,self.position[0]+1, self.position[1]):
                self.position = self.position[0] +1, self.position[1]
    def set_matrix(self, matrix):
        self.matrix = matrix
    def pickup(self,draw_game,items):
        for item in items:
            if item.position[0] == self.position[0] and item.position[1] == self.position[1] and item.visible and item.interact_on_top and self.inventory == None:
                item.pickup()
                self.inventory = item
                self.draw_game.draw_inventory(self)
    def drop(self):
        self.inventory.drop(self.position)
        self.inventory = None
        self.draw_game.draw_inventory(self,False)
        
    def interact_on_ground(self,terrain,trimmer_sound):
        if self.inventory ==None:
            return False
        if terrain.type == "G":
            if self.inventory.name =="trimmer" and terrain.situation > 0:
                #trimmer_sound.play()
                terrain.situation -= 1
                return True
        
        return False
    def interact_on_direction(self,matrix,dir):
        if self.inventory ==None:
            return False
        try:
            if dir == 'n':
                if matrix[self.position[0]][self.position[1]-1].type == "O":
                    if self.inventory.name =="prune_tools" and matrix[self.position[0]][self.position[1]-1].situation > 0:
                        matrix[self.position[0]][self.position[1]-1].situation -= 1
                        return True
            elif dir == 's':
                if matrix[self.position[0]][self.position[1]+1].type == "O":
                    if self.inventory.name =="prune_tools" and matrix[self.position[0]][self.position[1]+1].situation > 0:
                        matrix[self.position[0]][self.position[1]+1].situation -= 1
                        return True
            elif dir == 'o':
                if matrix[self.position[0]-1][self.position[1]].type == "O":
                    if self.inventory.name =="prune_tools" and matrix[self.position[0]-1][self.position[1]].situation > 0:
                        matrix[self.position[0]-1][self.position[1]].situation -= 1
                        return True
            elif dir == 'e':
                if matrix[self.position[0]+1][self.position[1]].type == "O":
                    if self.inventory.name =="prune_tools" and matrix[self.position[0]+1][self.position[1]].situation > 0:
                        matrix[self.position[0]+1][self.position[1]].situation -= 1
                        return True
        except:
            return False
        return False
                


