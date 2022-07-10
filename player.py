class Player:

    def __init__(self, name: str, position: str, rating: str, age: int = None):
        self._name = name
        self._position = position
        self._rating = int(rating)
        self._age = age
        self._progress: float = 0
        self._set_position_type(position)

    def _set_position_type(self, position: str) -> None:
        """Assigns the position type of a player to one of Goalkeeper, Defender, Midfielder, or Forward."""
        if 'B' in position:
            self._position_type = 'D'
        elif 'M' in position:
            self._position_type = 'M'
        elif 'G' in position:
            self._position_type = 'G'
        else:
            self._position_type = 'F'

    @property
    def name(self):
        return self._name

    @property
    def position_type(self):
        return self._position_type

    @property
    def rating(self):
        return self._rating

    @property
    def age(self):
        return self._age

    def __str__(self) -> str:
        return f"{self._position} - {self._name} ({self._age}) [{self._rating}]"

class Prospect(Player):

    def __init__(self, name: str, position: str, rating: str, potential: int, age: int):
        super().__init__(name, position, rating, age)
        self._potential = potential

    def __str__(self) -> str:
        return f"{self._position} - {self._name} ({self._age}) [{self._rating}] | Potential: {self._potential}"
        