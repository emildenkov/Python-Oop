class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self) -> str:
        skills = "\n".join(f"==={k} - {v}" for k, v in self.skills.items())
        return f"Name: {self.name}\n"\
               f"Guild: {self.guild}\n"\
               f"HP: {self.hp}\n" \
               f"MP: {self.mp}\n"\
               f"{skills}"

