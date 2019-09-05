# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = room

    def change_room(self, new_room):
        self.room = new_room

    def __str__(self):
        return f'Player: {self.name}\nRoom: {self.room}'

    def __repr__(self):
        return f'Player({repr(self.name)}, {repr(self.room)})'