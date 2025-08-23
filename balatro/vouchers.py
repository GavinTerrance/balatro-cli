# balatro/vouchers.py

class Voucher:
    """Base class for all Vouchers."""
    def __init__(self, name: str, description: str, cost: int):
        self.name = name
        self.description = description
        self.cost = cost

    def __repr__(self):
        return f"Voucher(name='{self.name}', cost={self.cost})"

    def apply_effect(self, game): # Game object passed to apply effects
        """Applies the voucher's effect to the game state."""
        pass

    def to_dict(self):
        return {
            "_class": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "cost": self.cost
        }

    @classmethod
    def from_dict(cls, data):
        # This will be a generic from_dict for the base Voucher class
        # Subclasses will need their own from_dict or a more sophisticated factory
        # For now, it will only handle the base Voucher attributes
        return cls(data["name"], data["description"], data["cost"])

# --- Example Voucher Implementations ---

class TarotMerchant(Voucher):
    def __init__(self):
        super().__init__(
            name="Tarot Merchant",
            description="Tarot cards appear in the shop.",
            cost=4
        )

    def apply_effect(self, game):
        # Placeholder for future shop integration
        print(f"{self.name} activated: Tarot cards now appear in shop.")

class CardSharp(Voucher):
    def __init__(self):
        super().__init__(
            name="Card Sharp",
            description="First hand of each round gets +2 Mult.",
            cost=4
        )

    def apply_effect(self, game):
        # This effect would need to be checked at the start of each round
        # and applied to the first hand played.
        print(f"{self.name} activated: First hand of each round gets +2 Mult.")

class Honeypot(Voucher):
    def __init__(self):
        super().__init__(
            name="Honeypot",
            description="Gain $10 when you sell a Joker.",
            cost=4
        )

    def apply_effect(self, game):
        # This effect would need to be triggered when a Joker is sold.
        print(f"{self.name} activated: Gain $10 when you sell a Joker.")

VOUCHER_CLASSES = {
    "Voucher": Voucher,
    "TarotMerchant": TarotMerchant,
    "CardSharp": CardSharp,
    "Honeypot": Honeypot
}

def voucher_from_dict(data):
    voucher_class = VOUCHER_CLASSES[data["_class"]]
    return voucher_class(data["name"], data["description"], data["cost"])
