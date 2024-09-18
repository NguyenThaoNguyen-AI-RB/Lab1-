from project.room import Room
class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0
    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")
    def add_room(self, room: Room):
        self.rooms.append(room)
    def take_room(self, room_number: int, people: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            result = room.take_room(people)
            if result is None:
                self.guests += people
            else:
                return result
    def free_room(self, room_number: int):
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            if room.is_taken:
                self.guests -= room.guests
                room.free_room()
            else:
                return f"Room number {room_number} is not taken"
    def print_status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(free_rooms)}")
        print(f"Taken rooms: {', '.join(taken_rooms)}")