def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    speaker_list = []
    for name in names:
        message = f"Hello, my name is {name}."
        speaker_list.append(message)
    return speaker_list

def assign_rooms(names):
    room_assignments = []
    room = 1
    for name in names:
        message = f"Hello, {name}! You'll be assigned to room {room}!"
        room_assignments.append(message)
        room += 1
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)

    for room in rooms:
        print(room)