
## Importing dependencies
from random import randint as rnd
from random import shuffle
## Setting the problem and algorithm parameters
N=7
MAX_WEIGHT=13
objects=[(10,2),(5,3),(15,5),(7,7),(6,1),(18,4),(3,1)]
#objects=None
POPULATION_SIZE=200
MUTATION_RATE=0.8
EPOCH=200
## Item Class
class Item:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
## Item Getter Function
def get_items(n,input_items=None,verbos=0):
    items=[]
    if input_items==None:
        for i in range(n):
            print(f"Items #{i+1}")
            item_profit=int(input("please enter the profit of the item: "))
            item_weight=int(input("please enter the weight of the item: "))
            items.append(Item(item_profit,item_weight))
        print("#############################")
    else:
        for item in input_items:
            items.append(Item(item[0],item[1]))
    if verbos:
        for item in items:
            print(f"Item #{items.index(item)+1}: profit:{item.profit} weight:{item.weight}")
    return items
## Init population function
def init_population(n,p):
    population_list=[]
    for i in range (p):
        new_memeber=[0 for i in range(n)] + [1 for i in range(n)]
        shuffle(new_memeber)
        new_memeber=new_memeber[:n]+[None,None]
        population_list.append(new_memeber)
    return population_list
## Cross over function
def cross_over(population_list,n,p):
    n_b2=n//2
    for i in range(0,p,2):
        child1=population_list[i][:n_b2] + population_list[i+1][n_b2:n] + [None,None]
        child2=population_list[i+1][:n_b2] + population_list[i][n_b2:n] + [None,None]
        population_list.append(child1)
        population_list.append(child2)
    return population_list
## Mutation Function
def mutation(population_list,n,p,m):
    choosen_ones=[i for i in range(p,p*2)]
    shuffle(choosen_ones)
    choosen_ones=choosen_ones[:int(((p*2)-1)*m)]
    for i in choosen_ones:
        cell=rnd(0,n-1)
        population_list[i][cell] = 1 if population_list[i][cell]==0 else 0
    return population_list
## Fitness
def weight_distance(bag,n,max_weight,items_list):
    total_weight=0
    for i in range(n):
        if bag[i]:
            total_weight+=items_list[i].weight
    return abs(max_weight-total_weight) if total_weight<=max_weight else 200
def profit(bag,n,items_list):
    total_profit=0
    for i in range(n):
        if bag[i]:
            total_profit+=items_list[i].profit
    return total_profit
def fitness(population_list,n,p,items_list,max_weight):
    for i in range(p*2):
        population_list[i][n] = weight_distance(population_list[i],n,max_weight,items_list)
        population_list[i][n+1]=profit(population_list[i],n,items_list)
    return population_list
## Sorter Function
def sorter(population_list,index1,index2):
    sorted_list=sorted(population_list,key=lambda x: (x[index1],-x[index2]))
    return sorted_list
## Main 
if __name__=="__main__":
    print(f"MAX WEIGHT is {MAX_WEIGHT}")
    print("$$$$$$$$$$$$$$$$$$$$")
    items=get_items(N,input_items=objects,verbos=0)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    current_population=init_population(N,POPULATION_SIZE)
    while EPOCH:
        current_population=cross_over(current_population,N,POPULATION_SIZE)
        current_population=mutation(current_population,N,POPULATION_SIZE,MUTATION_RATE)
        current_population=fitness(current_population,N,POPULATION_SIZE,items,MAX_WEIGHT)
        current_population=sorter(current_population,N,N+1)
        current_population=current_population[:POPULATION_SIZE]
        current_population=sorted(current_population,key=lambda x: -x[N+1])
        EPOCH-=1
        
        #break
    else:
        print("Best found solution:", current_population[0])
        
