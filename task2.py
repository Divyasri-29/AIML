import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('spotify2.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[1]))
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Weather Data")
  
plt.xticks(rotation = 25)
plt.xlabel('Year')
plt.ylabel('BPM')
plt.title('Weather Report', fontsize = 20)
plt.grid()
plt.show()
