class atom:
    def __init__(self, atomName, symbol, protons, electrons, netruons):
        self.atomName = atomName
        self.symbol = symbol
        self.protons = protons
        self.electrons = electrons
        self.neutrons = netruons

    def atomicMass(self):
        return self.protons + self.electrons + self.neutrons

    def printSymbolAndName(self):
        print(f'{self.symbol} :: {self.atomName}')