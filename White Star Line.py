import matplotlib.pyplot
import matplotlib
import numpy as np
import tkinter as tk
matplotlib.use('TkAgg')
from tkinter import * 


# Set the coordinate size
fig = matplotlib.pyplot.figure(figsize=(10, 10))
ax = fig.add_axes([0.1, 0.1, 0.8,0.8])

# Menu, menu elements
root = tk.Tk()
root.geometry('700x700')
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
model_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
root.title("Iceberg")

#Creating labels, showing the result of mass of each iceburg.
Iceburg=Label(root,text = 'The following iceberg are listed from left to right, top to bottom: iceberg1, iceberg2, iceburg3, iceberg4 and iceberg5',width=100, height=5, background = 'black', fg='white')
Iceburg.place(x=70,y=90)
Iceburg.pack(ipadx=20,ipady=30)
mass_d=tk.Label(root, text='iceberg1 is undragable,  iceberg3 is undragable，  iceberg4 is undragable，  iceberg5 is undragable',bg='white',font=('Arial',10),width=100,height=5, fg='red')
mass_d.place(x=70,y=90)
mass_d.pack()
mass_ud=tk.Label(root, text='iceberg2 is dragable',bg='white',font=('Arial',10),width=100,height=5, fg='green')
mass_ud.place(x=70,y=90)
mass_ud.pack()
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



#initializing
Ice=[]# the lidar data with identified ice
Ice_volume=[]# volume 
Ice_mass=[]# mass
lidar=[] # lidar data
radar=[] # radar data

#read the data in the radar file, Using numpy to read it as a 300*300 array
radar=np.loadtxt(open("radar.txt","rb"),delimiter=",",skiprows=0)
# filter the ice
radar[radar<100]=0.0
radar[radar>=100]=1.0
"""
The radar file is used to identify ice with value > 100
set all the value < 100 to 0 and value >=100 to 1, 
in this way all the iceburg can be identified with value 1
"""
# TEST WHETHER RADAR FILE CAN BE SUCCESSFULLY READ AND PLOT
#print(radar)
#matplotlib.pyplot.imshow(radar)
#matplotlib.pyplot.show()


#read the data in the lidar file
lidar=np.loadtxt(open("lidar.txt","rb"),delimiter=",",skiprows=0)
# TEST WHETHER LIDAR FILE CAN BE SUCCESSFULLY READ AND PLOT
#print(lidar)
#matplotlib.pyplot.imshow(lidar)
#matplotlib.pyplot.show()

Ice.append(np.multiply(radar, lidar))
"""
Use lidar to multiply modified radar to filter out those are not ice in lidar
"""
# TEST WHETHER Ice IS CREATED SUCCESSFULLY
#print(Ice)

Ice_volume=np.array(Ice)
Ice_volume=Ice_volume.reshape(300,300)
"""
The volume above water equals Ice value *1*1
Due to lidar multiply modified radar becomes a 1 size list, it has to be transfered to 
300*300 array for calculating mass and plot
"""
# TEST WHETEHR Ice_volume IS CREATED AND PLOT SUCCESSFULLY
#print(Ice_volume)
#matplotlib.pyplot.imshow(Ice_volume)
#matplotlib.pyplot.show()



Ice_mass=Ice_volume*0.1*900*10
"""
The mass = volume * density, due to 10 units equals a metre of height, and 10 percent 
of its mass is above water, so the total mass of ice = ice_volume*0.1*900*10
"""
# Test whether mass is successfully created and plot
#print(Ice_mass)
#matplotlib.pyplot.imshow(Ice_mass)
#matplotlib.pyplot.show()



"""
The calculation above derived the total ice mass, but there are 5 iceburgs.
To derive the mass of each iceburg, several value thresholds were set to isolate each
iceburg using Ice_mass list. For example the iceburg1, the ice value is from 94500-96300, 
so set the treshold to pick the value up and sum them to get total mass of iceburg1. The 
mass of the 5 iceburgs are calculated below:
"""
iceburg1=Ice_mass[(Ice_mass > 94499) & (Ice_mass < 96301)]
iceburg1_mass=iceburg1.sum()
# Test whether iceburg1 calculate successfully
#print(iceburg1_mass)



iceburg2=Ice_mass[(Ice_mass > 228599) & (Ice_mass < 229501)]
iceburg2_mass=iceburg2.sum()
# Test whether iceburg2 calculate successfully
#print(iceburg2_mass)



iceburg3=Ice_mass[(Ice_mass > 134999) & (Ice_mass < 135901)]
iceburg3_mass=iceburg3.sum()
# Test whether iceburg3 calculate successfully
#print(iceburg3_mass)


iceburg4=Ice_mass[(Ice_mass > 201599) & (Ice_mass < 202501)]
iceburg4_mass=iceburg4.sum()
# Test whether iceburg4 calculate successfully
#print(iceburg4_mass)


iceburg5=Ice_mass[(Ice_mass > 91799) & (Ice_mass < 93601)]
iceburg5_mass=iceburg5.sum()
# Test whether iceburg5 calculate successfully
#print(iceburg5_mass)



def dragable(icemass):
    """
    If the iceburg mass is bigger than 36000000 then it is unable to drag, 
    create this function to check whether the 5 iceburgs can be dragged

    Parameters
    ----------
    icemass : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    if icemass < 36000000:
        print(f"{icemass} < 36000000 is dragable")
    else:
        print(f"{icemass} > 36000000 is too heavy to drag")





# function to plot the volume, mass and check 
def run():
    
    matplotlib.pyplot.imshow(Ice_volume)    
    matplotlib.pyplot.imshow(Ice_mass)
    dragable(iceburg1_mass)
    dragable(iceburg2_mass)
    dragable(iceburg3_mass)
    dragable(iceburg4_mass)
    dragable(iceburg5_mass)
 
   
    canvas.draw()


# command set
model_menu.add_command(label="Show", command=run)   
root.mainloop()     















