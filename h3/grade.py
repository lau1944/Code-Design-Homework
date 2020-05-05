import pandas as pd
import matplotlib.pyplot as plt

path = 'grade.csv'

file = pd.read_csv('grade.csv')
courses = ["Chinese", "English", "Math"]

def draw() :
    # set data set to plot
    to_plot=[file.Chinese, file.English, file.Math]
    fig=plt.figure(1,figsize=(9,6))
    ax=fig.add_subplot(111)
    ax.set_xticklabels(['Chinese', 'English', 'Math'])
    plt.title('Box Scores')
    plt.xlabel('courses')
    bp=ax.boxplot(to_plot)
    fig.savefig('peek.png',bbox_inches='tight')
    plt.show()

def main() :
    draw()


if __name__ == "__main__":
    main()