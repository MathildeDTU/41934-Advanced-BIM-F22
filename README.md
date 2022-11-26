# Use Case: Check model for information to LCA 
### Introduction 
This project is a part of the 41934 course at DTU, where we, group 4, have chosen LCA as use case. 
The use case is aimed to be relevant for sustainability engineers to help build inventory and overview of building material composistions. It is meant to be used in the early design stage of new buildings, when the first BIM model draft is ready. Then the code will check whether the BIM model contains the required information, for instance the area of the windows, to perform an early LCA to see if the buildings is within certain tresholds.  

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
The scope of the use case is to analyse aspects early stage design processes that have a big impact in the final LCA of a building. First of all it is a tool that checks if the necessary information is within the IFC file. In this connection it is of interst to examine the amount of steel beams in the building, to  be abæe to investigate the environmental impact the choice of steel as a material has in the final LCA of the building. Furthermore the tool should function on walls and components with material layers, and in the same way find the total area of windows in the building. All the materials will all have a influence in a final LCA, and will play a big part in the picture of whether a building is below a certain treshold regarding environemntal impacts.

# Report 

## 3A: Analyse use case
#### 1. Goal: 
The goal of this use case is to create a code that can check whether data is missing in the present BIM Model. The code shall print a warning if a material in the IFC file is missing. This should then be corrected in the BIM Model, whereas the model can be converted to an IFC file and be checked by the code again. 

#### 2. Model Use (Bim Uses): 
The model is outdated, as it does not include LCA, thus the most applicable is a _sustainability analysis_, where we _gather_ and _quantify_.

## 3B: Propose a (design for a) tool / workflow
#### 3. The process diagram/Flowchart of LCA
The flowchart of the overall process of a LCA is shown below in Figure 1. The red circle marks where in the process the scope of this use case is placed.

![LCA_2_Gr4](https://user-images.githubusercontent.com/112398958/193603479-5c783904-2264-419d-adf8-ca5258df26c9.svg)
*Figure 1: Flowchart of LCA tool*

#### 4. Description of the process of the workflow.
The scope is defined a previous section above. The initial step of performing a LCA is for the engineer to collect relevant data. The workflow illustrated above is based on the extraction of an IFC file from a BIM Model. The extracted IFC file can then be analysed using OpenBIM Software and in relation to this a script can be used to extract e.g. the amount of for instance steel beams in the building. The IFC file is then checked by the script to see if it contains all the relevant data. If the BIM model doesn't contain the required information, the model is sent back to the architect, who will then update it and send it back to the engineer, who can then extract a new IFC file once again. When all the needed data are colllected, the data can be entered into an LCA program e.g. LCA Byg by an engineer to get som initial results on the environemntal impact of the bulding. From here the results can be used to finally validate if the building complies to BR18.


## 3C: Information exchange
#### 5. The excel template 
The excel template is filled out with the information for the planned workflow. In this the LOD of the beams are specified as 200 (B325), however LOG can be lower since no actual geometry is required for a LCA.

#### 6. IFC entities and properties
The IFC entities and properties used are described in the previous section "IFC Concepts used".

## 3D: Value What is the potential improvement offered by this tool?
The described tool in this use case is an open source tool to extract IFC data for early stage design, and to check whether the file contains the necessary information. In this way it is avoided to use heavily licensed software e.g. Revit to extract quantities for data sheets. The extracted quantities are easily used to get an initial sustainability certification of the building design. 
#### 7./8. The business and societal value
The business value of the tool is clarified in the availability of it being an open source alternative. The tool would also contribute to the societal value by reducing the environmental footprint of the building. 

## 3E: Delivery
#### 9./10. Tool/workflow and delivery 
The worflow and the necessary steps are described in section 4 "Description of the process of the workflow".

# Describtion of the tool
The tool is meant to assist with creating an inventory of materials for Life Cycle Assessment (LCA) of buildings, based on the IFC-file. 
It can, as mentioned before, be used in the early design stage, when the first BIM drafts are ready. The code will then return material types, -amounts, and in some cases -dimensions to be input easily in LCA software. If the IFC file doesn’t contain the required information, the script will return a warning. The missing data should then be corrected in the BIM Model, whereas the model can be converted to an IFC file and then be checked again by the code.  
The 2 minute video gives a shot introduction to the purpose of the tool, together with a guidiance on how to use it and what the future visions for it is. 

# Future work 
As described in the description video, the vision for the future of this tool is illustrated below in Figure 2-4. 
The main window (Figure 2) would contain the initial check of whether each component has a referenced material. By selecting e.g. walls, it would show a 3D view of the missing information. Additionally, the user would be presented with a secondary window, showing the total amounts of each material. 

![Vision1](https://user-images.githubusercontent.com/112398958/204106106-54b5508a-cba4-4247-b8ec-e25f4ed049ff.PNG)
*Figure 2: The main window.* 

A user-friendly change would be to expand a window when selecting a component; and being able to suggest changes (like on Github), which would notify the architects upstream of what information is needed and how it can be solved (Figure 3). 

![Vision2](https://user-images.githubusercontent.com/112398958/204106110-2726eb63-063d-48a6-9121-0ba58fee87ca.PNG)
*Figure 3: Exansion of window when selecting a component.*

Alternative versions for checking the presence of material properties for daylighting, indoor climate, etc. could be developed as a more advanced version of the tool (Figure 4).  

![Vision3](https://user-images.githubusercontent.com/112398958/204106116-10d325f7-8188-4255-abe9-72b926b0c2bc.PNG)
*Figure 4: Alternative checks.*
