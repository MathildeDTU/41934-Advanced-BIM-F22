# Changes
The script has been edited to help give the user a quick overview of the materials on each level in the building.
Here, the materials used for the beams and slabs has been set up as a list. This list is then displayed when the user selects a level of their choice.
Below this is some overall information about the building; the gross floor area, as well as the number of beams, -slabs and -floors, and the elevation of the building site.

In the function writeCustomHTML, which is written in the  HTMLbuild.py file, we've added three "custom"s. For example for the gross floor area:
![MicrosoftTeams-image](https://user-images.githubusercontent.com/112400501/196029934-f096567f-425c-4a06-8c54-57f3b3392452.png)

These "custom"s is used in the html-build.js file as shown below:
![MicrosoftTeams-image (1)](https://user-images.githubusercontent.com/112400501/196029974-a8ef0bde-8954-4450-8cb8-0dc6dd26ceef.png)


Following an example to extract the information about the materials in beams and slabs used in each level:
![a](https://user-images.githubusercontent.com/112398682/196029496-d110471b-bea0-4b34-8db6-6904ece0b35e.jpg)

This is loaded into the visualization through the variable "floor_entities", in the function "classifyFloors".

In the html-build.css file we've changes the height and width of the text box, to fit the list of materials.

# Future work 
Further work will include expanding the list of materials and link amounts to each material, which is necessary for an LCA. For insulation the volume used on each level, could be based on the wall areas and the thicknesses expressed in the wall composition. 
As of now, the displayed material list is the 'total' material list, which might be due to a problem with indices or the placement of the empty list in the for loop. However, the the goal was to get the list of materials for the respective level.
