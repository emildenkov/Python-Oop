from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def expenses(self) -> int:
        return 250_000

    @property
    def sponsors(self):
        return {
            "Oracle": {
                1: 1_500_000,
                2: 800_000
            },
            "Honda": {
                8: 20_000,
                10: 10_000
            }
        }

