import random
import numpy as np
import matplotlib.pyplot as plt

attr = []
sum_num = 0
def generate_random(num):
    while(len(attr) < num):
        global sum_num 
        ram_num = random.randrange(0, num + 1, 1)
        sum_num += ram_num
        attr.append(ram_num)

def mean(list):
    return np.mean(list)

def std(list):
    return np.std(list, ddof=1)

def countUp(list, avg):
    return sum(i > avg for i in list)      

def countDown(list, avg):
    return sum(i < avg for i in list)

def draw(list):
    plt.figure(figsize=[10,5])
    n, bins, patches = plt.hist(x=list, bins=10, color='#0504aa',alpha=0.7, rwidth=0.65)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value',fontsize=15)
    plt.ylabel('Number',fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title('Diagram',fontsize=15)
    plt.show()

if __name__ == "__main__":
    generate_random(100)
    mean = mean(attr)
    std = std(attr)
    print("Total : " + str(sum_num) + "\n" + "Average : " + str(mean) + "\n"
        + "Standard deviation : " + str(std) + "\n" + "Above mean : " + str(countUp(attr, mean)) + "\n"
        + "Below mean : " + str(countDown(attr, mean)))
    draw(attr)