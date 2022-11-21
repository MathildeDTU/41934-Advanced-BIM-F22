# Created by Group 4: s173996; s183623; s183627; s183631
# (41934) Advanced BIM, F22
# Use case: LCA

#############################################
############## Adding libaries ##############
#############################################
import ifcopenshell
import tkinter as tk

#############################################
########## Loading the IFC model ############
#############################################

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

model = ifcopenshell.open(main_win.sourceFile)

#############################################
################### WALL ####################
#############################################
def wallMaterialAmount(model):
    walls = model.by_type("IfcWall")
    total_wall_material = {}
    for wall in walls:
        # print("\n")
        # print(wall.Name)

        for definition in wall.IsDefinedBy:
            if definition.is_a('IfcRelDefinesByProperties'):
                property_set = definition.RelatingPropertyDefinition

                for property in property_set.HasProperties:
                    if property.Name == "Area":
                        areaofwall = property.NominalValue.wrappedValue

        if wall.HasAssociations:
            for wallMaterial in wall.HasAssociations:
                if wallMaterial.is_a('IfcRelAssociatesMaterial'):
                    volumeofmaterial = 0
                    material_list = []

                    for materialLayer in wallMaterial.RelatingMaterial.ForLayerSet.MaterialLayers:
                        # print(materialLayer.Material)
                        material_list.append(materialLayer.Material.Name)
                        thickness = materialLayer.LayerThickness
                        volumeofmaterial = thickness * areaofwall
                        name = materialLayer.Material.Name

                        if name not in total_wall_material:
                            total_wall_material[name] = volumeofmaterial
                        else:
                            total_wall_material[name] += volumeofmaterial

                    if len(material_list) == 0:
                        warning_wall = 'Material is missing in {}'.format(wall.Name)
                        print(warning_wall)

    sorted_total_wall_material = sorted(total_wall_material.items(), key=lambda x: x[1], reverse=True)
    print("\n")
    label_wall = 'Materials and their amounts [m3]: \n {}'.format(sorted_total_wall_material)
    print(label_wall)


wallMaterialAmount(model)

#############################################
################### BEAM ####################
#############################################
def beamCounter(model):
    beams = model.by_type('IfcBeam')  # defines the different types of elements, e.g. beams, walls, etc.

    material_beam = []
    beam_counting = []
    beam_type = []
    for beam in beams:
        for relAssociatesMaterials in beam.HasAssociations:  # Checks the associated materials in the 'beams'-elements.
            if relAssociatesMaterials.RelatingMaterial.Name not in material_beam:
                material_beam.append(
                    relAssociatesMaterials.RelatingMaterial.Name)  # Prints out the materials used in each beam
            beam_counting.append(relAssociatesMaterials.RelatingMaterial.Name)
            beam_count = len(beam_counting)
            type_beam = beam.ObjectType  # Takes the Object type
            beam_type.append(type_beam)

    beam_type = {i: beam_type.count(i) for i in beam_type}  # count the number of times the type is repeated
    label_beam = 'The number of beams is: {} (type: numbers of beam type)'.format(beam_type)
    print("\n")
    print(label_beam)


beamCounter(model)

#############################################
################# WINDOW ####################
#############################################
def windowCounter(model):
    windows = model.by_type('IfcWindow')  # defines the different types of elements, e.g. beams, walls, etc.

    window_counting = []

    for window in windows:
        window_area = window.OverallHeight * window.OverallWidth
        window_counting.append(window_area)
        window_sum = sum(window_counting)
        window_count = len(window_counting)

    label_win = 'The total area of the windows is {} sqm'.format(window_sum)
    print("\n")
    print(label_win)


windowCounter(model)
