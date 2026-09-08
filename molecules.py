import particles
import json

class Molecule:
    def __init__(self, name, formula, atoms):
        self.name = name
        self.formula = formula
        self.atoms = atoms  # List of Particle instances

    def __str__(self):
        return f"{self.name} ({self.formula})"

    def get_molecular_weight(self):
        return sum(atom.mass for atom in self.atoms)

class MoleculeStore:
    def __init__(self):
        self.molecules = []

    def add_molecule(self, molecule):
        self.molecules.append(molecule)

    def get_molecule_by_name(self, name):
        for molecule in self.molecules:
            if molecule.name == name:
                return molecule
        return None

    def list_molecules(self):
        return [str(molecule) for molecule in self.molecules]

    def loadMoleculesFromFile(self, filename):
        with open(filename, 'r') as json_data:
            data = json.load(json_data)
            for molecule_data in data["molecules"]:
                atoms = [particles.Particle(atom) for atom in molecule_data["atoms"]]
                molecule = Molecule(molecule_data["name"], molecule_data["formula"], atoms)
                self.add_molecule(molecule)