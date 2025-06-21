import matplotlib.pyplot as plt
a=[1,2,3,4]
b=[5,6,3,8]
plt.plot(a,b,c='pink',linestyle='dashed',linewidth=2)
plt.scatter(a,b,c='purple',marker='*')
#plt.barh(a,b,color='lavender')
plt.title('sample graph',c='green')
plt.xlabel('x-axis',c='green')
plt.ylabel('y-axis',c='green')
plt.savefig(r'C:\Users\Divyasri\Desktop\AIML\g1.png')
plt.show() # this would be the last line.
