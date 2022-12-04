# Final Project Reflection Report 
A general problem for all three "LCA/materials" groups was that the tools are developed for the specific IFC file. Therefore, a future step for all groups were to generalize the tools. That is, to function as more general applicable tools for other IFC models. Another interesting idea, that we talked about between the groups, was to have workshops within the same topic to discuss difficulties. In that connection, we reached the conclusion that we have had many of the same problems. The workshops could help overcome these problems and create a more effective workflow. What was clear from the feedback was that our tool was meant to be used before the other "LCA/materials" groups, to check if the IFC file has sufficient data to perform an LCA. 

For future use cases regarding LCA, connecting product specific EPDs to JSON would be of great interest. This would work close together with being able to easily extract quantities of different materials from the IFC files and then automatically import it into LCAbyg through JSON files. The last summative step would be to create a great user interface where the LCA results are automatically being updated, when the IFC files updates. 

Throughout the project, the main workflow was to combine the concept of what needed to be extracted and what was available in the model. For this, the IFC structure was explored through the visualized Excel-version and then rewritten in Python-code. After some iterations with the code, it was compared with the information available through Blender. This workflow did work well, albeit slow, but for future projects we'd start out by learning and utilizing the IFC structure (through flowcharts and websites), and then Blender moreso than Excel before coding. We believe that this code and concept is a good stepping stone for others to understand and continue the work for extracting material data for an LCA, and later importing them into JSON files. As we have discussed with the other "LCA/Materials" groups, this tool was handy and easily usable to extract the needed data. 

##  The process of creating/developing the tool
In relation to IFC-files, we have learned a lot about the structure of IFC. However, it has been difficult to distinguish between general IFC structure and the specific structure for the Duplex.ifc model, which was the baseline for the course. We started out trying to make the script run through all materials in one loop, but quickly discovered, that the IFC structure varries too much for a generallisation. Thereafter we made a script, where we test walls, beams, and windows. Ideally all layered components (walls, roof, slab etc.) should be run through in the same loop, and come with a view of the matierals given in m3. Then another loop should run through beams and columns, and give a view of the different types in the model given in m (length) or kg. Windows should be kept sepperatly, since the structure is different and the wanted output is an area. In the end, matierals are listed for each category corresponding to the categories in LCAbyg and **if** there is an error in the file (e.g. interior walls are not assigned a material), there will be an error message, stating which component isn't sufficiently detailed for an LCA.
However, we ran out of time and didn't make it further than walls, beams and windows. Future students would benefit from starting out in our script and working on making it for general. They should especially work on making the script work for the general IFC structure and test the code on different IFC models.  

### Did the process of the course enable you to answer or define questions that you might need later for thesis?
In some way yes, it introduces the OpenBIM tool. However, the course needs a clearer structure, to give the students a better overview of what is expected from them from the start. 

### Would you have preferred to have been given less choice in the use cases?
The number of choices fit perfectly for the case studies. However, more focus on the background knowledge on the IFC structure before the choices were made could be beneficial. 

### Was the number of tools for the course ok - should we have more or less? - if so which ones would you leave out?
The HTML-part could perhaps be switched out with some more IFC-specific coding, so we could learn the step from blenderpy to Python easier.
It is difficult to have guest lectures, that interests all groups when our use cases are so different. An idea was to have lectures specific for each use case, and then the rest could work on their project and get help from the TAs.  

## Output of the tool
### Did the tool address the use case you identified?
Yes, the use case was to perform a check if an IFC-model had materials assignened to each component, and extract materials and their amounts. However, as mentioned, the tool is not finnished but we ran out of time. 

### Was the use case well modelled and clearly scoped
That depended on our own composition since the guidelines for the use cases weren’t strict. Judging from our feedback and our own perception, we think the case was well modelled and clearly scoped.  As mentioned before, we would have liked to have received a clearer introduction to what was expected from us from the start. 

## Future
### Are you likely to use OpenBIM tools in your thesis
Yes, probably. Coding opens up a lot of opportunities to make different processes more effective and automatic, which can advantageously be incorporated into a master thesis. 

### Are you likely to use OpenBIM tools in your professsional life in the next 10 years?
Probably. Coding opens up a lot of opportunities to make different processes more effective and automatic, which is very important in the building industry to keep cost down and reduce "human errors" in a project. 
