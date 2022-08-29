# MarsRover
Candidate take home test

## Problem Statement
Write a program that takes in commands and moves one or more robots around Mars.
* The world should be modelled as a grid with size m x n
* Your program should read the input, update the robots, and print out the final states
of the robots
* Each robot has a position (x, y), and an orientation (N, E, S, W)
* Each robot can move forward one space (F), rotate left by 90 degrees (L), or rotate
right by 90 degrees (R)
* If a robot moves off the grid, it is marked as ‘lost’ and its last valid grid position and
orientation is recorded
* Goingfromx->x+1isintheeasterlydirection,andy->y+1isinthenortherly
direction. i.e. (0, 0) represents the south-west corner of the grid

The input takes the form:
``` 
4 8
(2, 3, E) LFRFF 
(0, 2, N) FFLFRFF
```

 The first line of the input ‘4 8’ specifies the size of the grid. The subsequent lines each represent the initial state and commands for a single robot. (0, 2, N) specifies the initial state of the form (x, y, orientation). FFLFRFF represents the sequence of movement commands for the robot.
 
The output should take the form:
```
(4, 4, E)
(0, 4, W) LOST
```
Each line represents the final position and orientation of the robots of the form (x, y, orientation) and optionally whether the robot was lost.

Another example for the input:
``` 
4 8
(2, 3, N) FLLFR 
(1, 0, S) FFRLF
```
The output would be:
```
(2, 3, W)
(1, 0, S) LOST
```

# Approach 
The approach for this problem was fairly simple. Given the problem itself, I breifly concidered other data structures that would be appropriote but based on the data I didn't concider any of them of benefit. As for algorithms, again fairly simple, I did touch on different types of algorithms that could be applied in the "Potential Development" section

I went with an object based approach as a clean way to solve the problem. This allows for easier testing and code can be built in a more modular connected way rather than simply having some arrays to store data with a few functions. 

## Usage
At the bottom of the script are the inputs, two variables ```grid``` and ```robot_list```, you can modify the input easily by pasting in your grid size and robot locations + command list

To call the script, ensure you have python installed on your machine or find an online python runner and paste the contents of the script in there. If you're running the script locally, either run it from your IDE or open up your terminal and enter ```python mars_rover.py```.
Note: Please ensure when you do this your current path is within the MarsRover repo.

## Robot class
Formats the input string and seperates out the nessisary data for current location, direction and command list as well as whether or not the robot is lost

## MarsMap class
This is a class which handles the navigation of the robots with an output function to display the results. It also stores a list of robots. There is a reference to a `grid` here which lays the foundation for further developments as mentioned in "Potential Development". Under normal circumstances, I wouldn't leave in code that was unused.

# Notable Comments 
The way that i decided to accept input was in the script, this was a concious decision as there were a few options but based on the review I chose this one. 

### CSV file
Allow for the acceptance of a CSV file which has this information inside but I felt that may be kind of clunky and during the review you may likely wish to change the data repeatedly, as such this would stem the flow during the review process.

### User input 
This would be to use the python ```input``` functionality which would effectively if the program accepting multiple robots require an infinite menu where I would have to ask if you want to add another robot until you don't and you would enter "N" which would run the program

### Command line arguments
This is absolutely just showing off but you could do it, it's just a clunky way of calling the script as if you want to call the script with command line arguments, if robot_command1 represents the first robot command then you would call the script as follows 
```
$prompt$ python mars_rover.py '4 8' robot_command1 robot_command2 robot_command3 robot_command4
```



# Potential Development 

# If I had more time 
### Testing
The first thing I'd do is to use Pytest or whichever testing library / framework the team was using to cover the test cases and edge case for regression. Philosophy on testing is that tests should be as small and simple as possible testing every divergence of code in your codebase. 

### User expirience
I would have probably built two solutions, one that conforms to the spec and the other that goes beyond the spec. The beyond the spec version would be to follow more of a game design. I would gracefully accept the users mistakes and print messages to the menu rather than raising exceptions on data entry.

I'd also make it such that you could enter these robots and then all at once make them move 
This also poses challanges whereby you would have to build in crash acceptance / avoidance 
Creating a GUI to represent the map + the robots moving through the map 

### add_hill function
The idea behind the hill is that 
the mars rover robots could have to collect things. By placing hills in the map 
you could build in rules such that the robots can overcome a hill if theyre not 
carrying anything but not if they are.

### add_crator function 
The idea behind the crators would be that some robots wouldnt get lost they would crash and fall down into a crator, there are a few ways you could go with this like the crators just cause a crash or a list of commands provided result in the robot going into a crator so they have to avoid it using a path finding algorithm mixed in with trying to avoid robots on their journey

That side of things presents interesting avenues for the program to evole such as right-of-way 
robots carrying things take presidence, then avoiding crators then robots just on their normal journey
