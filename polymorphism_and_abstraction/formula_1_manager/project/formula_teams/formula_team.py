from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    MIN_BUDGET_FOR_PARTICIPATION = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def expenses(self) -> int:
        ...

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.MIN_BUDGET_FOR_PARTICIPATION:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for sponsor in self.sponsors.values():
            for reward_pos in sponsor:
                if race_pos <= reward_pos:
                    revenue += sponsor[reward_pos]
                    break

        revenue -= self.expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"


