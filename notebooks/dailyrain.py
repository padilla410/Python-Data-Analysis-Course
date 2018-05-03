#Import modules
import matplotlib.pyplot as plt
import pandas as pd


#Import data
df = pd.read_excel("Output_data/df_daily.xlsx",index_col=0)


#step 1. Create a figure. A figure is a single page with 1 or more plots on it.
fig = plt.figure(figsize=(11,8))

#step 2. Create an axis. This is a single "plot". 
#The 111 is a short cut for a page layout. 1 plot vertically on page, 1 plot horizontally on page, and this is the first one.
ax = fig.add_subplot(1,1,1)

#step 3. Draw your plot. Basic function is plot(xdata,ydata,...other optional parameters)
x = df.index
y1 = df["Precip_in"]
y2 = df["precip_cm"]

l1 = ax.plot(x,y1)

#step 4. Personalize it!
ax.set_title("Daily Rainfall at DCA")
ax.set_ylabel("Date")
ax.set_xlabel("Rainfall, in")
ax.grid()

plt.tight_layout()  #Makes the plot fill the page and fix spacing

plt.show()

#plt.savefig("Output_data/dailyrain.png",dpi=600)