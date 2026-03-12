class atom:
    def __init__(self, atomName, symbol, protons, electrons, netruons):
        self.atomName = atomName
        self.symbol = symbol
        self.protons = protons
        self.electrons = electrons
        self.neutrons = netruons

        def atomicMass():
            return protons + electrons + netruons
        