"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""
import sys, argparse, os
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

x_coords=[]
y_coords=[]

file= "Test.txt"

blocksCont=0
beehivesCont=0
blinkersCont=0
boatsCont=0
beaconsCont=0
glidersCont=0
lightWeightsCont=0
loafsCont=0
toadsCont=0
tubsCont=0
othersCont=0

if os.path.exists("Results.txt"):
  os.remove("Results.txt")

def paint(x,y,grid,newGrid):
    grid[x,y]=0
    newGrid[x,y]=255

def neighbors(grid, x, y,cont):
    if(grid[x+1,y]==255):cont+=1
    if(grid[x+1,y+1]==255):cont+=1
    if(grid[x+1,y-1]==255):cont+=1
    if(grid[x,y+1]==255):cont+=1
    if(grid[x,y-1]==255):cont+=1
    if(grid[x-1,y]==255):cont+=1
    if(grid[x-1,y-1]==255):cont+=1                    
    if(grid[x-1,y+1]==255):cont+=1

    return cont

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def addGlider(i, j, grid,name):
    """adds a glider with top left cell at (i, j)"""
    configuration = name
    x=configuration.shape[0]
    y=configuration.shape[1]
    grid[i:i+x, j:j+y] = configuration

def update(frameNum, img, grid, N, G):
    
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    
    global blocksCont
    global beehivesCont
    global blinkersCont
    global boatsCont
    global beaconsCont
    global glidersCont
    global lightWeightsCont
    global loafsCont
    global toadsCont
    global tubsCont
    global othersCont


    f = open("Results.txt", "a")
    alives=0
    deads=0
    newAlives=0
    for x in range (0,N):
        for y in range (0,N):
            if(grid[x,y]==255):
                alives+=1
    
    f.write("Generation: "+ str(frameNum) + "\n")
    f.write("Alives: "+ str(alives) + "\n")
       
    # TODO: Implement the rules of Conway's Game of Life

    blocks= 0
    beehives=0
    blinkers=0
    boats=0
    beacons=0
    gliders=0
    lightWeights=0
    loafs=0
    toads=0
    tubs=0
    others=0
    

    for x in range (0,N):
        for y in range (0,N):
            if (x-1 >= 0 and y-1 >= 0 and x+1 < N and y+1 < N):
                if(grid[x,y]==255):
                    #Any live cell with two or three neighbors survives.
                    cont=0
                    cont= neighbors(grid, x, y,cont)
                    if(cont ==2 or cont==3):newGrid[x,y]=255
                    #if(cont==0):others+=1

                    #All other live cells die in the next generation.
                    else:
                        newGrid[x,y]=0
                        deads+=1
                else:
                    #Any dead cell with three live neighbors becomes a live cell.
                    cont=0
                    cont= neighbors(grid, x, y,cont)

                    if(cont==3):
                        newGrid[x,y]=255
                        newAlives+=1

    for x in range (0,N):
        for y in range (0,N):
            if (x-1 >= 0 and y-1 >= 0 and x+1 < N and y+1 < N):
                if(grid[x,y]==255): 
                    cont=0
                    cont= neighbors(grid, x, y,cont)
                    if(cont>=1):                       
                        #Blocks
                        if (x+3 < N and y+3 < N and y-2 >= 0 and x-2 >= 0):
                            if((grid[x+1,y]==255 and grid[x+1,y+1]==255 and grid[x,y+1]==255) and (grid[x-1,y-1]==0 and grid[x-1,y]==0 and grid[x-1,y+1]==0 and grid[x-1,y+2]==0 and grid[x,y-1]==0 and grid[x,y+2]==0 and grid[x+1,y-1]==0 and grid[x+1,y+2]==0 and grid[x+2,y-1]==0 and grid[x+2,y]==0 and grid[x+2,y-1]==0 and grid[x+2,y+2]==0) ):
                                blocks+=1  
                                grid[x+1,y]=0
                                grid[x,y+1]=0   
                                grid[x+1,y+1]=0

                        if (x+3 < N and y+2 < N and y-2 >= 0):
                            #Toads
                            if((grid[x+1,y+1]==255 and grid[x+2,y+1]==255 and grid[x+3,y-1]==255 and grid[x+1,y-2]==255 and grid[x+2,y-2]==255 and (grid[x+1,y]==0 and grid[x+2,y]==0 and grid[x+1,y-1]==0 and grid[x+2,y-1]==0))): 
                                toads+=1   
                                grid[x+1,y+1]=0
                                grid[x+2,y+1]=0
                                grid[x+3,y-1]=0
                                grid[x+1,y-2]=0
                                grid[x+2,y-2]=0

                            elif((grid[x,y+1]==255 and grid[x,y+2]==255 and grid[x+1,y]==255 and grid[x+1,y+1]==255 and grid[x+1,y-1]==255)):
                                toads+=1   
                                grid[x,y+1]=0
                                grid[x,y+2]=0
                                grid[x+1,y]=0
                                grid[x+1,y+1]=0
                                grid[x+1,y-1]=0

                        if (x+3 < N and y+3 < N ):
                            #Loafs
                            if(grid[x,y+1]==255 and grid[x+1,y-1]==255  and grid[x+1,y+2]==255 and grid[x+2,y]==255 and grid[x+2,y+2]==255 and grid[x+3,y+1]==255 and (grid[x+1,y]==0 and grid[x+1,y+1]==0 and grid[x+2,y+1]==0)): 
                                loafs+=1
                                grid[x,y+1]=0 
                                grid[x+1,y-1]=0 
                                grid[x+1,y+2]=0 
                                grid[x+2,y]=0 
                                grid[x+2,y+2]=0 
                                grid[x+3,y+1]=0
                                
                            #Beacon
                            elif((grid[x+1,y]==255 and grid[x+1,y+1]==255 and grid[x,y+1]==255 and grid[x+2,y+2]==255 and grid[x+3,y+3]==255 and grid[x+3,y+2]==255 and grid[x+2,y+3]==255)):
                                beacons+=1 
                                grid[x+1,y]=0 
                                grid[x+1,y+1]=0 
                                grid[x,y+1]=0 
                                grid[x+2,y+2]=0 
                                grid[x+3,y+3]=0 
                                grid[x+3,y+2]=0 
                                grid[x+2,y+3]=0

                            elif(grid[x+1,y]==255 and grid[x,y+1]==255 and grid[x+2,y+3]==255 and grid[x+3,y+2]==255 and grid[x+3,y+3]==255):
                                beacons+=1
                                grid[x+1,y]=0 
                                grid[x,y+1]=0 
                                grid[x+2,y+3]=0 
                                grid[x+3,y+2]=0 
                                grid[x+3,y+3]=0

                            #Blinker
                            elif((grid[x,y+1]==255 and grid[x,y+2]==255 and ( grid[x-1,y-1]==0 and grid[x+1,y-1]==0 and grid[x-1,y+3]==0 and grid[x+1,y+3]==0 and grid[x-1,y+2]==0 and grid[x+1,y+2]==0 ))):
                                blinkers+=1
                                grid[x,y+1]=0 
                                grid[x,y+2]=0

                            elif((grid[x+1,y]==255 and grid[x+2,y]==255 and (grid[x+3,y+1]==0 and grid[x+3,y-1]==0 and grid[x-1,y-1]==0 and grid[x-1,y+1]==0 and grid[x+2,y-1]==0))):
                                blinkers+=1
                                grid[x+1,y]=0 
                                grid[x+2,y]=0

                        if (x+2 < N and y+2 < N):
                            #Beehives
                            if(grid[x,y+1]==255 and grid[x+1,y-1]==255  and grid[x+1,y+2]==255 and grid[x+2,y]==255 and grid[x+2,y+1]==255 and grid[x+1,y]==0 and grid[x+1,y+1]==0): 
                                beehives+=1 
                                grid[x,y+1]=0
                                grid[x+1,y-1]=0
                                grid[x+1,y+2]=0
                                grid[x+2,y]=0
                                grid[x+2,y+1]=0
            
                            #Boats
                            if(grid[x,y+1]==255 and grid[x+1,y]==255  and grid[x+1,y+2]==255 and grid[x+2,y+1]==255 and (grid[x,y-1]==0 and grid[x,y+2]==0 and grid[x-1,y-1]==0 and grid[x+2,y+2]==0 and grid[x+2,y]==0)): 
                                boats+=1 
                                grid[x,y+1]=0
                                grid[x+1,y]=0
                                grid[x+1,y+2]=0
                                grid[x+2,y+1]=0
                        
                        #Tubs
                        if (x+2 < N):
                            if(grid[x+1,y+1]==255 and grid[x+2,y]==255  and grid[x+1,y-1]==255 and (grid[x,y-1]==0 and  grid[x,y+1]==0 and grid[x+1,y]==0 and  grid[x+2,y-1]==0 and grid[x+2,y+1]==0)): 
                                tubs+=1 
                                grid[x+1,y+1]=0
                                grid[x+2,y]=0
                                grid[x+1,y-1]=0
                        #Gliders
                        if (x+2 < N and y+2 < N and y-2 >= 0):
                            if(grid[x+1,y+1]==255 and grid[x+2,y+1]==255  and grid[x+2,y]==255 and grid[x+2,y-1]==255 and (grid[x,y+1]==0)): 
                                gliders+=1 
                                grid[x+1,y+1]=0
                                grid[x+2,y+1]=0
                                grid[x+2,y]=0
                                grid[x+2,y-1]=0
                                

                            elif(grid[x,y+2]==255 and grid[x+1,y+1]==255  and grid[x+1,y+2]==255 and grid[x+2,y+1]==255 and (grid[x+1,y]==0)):
                                gliders+=1 
                                grid[x,y+2]=0
                                grid[x+1,y+1]=0
                                grid[x+1,y+2]=0
                                grid[x+2,y+1]=0

                            elif(grid[x+1,y]==255 and grid[x+2,y]==255  and grid[x+2,y-1]==255 and grid[x+1,y-2]==255 and (grid[x,y-1]==0)):
                                gliders+=1 
                                grid[x+1,y]=0
                                grid[x+2,y]=0
                                grid[x+2,y-1]=0
                                grid[x+1,y-2]=0
                                

                            elif(grid[x+1,y+1]==255 and grid[x+2,y+1]==255  and grid[x+2,y]==255 and grid[x+1,y+2]==255 and (grid[x,y+1]==0 and grid[x+1,y]==0)):
                                gliders+=1 
                                grid[x+1,y+1]=0
                                grid[x+2,y+1]=0
                                grid[x+2,y]=0
                                grid[x+1,y+2]=0

                        #Light Weight Spaceships
                        if (x+3 < N and y+4 < N and y-2 >= 0):
                            if(grid[x,y+1]==255 and grid[x+1,y+1]==255  and grid[x+1,y+2]==255 and grid[x+1,y-1]==255 and grid[x+1,y-2]==255 and grid[x+2,y-2]==255  and grid[x+2,y-1]==255 and grid[x+2,y]==255 and grid[x+2,y+1]==255  and grid[x+3,y-1]==255 and grid[x+3,y]==255): 
                                lightWeights+=1 
                                grid[x+1,y+1]=0
                                grid[x+1,y+2]=0
                                grid[x+1,y-1]=0
                                grid[x+1,y-2]=0
                                grid[x+2,y-2]=0
                                grid[x+2,y-1]=0
                                grid[x+2,y]=0
                                grid[x+2,y+1]=0
                                grid[x+3,y-1]=0
                                grid[x+3,y]=0

                            elif(grid[x,y+1]==255 and grid[x,y+2]==255  and grid[x,y+3]==255 and grid[x+1,y-1]==255 and grid[x+1,y+3]==255 and grid[x+3,y-1]==255  and grid[x+2,y+3]==255 and grid[x+3,y+2]==255): 
                                lightWeights+=1 
                                grid[x,y+1]=0
                                grid[x,y+2]=0
                                grid[x,y+3]=0
                                grid[x+1,y-1]=0
                                grid[x+1,y+3]=0
                                grid[x+3,y-1]=0
                                grid[x+2,y+3]=0
                                grid[x+3,y+2]=0

                            elif(grid[x,y+1]==255 and grid[x+1,y-1]==255  and grid[x+1,y]==255 and grid[x+1,y+1]==255 and grid[x+1,y+2]==255 and grid[x+2,y-1]==255  and grid[x+2,y]==255 and grid[x+2,y+2]==255 and grid[x+2,y+3]==255  and grid[x+3,y+1]==255 and grid[x+3,y+2]==255): 
                                lightWeights+=1 
                                grid[x,y+1]=0
                                grid[x+1,y-1]=0
                                grid[x+1,y]=0
                                grid[x+1,y+1]=0
                                grid[x+1,y+2]=0
                                grid[x+2,y-1]=0
                                grid[x+2,y]=0
                                grid[x+2,y+2]=0
                                grid[x+2,y+3]=0
                                grid[x+3,y+1]=0
                                grid[x+3,y+2]=0
                        else:
                            others+=1
                  
                    else:
                        #Light Weight Spaceships
                        if (x+3 < N and y+4 < N ):
                            if(grid[x,y+3]==255 and grid[x+1,y+4]==255  and grid[x+2,y+4]==255 and grid[x+3,y+4]==255 and grid[x+2,y]==255 and grid[x+3,y+1]==255  and grid[x+3,y+2]==255 and grid[x+3,y+3]==255): 
                                lightWeights+=1 
                                grid[x,y+3]=0
                                grid[x+1,y+4]=0
                                grid[x+2,y+4]=0
                                grid[x+3,y+4]=0
                                grid[x+2,y]=0
                                grid[x+3,y+1]=0
                                grid[x+3,y+2]=0
                                grid[x+3,y+3]=0
                            else:
                                others+=1       
               
    
    # update data
    f.write("New Alives: "+ str(newAlives) + "\n")
    f.write("Deads: "+ str(deads) + "\n")
    f.write("********AMOUNT OF CONFIGURATIONS********\n")
    f.write("Blocks:" + str(blocks) + "\n")
    f.write("Behives:" + str(beehives) + "\n")
    f.write("Loafs:" + str(loafs) + "\n")
    f.write("Boats:" + str(boats) + "\n")
    f.write("Tubs:" + str(tubs) + "\n")
    f.write("Blinkers:" + str(blinkers) + "\n")
    f.write("Toads:" + str(toads) + "\n")
    f.write("Beacons:" + str(beacons) + "\n")
    f.write("Gliders:" + str(gliders) + "\n")
    f.write("Light-weight Spaceships:" + str(lightWeights) + "\n")
    f.write("Others:" + str(others) + "\n")
    f.write("---------------------------------------\n\n")
    

    blocksCont+=blocks
    beehivesCont+=beehives
    blinkersCont+=blinkers
    boatsCont+=boats
    beaconsCont+=beacons
    glidersCont+=gliders
    lightWeightsCont+=lightWeights
    loafsCont+=loafs
    toadsCont+=toads
    tubsCont+=tubs
    othersCont+=others

    
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    
    if (frameNum==G-1):
        total= blocksCont + beaconsCont + beehivesCont + blinkersCont + boatsCont + glidersCont + lightWeightsCont + loafsCont + toadsCont + tubsCont + othersCont
        f.write("***********PERCENTAGE***********\n")
        f.write("Blocks:" + str(round(blocksCont/total*100,2)) + "%\n")
        f.write("Beehives:" + str(round(beehivesCont/total*100,2)) + "%\n")
        f.write("Loafs:" + str(round(loafsCont/total*100,2)) + "%\n")
        f.write("Boats:" + str(round(boatsCont/total*100,2)) + "%\n")
        f.write("Tubs:" + str(round(tubsCont/total*100,2)) + "%\n")
        f.write("Blinkers:" + str(round(blinkersCont/total*100,2)) + "%\n")
        f.write("Toads:" + str(round(toadsCont/total*100,2)) + "%\n")
        f.write("Beacons:" + str(round(beaconsCont/total*100,2)) + "%\n")        
        f.write("Gliders:" + str(round(glidersCont/total*100,2)) + "%\n")
        f.write("Light-weight Spaceships:" + str(round(lightWeightsCont/total*100,2)) + "%\n")       
        f.write("Others:" + str(round(othersCont/total*100,2)) + "%\n")
        f.close()
        os.startfile("Results.txt")
        exit()
    return img,

# main() function
def main():    
    
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments


    grid = np.array([])
    try:
        f = open(file, "r")
        
        count = len(f.readlines())
    
        f = open(file, "r")
        for x in range (0,count):
            if x == 0:
                size= f.readline().split()
                N=int(size[0])
                G=int(size[1])
                grid = np.zeros(N*N).reshape(N, N)
            else:
                coords= f.readline().split()
                x=int(coords[1])
                y=int(coords[0])
                    
                if (x<N and y<N):
                    x_coords.append(x)
                    y_coords.append(y)
                else:
                    print ("Coordinate values out of the Grid size")
                    exit()

        for x in range (0, count-1):
            grid[x_coords[x],y_coords[x]] =255
    except:
        print("The must be an error on your format file, please try again")
        exit()

    # set grid size
    
    #G=20
    #N=100
        
    # set animation update interval
    updateInterval = 500

    # declare grid
    
    # populate grid with random on/off - more off than on
    #grid = randomGrid(N)
    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(N*N).reshape(N, N)
    #addGlider(2, 2, grid,blinker)

    
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, G),
                                  frames = G,
                                  interval=updateInterval,
                                  save_count=50)

    plt.show()

# call main
if __name__ == '__main__':
    main()