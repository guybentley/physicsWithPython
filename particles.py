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

    def decay(self):
        #as far as we know, only hydrogen and helium are stable with more neutrons than protons, so if the atom has more protons than neutrons, it will decay.
        #later on I will add in the maths around decay and half life, but for now this is a simple implementation of decay.
        #TODO A proper balanced calculation of neutrons to protons balance calculation based on the weak nuclear force and the strong nuclear force, as well as the electromagnetic force, and the weak nuclear force.
        if(self.protons > self.neutrons and self.protons != 1 and self.protons != 2):
            self.protons -= 1
            self.neutrons += 1
            print(f'{self.atomName} has decayed')

    