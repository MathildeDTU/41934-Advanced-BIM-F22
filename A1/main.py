# Created by Group 4: s173996; s183623; s183627; s183631
# (41934) Advanced BIM, F22
# Use case: LCA

import bpy
from blenderbim.bim.ifc import IfcStore                     # Imports Ifcopenshell.util.element.

file = IfcStore.get_file()
beams = file.by_type("IfcBeam")                             # defines the different types of elements, e.g. beams, walls, etc.
walls = file.by_type("IfcWall")   

for beam in beams:
  for relAssociatesMaterials in beam.HasAssociations:       # Checks the associated materials in the 'beams'-elements.
    print(relAssociatesMaterials.RelatingMaterial.Name)     # Prints out the materials used in each beam.
    

# Walls have different layers (with thicknesses), so the approach will be slightly adjusted for walls ...

# for wall in walls: 
  # ... 
  
