import re
import pandas as pd
import numpy as np
import ipywidgets
from ipywidgets import interact, interactive, fixed, widgets
import py3Dmol as p3d


def psi4_read_scf(file):
    cycles=[]
    with open(file, "r") as file:
        for line in file:
            if re.search('iter', line):
                cycles.append(line)
    cycles = [ cycle.replace('@DF-UHF iter ','').replace(' DIIS', '').split('   ') for cycle in cycles]
    cycles = np.array(cycles)
    scf = pd.DataFrame(cycles[:,1:], columns=['iteration', 'Total Energy', 'Delta E', 'RMS |[F,P]|'])
    scf['Total Energy'] = scf['Total Energy'].astype(float)
    scf['Delta E'] = scf['Delta E'].astype(float)
    scf['RMS |[F,P]|'] = scf['RMS |[F,P]|'].astype(float)
    return scf


def read_coordinates(file):
    f = open(file, "r")
    lines = f.readlines()
    new=True
    molecules = []
    for line in lines:
        if new:
            nAtoms=int(line)
            molecule = []
            added=0
            new=False
            continue
        if 'Geometry for iteration' in line:
            continue
        if added<=nAtoms:
            coord = list(filter(None, line.replace('\t','').replace('\n','').split(' ')))[1:]
            coord = [float(x) for x in coord]
            molecule.append(coord)
            added+=1
            if added==nAtoms:
                new=True
                molecules.append(np.array(molecule))
    return molecules

def readXYZ(file):
    f = open(file, "r")
    lines = f.readlines()
    new=True
    molecules = []
    for line in lines:
        if new:
            nAtoms=int(line)
            molecule = ""
            added=0
            new=False
            continue
        if 'Geometry for iteration' in line:
            continue
        if added<=nAtoms:
            coord = str(line.replace('\t   ',''))
            molecule+=coord
            added+=1
            if added==nAtoms:
                new=True
                
                molecules.append(f"{nAtoms}\n\n"+molecule)
    return molecules[1:]

def angle_distances(coordinates):
    """for a triatomic molecule return the angle and the distances"""
    O=coordinates[0]
    H1=coordinates[1]
    H2=coordinates[2]
    OH1=O-H1
    OH2=O-H2
    unit_vector_1 = OH1 / np.linalg.norm(OH1)
    unit_vector_2 = OH2 / np.linalg.norm(OH2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    return angle*180/np.pi, np.linalg.norm(OH1), np.linalg.norm(OH2)


# Draws XYZ list geometries based on their input number, useful for interact
def drawXYZGeomNum(geom, conf):
    view = p3d.view(width=400, height=400)
    view.addModel(geom[conf], "xyz")
    view.setStyle({'stick':{}})
    view.zoomTo()
    return(view.show())

def drawXYZGeomSlider(geom):
    interact(drawXYZGeomNum, geom=fixed(geom), conf=widgets.IntSlider(min=0, max=len(geom)-1, step=1))
