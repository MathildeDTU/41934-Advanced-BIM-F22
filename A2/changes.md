The script has been edited to help give the user a quick overview of the materials on each level in the building.
Here, the materials used for the beams and slabs has been set up as a list. This list is then displayed when the user selects a level of their choice.
Below this is some overall information about the building; the gross floor area, as well as the number of beams, -slabs and -floors, and the elevation of the building site.

In the function writeCustomHTML, which is 

screenshot

We have added some additional inputs to writeCustomHTML to display this overall




Following an example to extract the information about the materials used in the floor:

![a](https://user-images.githubusercontent.com/112398682/196029496-d110471b-bea0-4b34-8db6-6904ece0b35e.jpg)

This is loaded into the visualization through a variable "floor_entities", for the function "classifyFloors".
  

Further work will include the volume of insulation used on each level, based on the wall areas and the thicknesses expressed in the wall composition. 
As of now, the displayed material list is the 'total' material list, which might be due to a problem with indices. However, the the goal was to get the list of materials for the respective level.
