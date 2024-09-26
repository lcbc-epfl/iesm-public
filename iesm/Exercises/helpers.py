import re
import pandas as pd
import numpy as np
import ipywidgets
from ipywidgets import interact, interactive, fixed, widgets
import py3Dmol
import psi4 

hartree2A = 0.52917721067121

def psi4_read_scf(file):
    cycles=[]
    with open(file, "r") as file:
        for line in file:
            if re.search('iter', line):
                cycles.append(line)
    cycles = [ cycle.replace('@DF-UHF iter ','').replace(' DIIS', '').replace('/', '').replace('ADIIS', '').replace('DIIS', '').replace('\n', '').split(' ') for cycle in cycles]
    new_cycles=[]
    for cycle in cycles:
        new_cycles.append([i for i in cycle if i != ''])
    cycles=new_cycles
    cycles = np.array(cycles)
    scf = pd.DataFrame(cycles[:,:], columns=['iteration', 'Total Energy', 'Delta E', 'RMS |[F,P]|'])
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
    view = py3Dmol.view(width=400, height=400)
    view.addModel(geom[conf], "xyz")
    view.setStyle({'stick':{}, 'sphere':{'scale':0.1}})
    view.zoomTo()
    return(view.show())

def drawXYZGeomSlider(geom):
    interact(drawXYZGeomNum, geom=fixed(geom), conf=widgets.IntSlider(min=0, max=len(geom)-1, step=1))

#Slider of molecular energy at different values of a property (i.e. dihedral angle)
#including both the 2D energy-property plot and showing the corresponding geometry
def drawXYZGeomSliderMolecularProperty(geom, quantity_array, energies_array, quantity_label):
    import matplotlib.pyplot as plt
    def drawXYZGeomNumMolecularProperty(geom, quantity):
        view = py3Dmol.view(width=400, height=400)
        i,= np.where(quantity_array==quantity)
        view.addModel(geom[int(i)], "xyz")
        view.setStyle({'stick':{}, 'sphere':{'scale':0.1}})
        view.zoomTo()
        fig, ax = plt.subplots()
        ax.plot(quantity_array, energies_array)
        ax.scatter(quantity_array[np.where(quantity_array == quantity, True, False)], energies_array[np.where(quantity_array == quantity, True, False)])
        ax.set_xlabel(quantity_label)
        ax.set_ylabel('Pot. Energy [kcal/mol]')
        plt.show()
        return(view.show())
    
    interact(drawXYZGeomNumMolecularProperty, geom=fixed(geom), quantity=widgets.IntSlider(min=min(quantity_array), max=max(quantity_array), step=(max(quantity_array)-min(quantity_array))/(len(quantity_array)-1)))


def calculate_dihedral(a, b, c, d):
    """Calculates dihedral from cartesian coordinates"""
    b0 = -1.0*(b - a)
    b1 = c - b
    b2 = d - c
    # normalize b1
    b1 /= np.linalg.norm(b1)
    # v = projection of b0 onto plane perpendicular to b1
    #   = b0 minus component that aligns with b1
    # w = projection of b2 onto plane perpendicular to b1
    #   = b2 minus component that aligns with b1
    v = b0 - np.dot(b0, b1)*b1
    w = b2 - np.dot(b2, b1)*b1
    # angle between v and w in a plane is the torsion angle
    # v and w may not be normalized but that's fine since tan is y/x
    x = np.dot(v, w)
    y = np.dot(np.cross(b1, v), w)
    return np.degrees(np.arctan2(y, x))

def calculate_angle(a,b,c):
    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)

def calculate_bond(a,b):
    ba = a - b
    return np.linalg.norm(ba)



def drawXYZ_labeled(mol):
    hartree2A = 0.52917721067121
    view = py3Dmol.view(width=400, height=400)
    view.addModel(mol.save_string_xyz_file(), "xyz")

    for i,(x,y,z) in enumerate(mol.to_arrays()[0]*hartree2A):
        view.addLabel(str(i),{'position':{'x':x,'y':y,'z':z},'inFront':True})
    view.setStyle({'stick':{}, 'sphere':{'scale':0.1}})
    view.setStyle({'model':0},{'stick':{'colorscheme':'yellowCarbon'}, 'sphere':{'scale':0.1}})
    view.zoomTo()
    return(view.show())


import glob
def findCubeFiles(wd="./"):
    """
    returns list of all cube files
    """
    orbitals = {}
    cubefiles = glob.glob(wd+"*.cube")
    cubefiles = [cube.replace(wd,'') for cube in cubefiles]
    cubefiles = [cube.replace('Psi_','') for cube in cubefiles]
    cubefiles = [cube.split('-') for cube in cubefiles]

    for cube in cubefiles:
        alpha_or_beta, n1, n2 = cube[0].split('_')
        irrep, name = cube[1].replace('.cube', '').split('_')
        if name in orbitals:
            orbitals[name].append((alpha_or_beta, n1, n2, irrep))
        else:
            orbitals[name] =[(alpha_or_beta, n1, n2, irrep)]
    return orbitals

import ipywidgets
from ipywidgets import interact, interactive, fixed, widgets

def draw_orbital(mol, orbitals, orbital, wd):
    view = py3Dmol.view(width=400, height=400)

    xyz = mol.save_string_xyz_file()
    view.addModel(xyz, "xyz")
    view.setStyle({'stick':{}})
    colours = ['red', 'blue']

    for i,orb in enumerate(orbitals[orbital]):
        orb_file = open(f"{wd}/Psi_{orb[0]}_{orb[1]}_{orb[2]}-{orb[3]}_{orbital}.cube", "r").read()
        view.addVolumetricData(orb_file, "cube", {'isoval': -0.02, 'color': colours[i], 'opacity': 0.75})

    view.zoomTo()
    return(view.show())

def show_orbitals(wd="./", mol=None):
    """
    wrapper function that parses the files and initializes the widget.
    """
    orbitals =  findCubeFiles(wd)
    _ = interact(draw_orbital, mol=fixed(mol),wd=fixed(wd), orbitals=fixed(orbitals), orbital = widgets.Dropdown(
    options=orbitals.keys(),
    value='SOMO',
    description='Orbital:',
    disabled=False,
))


def drawXYZSideBySide(mol1, mol2):
    view = py3Dmol.view(viewergrid=(1,2))
    view.addModel(mol1.save_string_xyz_file(), "xyz", viewer=(0,0))
    view.addModel(mol2.save_string_xyz_file(), "xyz", viewer=(0,1))
    view.setStyle({'stick':{}, 'sphere':{'scale':0.1}})
    view.zoomTo()
    return(view.show())

def drawXYZSideBySide_labeled(mol1, mol2):
    hartree2A = 0.52917721067121
    view = py3Dmol.view(viewergrid=(1,2))
    if type(mol1) == str:
        mol1 = psi4.geometry(mol1)
    view.addModel(mol1.save_string_xyz_file(), "xyz", viewer=(0,0))
    for i,(x,y,z) in enumerate(mol1.to_arrays()[0]*hartree2A):
        view.addLabel(str(i),{'position':{'x':x,'y':y,'z':z},'inFront':True}, viewer=(0,0))
    if type(mol2) == str:
        mol2 = psi4.geometry(mol2) 
    view.addModel(mol2.save_string_xyz_file(), "xyz", viewer=(0,1))
    for i,(x,y,z) in enumerate(mol2.to_arrays()[0]*hartree2A):
        view.addLabel(str(i),{'position':{'x':x,'y':y,'z':z},'inFront':True}, viewer=(0,1))
    
    view.setStyle({'stick':{}})
    view.setStyle({'model':0},{'stick':{'colorscheme':'yellowCarbon'}, 'sphere':{'scale':0.1}})
    view.zoomTo()
    return(view.show())


def drawXYZ(mol):
    view = py3Dmol.view(width=400, height=400)
    view.addModel(mol.save_string_xyz_file(), "xyz")
    view.setStyle({'stick':{}, 'sphere':{'scale':0.1}})
    view.zoomTo()
    return(view.show())

def peak(S,nrows=4,ncols=4):
    print(F'Here is a peak at the first {nrows} x {ncols} elements of the matrix:\n{S[:nrows,:ncols]}')

def isBasisOrthonormal(S):
    # get the number of rows of S
    size_S = S.shape[0] 
    
    # construct an identity matrix, I
    identity_matrix = np.eye(size_S) 

    # are all elements of S numerically close to the identity matrix? 
    # We won't test for equality because there can be very small numerical 
    # differences that we don't care about
    orthonormal_check = np.allclose(S, identity_matrix)

    print(F'Q:(T/F) The AO basis is orthonormal? A: {orthonormal_check}')
    return orthonormal_check


from IPython.display import display

def section(fle, begin, end):
    """
    yields a section of a textfile. 
    Used to identify [COORDS] section etc
    """
    with open(fle) as f:
        for line in f:
            # found start of section so start iterating from next line
            if line.startswith(begin):
                for line in f: 
                    # found end so end function
                    if line.startswith(end):
                        return
                    # yield every line in the section
                    yield line.rstrip()    

def parse_molden(filename='default.molden_normal_modes'):
    """
    Extract all frequencies, the base xyz coordinates 
    and the displacements for each mode from the molden file
    """
    all_frequencies = list(section(filename, '[FREQ]', '\n'))
    all_frequencies = [(float(freq),i) for i, freq in enumerate(all_frequencies)]
    coords = list(section(filename, '[FR-COORD]', '\n'))
    normal_modes = []
    for freq in range(len(all_frequencies)):
        if freq+1 != len(all_frequencies):
            normal_modes.append(list(section(filename, f'vibration {freq+1}', 'vibration')))
        else:
            normal_modes.append(list(section(filename, f'vibration {freq+1}', '\n')))
    return all_frequencies, coords, normal_modes

def draw_normal_mode(mode=0, coords=None, normal_modes=None):
    """
    draws a specified normal mode using the animate mode from py3Dmol. 
    Coming from psi4 units need to be converted from a.u to A. 
    """
    fac=0.52917721067121  # bohr to A
    xyz =f"{len(coords)}\n\n"
    for i in range(len(coords)):
        atom_coords = [float(m) for m in  coords[i][8:].split('       ')]
        mode_coords = [float(m) for m in  normal_modes[mode][i][8:].split('       ')]
        xyz+=f"{coords[i][0:4]} {atom_coords[0]*fac} {atom_coords[1]*fac} {atom_coords[2]*fac} {mode_coords[0]*fac} {mode_coords[1]*fac} {mode_coords[2]*fac} \n"
    view = py3Dmol.view(width=400, height=400)
    view.addModel(xyz, "xyz", {'vibrate': {'frames':10,'amplitude':1}})
    view.setStyle({'sphere':{'scale':0.30},'stick':{'radius':0.25}})
    view.setBackgroundColor('0xeeeeee')
    view.animate({'loop': 'backAndForth'})
    view.zoomTo()
    return(view.show())

def show_normal_modes(filename='default.molden_normal_modes'):
    """
    wrapper function that parses the file and initializes the widget.
    """
    all_frequencies, coords, normal_modes =  parse_molden(filename=filename)
    _ = interact(draw_normal_mode, coords=fixed(coords), normal_modes=fixed(normal_modes), mode = widgets.Dropdown(
        options=all_frequencies,
        value=0,
        description='Normal mode:',
        style={'description_width': 'initial'}
    ))
    
def mol2traj(mol, coordinates):
    elements = mol.to_dict()['elem']
    traj = []
    for coords in coordinates:
        coords = np.array(coords)
        coords*= hartree2A 
        xyz =f"{len(coords)}\n\n"
        for i in range(len(coords)):
            xyz+=f"{elements[i]} {coords[i][0]} {coords[i][1]} {coords[i][2]} \n"
        traj.append(xyz)
    return traj

def coord2traj_array(coordinates):
    traj_array = []
    for coords in coordinates:
        coords = np.array(coords)
        coords*= hartree2A 
        traj_array.append(coords)
    return traj_array
     


