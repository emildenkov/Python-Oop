from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)

        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)

        else:
            raise ValueError("Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self,race_name: str, red_bull_pos: int, mercedes_pos: int) -> str:
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        return self.race_data(race_name, red_bull_pos, mercedes_pos)

    def race_data(self, race_name: str, red_bull_pos: int, mercedes_pos: int) -> str:
        better_pos = "Mercedes" if mercedes_pos < red_bull_pos else "Red Bull"

        red_bull_rev = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_rev = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return (f"Red Bull: {red_bull_rev}. "
                f"Mercedes: {mercedes_rev}. "
                f"{better_pos} is ahead at the {race_name} race.")




