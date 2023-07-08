def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [badge_maker(i) for i in names]
    
def assign_rooms(names):
    assigned = [f"Hello, {j}! You'll be assigned to room {i+1}!" for i, j in enumerate(names)]
    return assigned
    
def printer(names):
    badges = batch_badge_creator(names)
    assigned = assign_rooms(names)

    # for i in range(len(badges)):
    #     print(badges[i])
    # for i in range(len(assigned)):
    #     print(assigned[i])

    for i in badges:
        print(i)
    for i in assigned:
        print(i)
