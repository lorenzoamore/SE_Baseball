from dataclasses import dataclass


@dataclass
class Team:
    name : str
    team_code : str
    salary : float

    def __str__(self):
        return f"{self.team_code} ({self.name}) salario: {self.salary}"

    def __hash__(self):
        return hash(self.name)
