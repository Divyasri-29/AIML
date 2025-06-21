import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('spotify-2023.csv','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')

    for row in plots:
        x.append(row[0])
        y.append(row[1])
plt.bar(x,y,color='pink',width=0.72)
plt.scatter(x,y,color='deepskyblue',marker='*')
plt.xlabel('Danceability',c='purple')
plt.ylabel('Energy',c='purple')
plt.title('Energy required to dance',c='purple')
plt.savefig(r'C:\Users\Divyasri\Desktop\AIML\g2.png')
plt.show()
