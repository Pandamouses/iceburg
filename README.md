# White Star Line Model
<img class='nolazy' style='float:right;' src="Skaven4.png" width="500" height="250" />

#### By Yuming Zhang
<br>

## 1. Introduction
>> This model aims to help shipping companies with iceberg-towing tug business. The model identifies ice in the study area, filters out icebergs, calculates the mass of each iceberg, and shows it in the window.


## 2. Content
>> The model source code contains in [White Star Line.py](White Star Line.py). The model was designed in the following steps: 1. Get the lidar and radar data and store them as txt file; 2. Read lidar and radar file; 3. Identify ice using radar file; 4. filter out the none ice area in lidar using radar; 5. Calculate volume and mass of total ice; 6. calculate indivisual mass of iceburg using total ice mass; 7. Check whether each iceberg could be draged; 8. Pull the result to the GUI.

## 3. How it works
>> Download White Star Line.py, [lidar.txt](lidar.txt) and [radar.txt](radar.txt). Open it in Spyder and directly run it, the display window will pop up, then click `model` under the menu bar and click`show`. The 5 icebergs within a 300`*`300 background will be displayed. The mass of each iceberg will be printed under the console.

## 4. Test
>> The model is fully tested, and all the lists can be successfully printed and plotted. But the model is unstable and the console might crash. The tests were commented out in the source code.

## 5. Limitations
>> The model contains limitations. The desired final output was to create an interactive window, each iceberg should be separated from the background, and users can drag the iceberg to check whether the mass is small enough to drag. However, due to a lack of skills, the result was shown in the window as labels. The iceberg  filter part used the mass value as a threshold, the best way could be to use matrix coordinates to identify each iceberg. The limitations could be improved in the further development



## 6. License
>> [MIT © Yuming Zhang](LICENSE)
