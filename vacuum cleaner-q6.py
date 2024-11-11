def vacuum_cleaner(room_states, start_position):
    position = start_position
    actions = []
    
    while any(room_states):
        if room_states[position] == 1:
            room_states[position] = 0  # Clean the room
            actions.append(f"Cleaned room {position}")
        else:
            actions.append(f"Room {position} is already clean")
        
        # Move to the next room (assuming a 2-room setup)
        position = 1 - position
        actions.append(f"Moved to room {position}")
        
    return actions

# User input
room_states = [
    int(input("Enter state for Room 0 (1 for dirty, 0 for clean): ")),
    int(input("Enter state for Room 1 (1 for dirty, 0 for clean): "))
]
start_position = int(input("Enter starting position (0 for Room 0, 1 for Room 1): "))

# Run the vacuum cleaner program and print actions
actions = vacuum_cleaner(room_states, start_position)
print("\nActions taken by the vacuum cleaner:")
for action in actions:
    print(action)
