def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(names):
     badges = []
     for name in names:
        badges.append(badge_maker(name))
     return badges

def assign_rooms(names):
     room_assignments = []
     for index, name in enumerate(names):
        room_assignments.append("Hello, " + name + "! You'll be assigned to room " + str(index + 1) + "!")
     return room_assignments

def printer(names):
     badges = batch_badge_creator(names)
     room_assignments = assign_rooms(names)
     for badge, assignment in zip(badges, room_assignments):
        print(badge)
        print(assignment)