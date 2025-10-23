# python
# warrior.py
class Warrior:
    def __init__(self, name, power, weapon):
        self.name = name
        self.power = power
        self.weapon = weapon

    def worthy(self):
        if self.power > self.weapon:
            return True
        elif self.power == self.weapon:
            print("Compatible")
            return True  # or None if you prefer
        else:
            return False

    def surge(self):
        return self.power * 2

    def dishonor(self):
        # clarify intended behavior; example resets name if dishonored flag provided
        self.name = ""
