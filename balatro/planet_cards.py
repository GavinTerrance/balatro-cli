from enum import Enum

class PlanetCardType(Enum):
    PLUTO = "Pluto"
    MERCURY = "Mercury"
    URANUS = "Uranus"
    VENUS = "Venus"
    SATURN = "Saturn"
    JUPITER = "Jupiter"
    EARTH = "Earth"
    MARS = "Mars"
    NEPTUNE = "Neptune"
    PLANET_X = "Planet X"
    CERES = "Ceres"
    ERIS = "Eris"

class PlanetCard:
    def __init__(self, name: str, chips_bonus: int, mult_bonus: int, poker_hand_type: str, cost: int = 0):
        self.name = name
        self.chips_bonus = chips_bonus
        self.mult_bonus = mult_bonus
        self.poker_hand_type = poker_hand_type
        self.cost = cost

    def __repr__(self):
        return f"PlanetCard(name='{self.name}')"

    def apply_effect(self, game):
        # This will be implemented later when poker hand leveling is in place
        print(f"{self.name} used: Levels up {self.poker_hand_type} (effect not yet implemented).")

# --- Implementations for each Planet Card ---

class Pluto(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.PLUTO.value,
            chips_bonus=10,
            mult_bonus=1,
            poker_hand_type="High Card"
        )

class Mercury(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.MERCURY.value,
            chips_bonus=15,
            mult_bonus=1,
            poker_hand_type="Pair"
        )

class Uranus(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.URANUS.value,
            chips_bonus=20,
            mult_bonus=1,
            poker_hand_type="Two Pair"
        )

class Venus(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.VENUS.value,
            chips_bonus=20,
            mult_bonus=2,
            poker_hand_type="Three of a Kind"
        )

class Saturn(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.SATURN.value,
            chips_bonus=30,
            mult_bonus=3,
            poker_hand_type="Straight"
        )

class Jupiter(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.JUPITER.value,
            chips_bonus=15,
            mult_bonus=2,
            poker_hand_type="Flush"
        )

class Earth(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.EARTH.value,
            chips_bonus=25,
            mult_bonus=2,
            poker_hand_type="Full House"
        )

class Mars(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.MARS.value,
            chips_bonus=30,
            mult_bonus=3,
            poker_hand_type="Four of a Kind"
        )

class Neptune(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.NEPTUNE.value,
            chips_bonus=40,
            mult_bonus=4,
            poker_hand_type="Straight Flush"
        )

class PlanetX(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.PLANET_X.value,
            chips_bonus=35,
            mult_bonus=3,
            poker_hand_type="Five of a Kind"
        )

class Ceres(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.CERES.value,
            chips_bonus=40,
            mult_bonus=4,
            poker_hand_type="Flush House"
        )

class Eris(PlanetCard):
    def __init__(self):
        super().__init__(
            name=PlanetCardType.ERIS.value,
            chips_bonus=50,
            mult_bonus=3,
            poker_hand_type="Flush Five"
        )
