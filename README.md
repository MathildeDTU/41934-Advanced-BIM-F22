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

### Scope definition
The scope of the use case is to analyse aspects early stage design processes that have a big impact in the final LCA of a building. it is of interst to examine the amount of steel beams in the building, to investigate the environmental impact the choice of steel as a material has in the final LCA of the building. 

# Report 

## 3A: Analyse use case
# 1. Goal: 
The goal of this use case is to extract amount of steel beams in the building to investigate the environmental impact the choice of steel as a material has in the final LCA of the building.  
# 2. Model Use (Bim Uses): 
The model is outdated, as it does not include LCA, this the most applicable is a _sustainability analysis_, where we _gather_ and _quantify_.

## 3B: Propose a (design for a) tool / workflow
#### 3. The process diagram/Flowchart of LCA
The flowchart of the overall process of a LCA is shown below. The red circle marks where in the process the scope of this use case is placed.

![LCA_2_Gr4](https://user-images.githubusercontent.com/112398958/193603479-5c783904-2264-419d-adf8-ca5258df26c9.svg)

#### 4. Description of the process of the workflow.
The scope is defined a previous section above. The initial step of performing a LCA is for the engineer to collect relevant data. The workflow illustrated above is based on the extraction of an IFC file from a BIM Model. The extracted IFC file can then be analysed using OpenBIM Software and in relation to this a script can be used to extract the amount of steel beams in the building. If the BIM model doesn't contain the required information, the model is sent back to the architect, who will then update it and send it back to the engineer, who can then extract a new IFC file once again. When all the needed data are colllected, the data can be entered into a LCA program etc. LCA Byg by an engineer. From here the results can be used to finally validate if the building comply to BR18.


## 3C: Information exchange
5. Information Exchange: Fill out the excel template with the information for your planned tool / workflow. For this you will need access to the excel, and the Dikon document to help you specify the LOD (LOR,LOG,LOI) for each element you need for you tool / workflow. This can get confusing - don’t worry we can help 😊
6. IFC: Describe the IFC entities and properties for each of the elements you identified in your information exchange. Describe the data that you need to:
- Find in the IFC
- Find in an external sources i.e. BR18
- Based on assumptions (useful when we don't have the 'real' data that we need for our tool)

## 3D: Value What is the potential improvement offered by this tool?
This is the common question when developing tools and processes as an intrapreneur in a company. You should consider the business and societal value of this tool – does it save time to the company, does it make employees happier / more productive? Could it reduce material use in society?

7. Describe the business value (How does it create value for your business / employer)
8. Describe the societal value (How does it make the world better)
N.B. If it doesn't do either of these things (ideally it should do both - don't do it!!)

## 3E: Delivery
In this assignment we will focus on the input data that you need for your final tool / workflow. 
9. Your tool/workflow: Description of how your tool / workflow would solve the use case 
10. 10. Delivery: Description of how you would make the tool / workflow - what steps would you go through?
