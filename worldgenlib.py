# worldgenlib.py
# Library file for the Cepheus Light World Generator by Omer Golan-Joel
# v0.5 - March 7th, 2020
# This is open source code, feel free to use it for any purpose
# For any questions, contact me at golan2072@gmail.com

# Import modules
import stellagama


# Functions

def atmo_gen(size):
    if size == 0:
        atmosphere = 0
    else:
        atmosphere = stellagama.dice(2, 6) - 7 + size
    if atmosphere > 15:
        atmosphere = 15
    if atmosphere < 0:
        atmosphere = 0
    return atmosphere


def hydro_gen(size, atmosphere):
    hydrographics = stellagama.dice(2, 6) - 7 + size
    if size <= 1:
        hydrographics = 0
    elif atmosphere in [0, 1, 10, 11, 12]:
        hydrographics -= 4
    elif atmosphere == 14:
        hydrographics -= 2
    if hydrographics < 0:
        hydrographics = 0
    if hydrographics > 10:
        hydrographics = 10
    return hydrographics


def pop_gen(atmosphere, hydrographics):
    population = stellagama.dice(2, 6) - 2
    if atmosphere >= 10:
        population -= 2
    elif atmosphere == 6:
        population += 3
    elif atmosphere in [5, 8]:
        population += 1
    if hydrographics == 0 and atmosphere < 3:
        population -= 1
    if population < 0:
        population = 0
    elif population > 10:
        population = 10
    return population


def gov_gen(population):
    government = stellagama.dice(2, 6) - 7 + population
    if population == 0:
        government = 0
    if government < 0:
        government = 0
    if government > 15:
        government = 15
    return government


def law_gen(government):
    law = stellagama.dice(2, 6) - 7 + government
    if government == 0:
        law = 0
    if law < 0:
        law = 0
    if law > 10:
        law = 10
    return law


def starport_gen(population):
    starport_roll = stellagama.dice(2, 6) - 7 + population
    starport = "X"
    if starport_roll <= 2:
        starport = "X"
    elif starport_roll in [3, 4]:
        starport = "E"
    elif starport_roll in [5, 6]:
        starport = "D"
    elif starport_roll in [7, 8]:
        starport = "C"
    elif starport_roll in [9, 10]:
        starport = "B"
    elif starport_roll >= 11:
        starport = "A"
    if population == 0:
        starport = "X"
    return starport


def tech_gen(uwp_dict):
    tech = stellagama.dice(1, 6)
    if uwp_dict["starport"] == "A":
        tech += 6
    elif uwp_dict["starport"] == "B":
        tech += 4
    elif uwp_dict["starport"] == "C":
        tech += 2
    elif uwp_dict["starport"] == "X":
        tech -= 4
    if uwp_dict["size"] in [0, 1]:
        tech += 2
    elif uwp_dict["size"] in range(1, 5):
        tech += 1
    if uwp_dict["atmosphere"] in range(0, 4):
        tech += 1
    elif uwp_dict["atmosphere"] >= 10:
        tech += 1
    if uwp_dict["hydrographics"] == 0:
        tech += 1
    elif uwp_dict["hydrographics"] in [9, 10]:
        tech += 1
    if uwp_dict["population"] in range(1, 6):
        tech += 1
    elif uwp_dict["population"] == 9:
        tech += 1
    elif uwp_dict["population"] == 10:
        tech += 2
    elif uwp_dict["population"] == 11:
        tech += 3
    elif uwp_dict["population"] >= 12:
        tech += 4
    if uwp_dict["government"] in [1, 5]:
        tech += 1
    elif uwp_dict["government"] == 7:
        tech += 2
    elif uwp_dict["government"] in [13, 14]:
        tech -= 2
    if uwp_dict["hydrographics"] in [0, 10] and uwp_dict["population"] >= 6 and uwp_dict["tl"] < 4:
        tech = 4
    if uwp_dict["atmosphere"] in [4, 7, 9] and tech < 5:
        tech = 5
    elif uwp_dict["atmosphere"] in [0, 1, 2, 3, 10, 11, 12] and uwp_dict["tl"] < 7:
        tech = 7
    if uwp_dict["atmosphere"] in [13, 14] and uwp_dict["hydrographics"] == 10 and uwp_dict["tl"] < 7:
        tech = 7
    if tech < 0:
        tech = 0
    return tech


def zone_gen(uwp_dict):
    if uwp_dict["atmosphere"] >= 10:
        if stellagama.dice(2, 6) >= 9:
            return "A"
        else:
            return " "
    if uwp_dict["government"] in [0, 7, 10]:
        if stellagama.dice(2, 6) >= 9:
            return "A"
        else:
            return " "
    if uwp_dict["law"] == 0 or uwp_dict["law"] >= 9:
        if stellagama.dice(2, 6) >= 9:
            return "A"
        else:
            return " "
    else:
        return " "


def gas_gen():
    if stellagama.dice(2, 6) >= 5:
        return "G"
    else:
        return " "


def base_gen(starport):
    naval = False
    scout = False
    pirate = False
    if starport in ["A", "B"] and stellagama.dice(2, 6) >=8:
        naval = True
    if starport in ["A", "B", "C", "D"]:
        scout_presence = stellagama.dice(2, 6)
        if starport == "C":
            scout_presence -= 1
        elif starport == "B":
            scout_presence -= 2
        elif starport == "A":
            scout_presence -= 3
        if scout_presence >= 7:
            scout = True
    if starport != "A" and naval == False:
        if stellagama.dice(2, 6) >= 12:
            pirate = True
    if naval and not scout:
        base = "N"
    elif scout and not naval:
        base = "S"
    elif scout and naval:
        base = "A"
    elif pirate and not scout:
        base = "P"
    elif pirate and scout:
        base = "T"
    else:
        base = " "
    return base


def trade_gen(uwp_dict):
    trade_list = []
    if uwp_dict["atmosphere"] in range(4, 10) and uwp_dict["hydrographics"] in range(4, 9) and uwp_dict["population"] in range(5, 8):
        trade_list.append("Ag")
    if uwp_dict["size"] == 0:
        trade_list.append("As")
    if uwp_dict["population"] == 0:
        trade_list.append("Ba")
    if uwp_dict["atmosphere"] >= 2 and uwp_dict["hydrographics"] == 0:
        trade_list.append("De")
    if uwp_dict["atmosphere"] >= 10 and uwp_dict["hydrographics"] > 0:
        trade_list.append("Fl")
    if uwp_dict["atmosphere"] in [5, 6, 8] and uwp_dict["hydrographics"] in range(4, 10) and uwp_dict["population"] in range(4, 9):
        trade_list.append("Ga")
    if uwp_dict["population"] >= 9:
        trade_list.append("Hi")
    if uwp_dict["tl"] >= 12:
        trade_list.append("Ht")
    if uwp_dict["atmosphere"] <= 1 and uwp_dict["hydrographics"] >= 1:
        trade_list.append("Ic")
    if uwp_dict["atmosphere"] in [0, 1, 2, 4, 7, 9] and uwp_dict["population"] >= 9:
        trade_list.append("In")
    if uwp_dict["population"] in range(1, 4):
        trade_list.append("Lo")
    if uwp_dict["tl"] <= 5:
        trade_list.append("Lt")
    if uwp_dict["atmosphere"] <= 3 and uwp_dict["hydrographics"] <= 3 and uwp_dict["population"] >= 6:
        trade_list.append("Na")
    if uwp_dict["population"] in range(4, 7):
        trade_list.append("Ni")
    if uwp_dict["atmosphere"] in range(2, 6) and uwp_dict["hydrographics"] <= 3:
        trade_list.append("Po")
    if uwp_dict["atmosphere"] in [6, 8] and uwp_dict["population"] in range(6, 9):
        trade_list.append("Ri")
    if uwp_dict["hydrographics"] >= 10:
        trade_list.append("Wa")
    if uwp_dict["atmosphere"] <= 0:
        trade_list.append("Va")
    return trade_list


# Classes

class World:

    def __init__(self):
        self.uwp_dict = {"starport": "X", "size": stellagama.dice(2, 6) - 2, "atmosphere": 0, "hydrographics": 0,
                         "population": 0, "government": 0, "law": 0, "tl": 0}
        self.uwp_dict["atmosphere"] = atmo_gen(self.uwp_dict["size"])
        self.uwp_dict["hydrographics"] = hydro_gen(self.uwp_dict["size"], self.uwp_dict["atmosphere"])
        self.uwp_dict["population"] = pop_gen(self.uwp_dict["atmosphere"], self.uwp_dict["hydrographics"])
        self.uwp_dict["government"] = gov_gen(self.uwp_dict["population"])
        self.uwp_dict["law"] = law_gen(self.uwp_dict["government"])
        self.uwp_dict["starport"] = starport_gen(self.uwp_dict["population"])
        self.uwp_dict["tl"] = tech_gen(self.uwp_dict)
        self.hex_uwp = {"starport": self.uwp_dict["starport"], "size": stellagama.pseudo_hex(self.uwp_dict["size"]),
                        "atmosphere": stellagama.pseudo_hex(self.uwp_dict["atmosphere"]),
                        "hydrographics": stellagama.pseudo_hex(self.uwp_dict["hydrographics"]),
                        "population": stellagama.pseudo_hex(self.uwp_dict["population"]),
                        "government": stellagama.pseudo_hex(self.uwp_dict["government"]),
                        "law": stellagama.pseudo_hex(self.uwp_dict["law"]),
                        "tl": stellagama.pseudo_hex(self.uwp_dict["tl"])}
        self.zone = zone_gen(self.uwp_dict)
        self.gas_giants = gas_gen()
        self.base = base_gen(self.uwp_dict["starport"])
        self.trade_list = trade_gen(self.uwp_dict)
        self.trade_string = " ".join(self.trade_list)

    def print_raw_uwp(self):
        print(self.uwp_dict["starport"], self.uwp_dict["size"], self.uwp_dict["atmosphere"],
              self.uwp_dict["hydrographics"], self.uwp_dict["population"], self.uwp_dict["government"],
              self.uwp_dict["law"], "-", self.uwp_dict["tl"])

    def print_uwp(self):
        print(
            f"{self.hex_uwp['starport']}{self.hex_uwp['size']}{self.hex_uwp['atmosphere']}{self.hex_uwp['hydrographics']}{self.hex_uwp['population']}{self.hex_uwp['government']}{self.hex_uwp['law']}-{self.hex_uwp['tl']} {self.base}   {self.zone}   {self.gas_giants}   {self.trade_string}  ")

    def get_uwp_string(self):
        return (
            f"{self.hex_uwp['starport']}{self.hex_uwp['size']}{self.hex_uwp['atmosphere']}{self.hex_uwp['hydrographics']}{self.hex_uwp['population']}{self.hex_uwp['government']}{self.hex_uwp['law']}-{self.hex_uwp['tl']}")


# Test area
