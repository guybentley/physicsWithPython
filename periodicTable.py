import particles

class periodicTable:
    def __init__(self):
        self.table = []
        
        # Periodic Table - neutrons based on most abundant/stable isotope
        hydrogen      = particles.atom("Hydrogen",       "H",   1,   1,   0)
        helium        = particles.atom("Helium",         "He",  2,   2,   2)
        lithium       = particles.atom("Lithium",        "Li",  3,   3,   4)
        beryllium     = particles.atom("Beryllium",      "Be",  4,   4,   5)
        boron         = particles.atom("Boron",          "B",   5,   5,   6)
        carbon        = particles.atom("Carbon",         "C",   6,   6,   6)
        nitrogen      = particles.atom("Nitrogen",       "N",   7,   7,   7)
        oxygen        = particles.atom("Oxygen",         "O",   8,   8,   8)
        fluorine      = particles.atom("Fluorine",       "F",   9,   9,  10)
        neon          = particles.atom("Neon",           "Ne", 10,  10,  10)
        sodium        = particles.atom("Sodium",         "Na", 11,  11,  12)
        magnesium     = particles.atom("Magnesium",      "Mg", 12,  12,  12)
        aluminum      = particles.atom("Aluminum",       "Al", 13,  13,  14)
        silicon       = particles.atom("Silicon",        "Si", 14,  14,  14)
        phosphorus    = particles.atom("Phosphorus",     "P",  15,  15,  16)
        sulfur        = particles.atom("Sulfur",         "S",  16,  16,  16)
        chlorine      = particles.atom("Chlorine",       "Cl", 17,  17,  18)
        argon         = particles.atom("Argon",          "Ar", 18,  18,  22)
        potassium     = particles.atom("Potassium",      "K",  19,  19,  20)
        calcium       = particles.atom("Calcium",        "Ca", 20,  20,  20)
        scandium      = particles.atom("Scandium",       "Sc", 21,  21,  24)
        titanium      = particles.atom("Titanium",       "Ti", 22,  22,  26)
        vanadium      = particles.atom("Vanadium",       "V",  23,  23,  28)
        chromium      = particles.atom("Chromium",       "Cr", 24,  24,  28)
        manganese     = particles.atom("Manganese",      "Mn", 25,  25,  30)
        iron          = particles.atom("Iron",           "Fe", 26,  26,  30)
        cobalt        = particles.atom("Cobalt",         "Co", 27,  27,  32)
        nickel        = particles.atom("Nickel",         "Ni", 28,  28,  30)
        copper        = particles.atom("Copper",         "Cu", 29,  29,  34)
        zinc          = particles.atom("Zinc",           "Zn", 30,  30,  34)
        gallium       = particles.atom("Gallium",        "Ga", 31,  31,  38)
        germanium     = particles.atom("Germanium",      "Ge", 32,  32,  42)
        arsenic       = particles.atom("Arsenic",        "As", 33,  33,  42)
        selenium      = particles.atom("Selenium",       "Se", 34,  34,  46)
        bromine       = particles.atom("Bromine",        "Br", 35,  35,  44)
        krypton       = particles.atom("Krypton",        "Kr", 36,  36,  48)
        rubidium      = particles.atom("Rubidium",       "Rb", 37,  37,  48)
        strontium     = particles.atom("Strontium",      "Sr", 38,  38,  50)
        yttrium       = particles.atom("Yttrium",        "Y",  39,  39,  50)
        zirconium     = particles.atom("Zirconium",      "Zr", 40,  40,  50)
        niobium       = particles.atom("Niobium",        "Nb", 41,  41,  52)
        molybdenum    = particles.atom("Molybdenum",     "Mo", 42,  42,  56)
        technetium    = particles.atom("Technetium",     "Tc", 43,  43,  55)
        ruthenium     = particles.atom("Ruthenium",      "Ru", 44,  44,  58)
        rhodium       = particles.atom("Rhodium",        "Rh", 45,  45,  58)
        palladium     = particles.atom("Palladium",      "Pd", 46,  46,  60)
        silver        = particles.atom("Silver",         "Ag", 47,  47,  60)
        cadmium       = particles.atom("Cadmium",        "Cd", 48,  48,  66)
        indium        = particles.atom("Indium",         "In", 49,  49,  66)
        tin           = particles.atom("Tin",            "Sn", 50,  50,  70)
        antimony      = particles.atom("Antimony",       "Sb", 51,  51,  70)
        tellurium     = particles.atom("Tellurium",      "Te", 52,  52,  76)
        iodine        = particles.atom("Iodine",         "I",  53,  53,  74)
        xenon         = particles.atom("Xenon",          "Xe", 54,  54,  78)
        cesium        = particles.atom("Cesium",         "Cs", 55,  55,  78)
        barium        = particles.atom("Barium",         "Ba", 56,  56,  82)
        lanthanum     = particles.atom("Lanthanum",      "La", 57,  57,  82)
        cerium        = particles.atom("Cerium",         "Ce", 58,  58,  82)
        praseodymium  = particles.atom("Praseodymium",   "Pr", 59,  59,  82)
        neodymium     = particles.atom("Neodymium",      "Nd", 60,  60,  84)
        promethium    = particles.atom("Promethium",     "Pm", 61,  61,  84)
        samarium      = particles.atom("Samarium",       "Sm", 62,  62,  90)
        europium      = particles.atom("Europium",       "Eu", 63,  63,  90)
        gadolinium    = particles.atom("Gadolinium",     "Gd", 64,  64,  94)
        terbium       = particles.atom("Terbium",        "Tb", 65,  65,  94)
        dysprosium    = particles.atom("Dysprosium",     "Dy", 66,  66,  98)
        holmium       = particles.atom("Holmium",        "Ho", 67,  67,  98)
        erbium        = particles.atom("Erbium",         "Er", 68,  68,  98)
        thulium       = particles.atom("Thulium",        "Tm", 69,  69, 100)
        ytterbium     = particles.atom("Ytterbium",      "Yb", 70,  70, 104)
        lutetium      = particles.atom("Lutetium",       "Lu", 71,  71, 104)
        hafnium       = particles.atom("Hafnium",        "Hf", 72,  72, 106)
        tantalum      = particles.atom("Tantalum",       "Ta", 73,  73, 108)
        tungsten      = particles.atom("Tungsten",       "W",  74,  74, 110)
        rhenium       = particles.atom("Rhenium",        "Re", 75,  75, 112)
        osmium        = particles.atom("Osmium",         "Os", 76,  76, 116)
        iridium       = particles.atom("Iridium",        "Ir", 77,  77, 116)
        platinum      = particles.atom("Platinum",       "Pt", 78,  78, 117)
        gold          = particles.atom("Gold",           "Au", 79,  79, 118)
        mercury       = particles.atom("Mercury",        "Hg", 80,  80, 122)
        thallium      = particles.atom("Thallium",       "Tl", 81,  81, 124)
        lead          = particles.atom("Lead",           "Pb", 82,  82, 126)
        bismuth       = particles.atom("Bismuth",        "Bi", 83,  83, 126)
        polonium      = particles.atom("Polonium",       "Po", 84,  84, 126)
        astatine      = particles.atom("Astatine",       "At", 85,  85, 125)
        radon         = particles.atom("Radon",          "Rn", 86,  86, 136)
        francium      = particles.atom("Francium",       "Fr", 87,  87, 136)
        radium        = particles.atom("Radium",         "Ra", 88,  88, 138)
        actinium      = particles.atom("Actinium",       "Ac", 89,  89, 138)
        thorium       = particles.atom("Thorium",        "Th", 90,  90, 142)
        protactinium  = particles.atom("Protactinium",   "Pa", 91,  91, 140)
        uranium       = particles.atom("Uranium",        "U",  92,  92, 146)
        neptunium     = particles.atom("Neptunium",      "Np", 93,  93, 144)
        plutonium     = particles.atom("Plutonium",      "Pu", 94,  94, 150)
        americium     = particles.atom("Americium",      "Am", 95,  95, 148)
        curium        = particles.atom("Curium",         "Cm", 96,  96, 151)
        berkelium     = particles.atom("Berkelium",      "Bk", 97,  97, 150)
        californium   = particles.atom("Californium",    "Cf", 98,  98, 153)
        einsteinium   = particles.atom("Einsteinium",    "Es", 99,  99, 153)
        fermium       = particles.atom("Fermium",        "Fm",100, 100, 157)
        mendelevium   = particles.atom("Mendelevium",    "Md",101, 101, 157)
        nobelium      = particles.atom("Nobelium",       "No",102, 102, 157)
        lawrencium    = particles.atom("Lawrencium",     "Lr",103, 103, 159)
        rutherfordium = particles.atom("Rutherfordium",  "Rf",104, 104, 161)
        dubnium       = particles.atom("Dubnium",        "Db",105, 105, 163)
        seaborgium    = particles.atom("Seaborgium",     "Sg",106, 106, 163)
        bohrium       = particles.atom("Bohrium",        "Bh",107, 107, 163)
        hassium       = particles.atom("Hassium",        "Hs",108, 108, 162)
        meitnerium    = particles.atom("Meitnerium",     "Mt",109, 109, 169)
        darmstadtium  = particles.atom("Darmstadtium",   "Ds",110, 110, 171)
        roentgenium   = particles.atom("Roentgenium",    "Rg",111, 111, 170)
        copernicium   = particles.atom("Copernicium",    "Cn",112, 112, 173)
        nihonium      = particles.atom("Nihonium",       "Nh",113, 113, 173)
        flerovium     = particles.atom("Flerovium",      "Fl",114, 114, 175)
        moscovium     = particles.atom("Moscovium",      "Mc",115, 115, 174)
        livermorium   = particles.atom("Livermorium",    "Lv",116, 116, 177)
        tennessine    = particles.atom("Tennessine",     "Ts",117, 117, 177)
        oganesson     = particles.atom("Oganesson",      "Og",118, 118, 176)

        self.table = [
            hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen, oxygen,
            fluorine, neon, sodium, magnesium, aluminum, silicon, phosphorus, sulfur,
            chlorine, argon, potassium, calcium, scandium, titanium, vanadium, chromium,
            manganese, iron, cobalt, nickel, copper, zinc, gallium, germanium, arsenic,
            selenium, bromine, krypton, rubidium, strontium, yttrium, zirconium, niobium,
            molybdenum, technetium, ruthenium, rhodium, palladium, silver, cadmium, indium,
            tin, antimony, tellurium, iodine, xenon, cesium, barium, lanthanum, cerium,
            praseodymium, neodymium, promethium, samarium, europium, gadolinium, terbium,
            dysprosium, holmium, erbium, thulium, ytterbium, lutetium, hafnium, tantalum,
            tungsten, rhenium, osmium, iridium, platinum, gold, mercury, thallium, lead,
            bismuth, polonium, astatine, radon, francium, radium, actinium, thorium,
            protactinium, uranium, neptunium, plutonium, americium, curium, berkelium,
            californium, einsteinium, fermium, mendelevium, nobelium, lawrencium,
            rutherfordium, dubnium, seaborgium, bohrium, hassium, meitnerium, darmstadtium,
            roentgenium, copernicium, nihonium, flerovium, moscovium, livermorium,
            tennessine, oganesson
        ]

    def print_table(self):
        for element in self.table:
            print(element.atomName)

    def element_exists(self, symbol):
        for element in self.table:
            if element.symbol == symbol:
                return True
        return False
