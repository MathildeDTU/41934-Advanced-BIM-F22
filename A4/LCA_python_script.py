# Created by Group 4: s173996; s183623; s183627; s183631
# (41934) Advanced BIM, F22
# Use case: LCA


# Importing libraries and files
import tkinter as tk
import ifcopenshell
import time
import os


########## Engine

##### File explorer
from tkinter import filedialog
main_win = tk.Tk() 
main_win.withdraw()

main_win.overrideredirect(True)
main_win.geometry('0x0+0+0')

main_win.deiconify()
main_win.lift()
main_win.focus_force()

main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", #open file selector 
title='Please select a directory for your .IFC file')
main_win.destroy() #close window after selection
print(main_win.sourceFile) #print path 


##### Loading the IFC model
def modelLoader(name):

    model_url = "model/"+name+".ifc"

    if (os.path.exists(model_url)):
        model = ifcopenshell.open(model_url)
    
    else:
        print("\nERROR: please check your model folder : " +model_url+" does not exist")  
       
        return model

##### BEAM
def beamCounter(model):
    beams = model.by_type("IfcBeam")  # defines the different types of elements, e.g. beams, walls, etc.

    material_beam = []
    beam_counting = []
    for beam in beams:
        for relAssociatesMaterials in beam.HasAssociations:  # Checks the associated materials in the 'beams'-elements.
            if relAssociatesMaterials.RelatingMaterial.Name not in material_beam:
                material_beam.append(
                    relAssociatesMaterials.RelatingMaterial.Name)  # Prints out the materials used in each beam
                beam_counting.append(relAssociatesMaterials.RelatingMaterial.Name)
                beam_count = len(beam_counting)
                print(beam_count)
    





# Graphical User Interface (GUI)
window = tk.Tk()






#mainloop()


