# Use Case: LCA 
### Introduction 
This project is a part of the 41934 course at DTU, where we, group 4, have chosen LCA as use case. 
The use case is aimed to be relevant for sustainability engineers to help build inventory and overview of building material composistions. It is meant to be used in the early design stage of new buildings. 

The disciplinary expertise used to solve the use case is our general knowledge about LCA.

### IFC Concepts used
The IFC Concepts we will use in our script are HasAssociations of different IFC elements to find the different materials associated to the IFC entities (e.g the material of the beams). Furthermore, the script will be able to look into the dimensions of the elements in order to find the amount of the materials and ideally find the enviromental impacts.

### Overview of disciplinary analysis
To be able to perform a fulfilled LCA, it is required to have the energy frame analysis of the building.
Furthermore, it is essential to have all elements of the building and their materials.

Before it is possible to do an LCA analysis following use cases need to be done:

1. Structure 
2. Indoor and Energy 
3. Fire 
4. Acoustics 
5. Daylight 
6. Build / Operation

The input data for this use case would be the amount and the different types of materials together with the energy consumption of the building (from the energy frame). Additionally, the energy consumption used on the building site (data input based on Build/Operation) is needed to make a full LCA.

The use case, (Building) Code Validation, needs a LCA analysis to see if the building complies to BR18. 

###Scope definition
The scope of the use case is to analyse aspects early stage design processes that have a big impact in the final LCA of a building. An important contributor to the energy consumption of the building is the windows. Here the type, the number of glass layers and glass area has been chosen, because they play a big role regarding how much heating and cooling energy the building needs. Furthermore the case will focus on extracting the amount (m^3) of insulation. In addition to having a large impact on the heating and cooling of the building, the production of insulation has a large environmental impact. 

### Flowchart of LCA
The flowchart of the overall process of a LCA is shown below. The chosen scope is marked with a red circle.

![LCA_2_Gr4](https://user-images.githubusercontent.com/112398958/193603479-5c783904-2264-419d-adf8-ca5258df26c9.svg)



