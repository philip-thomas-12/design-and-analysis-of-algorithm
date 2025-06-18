def activity_selection(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = []
    last_end_time = -1
    
    for start, end in activities:
        if start > last_end_time:
            selected.append((start, end))
            last_end_time = end
    
    return selected

# Example
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]

selected = activity_selection(activities)
print("Selected Activities:", selected)
