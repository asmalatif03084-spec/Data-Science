import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x=np.array([2023,2024,2025,2026])
y=np.array([15,25,30,20])
y1=np.array([17,23,45,7])
y2=np.array([23,89,66,7])
line_style=dict(marker=".",markersize=30,markerfacecolor="red",
         markeredgecolor="black",linestyle="dashed",
         linewidth=3)
# #basic plot
plt.plot(x,y,marker=".",markersize=30,markerfacecolor="red",
         markeredgecolor="black",linestyle="dashed",
         linewidth=3,color="red")
#plt.plot(y)
plt.plot(x,y1,color="#1c5bfc",**line_style)
plt.plot(x,y2,color="#1cfc45",**line_style)


# #LABELS
x1=np.array([2023,2024,2025,2026])
y1=np.array([15,25,30,20])
y3=np.array([17,23,45,7])
y4=np.array([23,89,66,7])

plt.title("class size",fontsize=20,family="Arial",fontweight="bold",
          color="red")

plt.xlabel("year",fontsize=20,family="Arial",color="blue",
           fontweight="bold")
plt.ylabel("Students",fontsize=20,family="Arial",color="blue",
           fontweight="bold")
plt.tick_params(axis="both",colors="blue")
plt.plot(x1,y1)
plt.plot(x1,y3)
plt.plot(x1,y4)


#grid line
x=[1,2,3,4]
y=[5,10,15,66]
plt.plot(x,y)
plt.grid(axis="both",linewidth=2,color="lightgray",linestyle="dashed")

#bar chart
categories=np.array(["fruit","grain","vegetable","protein","sweet"])
values=np.array([5,10,4,7,1])
plt.bar(categories,values)
plt.title("daily consumption")
plt.xlabel("food")
plt.ylabel("values")

#cicular bar chart

categories=np.array(["freshmen","sophomores","juniors","seniors"])
values=np.array([300,250,275,225])
colors=["blue","red","green","yellow"]
plt.pie(values,labels=categories,autopct="%1.1f%%",colors=colors,
        explode=[0.1,0,0,0],shadow=True,startangle=90)
plt.title("pie chart")

#scatter graph

x=np.array([0,1,1,2,3,4,5,6,7,7,8])#hour studied
y=np.array([55,60,65,62,68,70,75,78,82,85,87])#grade

x1=np.array([0,1,1,5,3,4,6,6,8,7,8])#hour studied
y1=np.array([55,60,65,62,98,70,75,78,522,85,88])#grade

plt.scatter(x,y,color="skyblue",alpha=0.75,s=150,label="classA")
plt.scatter(x1,y1,color="red",alpha=0.5,s=200,label="classB")
plt.xlabel("hours studied")
plt.ylabel("grade")
plt.title("Test score")
plt.legend()



#histogram
scores=np.random.normal(loc=80,scale=10,size=100)
scores=np.clip(scores,0,100)
plt.hist(scores,bins=10,color="lightgreen",edgecolor="black")
plt.title("Exam score")
plt.xlabel("score")
plt.ylabel("No of student")


#subplots
x=np.array([1,2,3,4,5])

figure,axes=plt.subplots(2,2)
axes[0,0].plot(x,x*2,color="red")
axes[0,0].set_title("x*2")

axes[0,1].plot(x,x**2,color="blue")
axes[0,1].set_title("x**2")

axes[1,0].plot(x,x**3,color="green")
axes[1,0].set_title("x**3")

axes[1,1].plot(x,x**4,color="purple")
axes[1,1].set_title("x**4")

plt.tight_layout()



#matplotlib+pandas
df=pd.read_csv("record.csv")
type_count=(df["Name"].value_counts())
plt.barh(type_count.index,type_count.values,color="yellow",
         edgecolor="black")

plt.title("student record")
plt.ylabel("name")

plt.show()

