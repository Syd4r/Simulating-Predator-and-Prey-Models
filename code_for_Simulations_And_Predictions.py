import numpy as np
import random
import matplotlib.pyplot as plt

# define the size of the grid
GRID_SIZE = 20

# initialize the grid with random predator and prey cells
grid = np.random.randint(0, 3, (GRID_SIZE, GRID_SIZE))

#All customizable variables
PRED_DIE = random.random()
PRED_REP = random.random()
PRED_REP_2 = random.random()
PREY_REP = random.random()
PREY_SPAWN = random.randint(0,10)/100

#Uncomment these variables for the best simulation
PRED_DIE = 1
PRED_REP = 0.5
PRED_REP_2 = 0.2
PREY_REP = 0.4
PREY_SPAWN = 0.001

''''
PRED_DIE = 0.7
PRED_REP = 0.97
PRED_REP_2 = 0.15
PREY_REP = 0.45
PREY_SPAWN = 0.06
'''
print(PRED_DIE)
print(PRED_REP)
print(PRED_REP_2)
print(PREY_REP)
print(PREY_SPAWN)

predator_counts = []
prey_counts = []
tot_counts = []
counts_label = []
# define the rules for how the cells interact
def update_grid(grid):
    # create a copy of the grid to update
    new_grid = grid.copy()
    pred_count = 0
    prey_count = 0
    # loop over the cells in the grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # check if the current cell is a predator
            if grid[i, j] == 1:
                pred_count += 1
                # check if there is a prey cell adjacent to the predator
                prey_found = False
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # make sure we're not checking the current cell
                        if (x != i and y != j) and x >= 0 and x < GRID_SIZE and y >= 0 and y < GRID_SIZE:
                            if grid[x, y] == 2:
                                # if there is prey adjacent to the predator, the predator survives
                                prey_found = True
                                if random.random() < PRED_REP:
                                    new_grid[x,y] = 1
                                else:
                                    new_grid[x,y] = 0
                                break
                            
                # if the predator did not find any prey, it dies
                if not prey_found and random.random() < PRED_DIE:
                    new_grid[i, j] = 0
            
            # check if the current cell is prey
            elif grid[i, j] == 0:
                if random.random() < PREY_SPAWN:
                    new_grid[i,j] = 2
                # check if there is another prey cell adjacent to the current prey cell
                adjacent_prey_count = 0
                adjacent_pred_count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # make sure we're not checking the current cell
                        if (x != i or y != j) and x >= 0 and x < GRID_SIZE and y >= 0 and y < GRID_SIZE:
                            if grid[x, y] == 2:
                                # if there is another prey cell adjacent, increment the count
                                adjacent_prey_count += 1
                            if grid[x,y] == 1:
                                adjacent_pred_count += 1
                
                # if there are two or more adjacent prey cells, the current prey cell reproduces
                rand = random.randint(0,adjacent_prey_count + adjacent_prey_count)
                if rand < adjacent_prey_count:
                    if adjacent_prey_count >= 2 and random.random() < PREY_REP: 
                        new_grid[i, j] = 2
                else:
                    if adjacent_pred_count >= 1 and random.random() < PRED_REP_2: 
                        new_grid[i, j] = 1
            else:
                prey_count += 1
    # return the updated grid
    return new_grid,pred_count,prey_count

# run the simulation for 100 steps
for i in range(200):
    # update the grid according to the rules
    grid,num_pred,num_prey = update_grid(grid)
    predator_counts.append(num_pred)
    prey_counts.append(num_prey)
    tot_counts.append(num_pred+num_prey)
    counts_label.append(i+1)
#plt.plot(predator_counts, label="Predators")
#plt.plot(prey_counts, label="Prey")
#plt.plot(tot_counts, label="Total Pop.")
#plt.xlabel("Generation")
#plt.ylabel("Population")
#plt.legend()
#plt.show()

fig, ax = plt.subplots()

ax.bar(counts_label,tot_counts,1, label='Predators')
ax.bar(counts_label,prey_counts,1, label="Prey")


ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()