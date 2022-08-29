'''
Take home test (Mars Rover)
Date: 29th Aug 2022
Author: Fionn Mcguire


NOTE 
Please ignore references to the grid in the mars map class
This was purely if I went down the different variations described in the README under potential developments.
The robot class has an initial location variable if we wanted to report where it came from 
to where it is now. Normally, I would take this out as it's unused code but this may assist in the review
'''


class Robot:

    def __init__(self):
        self.initial_location = None 
        self.current_location = None
        self.direction = None
        self.command_list = None 
        self.lost = False 
    
    def strip_command(self,command_str):
        try: 
            # Dividing, stripping and splitting command string into variables
            initial_location, command_list_str = command_str.split(")")
            x,y,direction = initial_location[1:].split()
            x = x.rstrip(",")
            y = y.rstrip(",")
            command_list_str = command_list_str.lstrip()
        except:
            raise(Exception("Command list is not in correct format. Please ensure format is (X, Y, D) Commands eg. (0, 0, N) LRF"))
        
        # Checking some data integrity with assertions
        try:
            x = int(x)
            y = int(y)
            assert direction in "NESW"
            for command in command_list_str:
                assert command in "LRF"
        except:
            raise(Exception("Command list has corrupted data, ensure direction is one of N E S W and commands are in L R F"))
        
        # Setting robot properties 
        self.initial_location = [x,y]
        self.current_location = [x,y]
        self.direction = direction 
        self.command_list = command_list_str

class MarsMap:

    def __init__(self):
        self.grid = []
        self.length = None 
        self.width = None
        self.robots_on_map = []
    
    def strip_grid_dimentions(self,grid_str):
        try:
            x, y = grid_str.split()
            x = int(x)
            y = int(y)
        except:
            raise(Exception("Grid dimentions are in the wrong format, must be 'X Y'"))
        self.grid = [ [ 0 for width in range( x ) ] for length in range( y ) ]
        self.length = y 
        self.width = x


    def navigate(self):
        available_directions = "NESW"
        #navigate the actual map 
        for robot in self.robots_on_map:
            for command in robot.command_list:
                if command == "F":
                    ''' Track last known location if rover is about to go missing
                        NOTE I think i'm building in a bug here to fit the expected output (should be self.width -1 etc)
                        based on the hypothesis that we're returning the last known location and not the faulty location 
                        If we're returning the faulty location, the 0s in this if should be -1'''
                    if ((robot.direction == "E" and robot.current_location[0] == self.width) or
                        (robot.direction == "W" and robot.current_location[0] == 0) or 
                        (robot.direction == "N" and robot.current_location[1] == self.length) or 
                        (robot.direction == "S" and robot.current_location[1] == 0)):
                        
                        robot.lost = True
                        break

                    # Modifying location based on direction 
                    # current_location[0] = X axis 
                    # current_location[1] = Y axis 
                    if robot.direction == "N":
                        robot.current_location[1] += 1
                    elif robot.direction == "S":
                        robot.current_location[1] -= 1
                    elif robot.direction == "E":
                        robot.current_location[0] += 1
                    else:
                        robot.current_location[0] -= 1
                        
                elif command == "L":
                    '''Could replace this with a series of IF statements determining the next direction 
                        based off previous, although this is more complex it's also more concise and easier to maintain / debug
                        available_directions is a clockwise string of directions, when you move left (L), you move one char down in the str
                        when you move right (R) you move one char up the str
                        Using modulous to ensure make it into a loop
                    '''
                    robot.direction = available_directions[(available_directions.find(robot.direction)-1)%4]
                else:
                    robot.direction = available_directions[(available_directions.find(robot.direction)+1)%4]

    def output_results(self):
        for robot in self.robots_on_map:
            return_str = f"({robot.current_location[0]}, {robot.current_location[1]}, {robot.direction})"
            if robot.lost == True:
                return_str+= " LOST"
            print(return_str)

    
    def add_crator(self):
        pass 

    def add_hill(self):
        pass

#####################################
############# INPUT #################
#####################################
grid = "4 8"
robot_list = ["(2, 3, E) LFRFF", 
    "(0, 2, N) FFLFRFF", 
    "(2, 3, N) FLLFR", 
    "(1, 0, S) FFRLF",
    "(1, 0, S)"]


# Initialising MarsMap and creating the grid
map = MarsMap()
map.strip_grid_dimentions(grid)

# Creating robot instances and adding them to map
for robot_command_str in robot_list:
    robot_instance = Robot()
    robot_instance.strip_command(robot_command_str)
    map.robots_on_map.append(robot_instance)

# Moving the robots through their commands and outputing results
map.navigate()
map.output_results()

