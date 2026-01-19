"""
Q3: Event Overload Detector

You are analyzing activity logs from a system where users trigger events over time.

Each event contains:
- a `user_id` (integer)
- a `timestamp` (in seconds)

A user is considered **overloaded** if they generate **too many events in a
short period of time**.

Specifically, a user is overloaded if **three or more of their events occur
within any 10-second time window**.

Your task is to identify all such users.

Return a set containing the `user_id`s of all overloaded users.

If no user is overloaded, return an empty set.

Examples:
---------
Input:
events = [
    (1, 10),  # user 1 at time 10
    (1, 12),  # user 1 at time 12
    (1, 18),  # user 1 at time 18
    (2, 5),   # user 2 at time 5
    (2, 20),  # user 2 at time 20
    (3, 1),   # user 3 at time 1
    (3, 2),   # user 3 at time 2
    (3, 3)    # user 3 at time 3
]

Output: {1, 3}

Explanation:
- User 1: Events at [10, 12, 18]
  - From 10 to 18 is 8 seconds, contains 3 events → OVERLOADED
- User 2: Events at [5, 20]
  - Only 2 events, not overloaded
- User 3: Events at [1, 2, 3]
  - From 1 to 3 is 2 seconds, contains 3 events → OVERLOADED

Note: The window is "within 10 seconds", meaning timestamps[j] - timestamps[i] < 10
"""


def find_overloaded_users(events):
    """
    Identify users with 3+ events within any 10-second window.

    Args:
        events (list): List of tuples (user_id, timestamp)
                      where user_id is int and timestamp is int (seconds)

    Returns:
        set: Set of user_ids that are overloaded

    Examples:
        >>> find_overloaded_users([(1, 10), (1, 12), (1, 18), (3, 1), (3, 2), (3, 3)])
        {1, 3}
        >>> find_overloaded_users([])
        set()
        >>> find_overloaded_users([(1, 1), (1, 20), (1, 40)])
        set()
    """
    # arranging users based on their id
    user_events = {}
    for user_id, timestamp in events:
        if user_id not in user_events:
            user_events[user_id] = []
        user_events[user_id].append(timestamp)
    
    overloaded = set() # to store overloaded users
    
    for user_id, timestamps in user_events.items():
        # Sorting timestamps
        timestamps.sort()
        
        # checking for overload(>3 events in 10 sec)
        for i in range(len(timestamps)):
            count = 0
            for j in range(i, len(timestamps)):
                if timestamps[j] - timestamps[i] < 10:   # under 10 sec check
                    count += 1
                else:
                    break
                  
            # task counter>3
            if count >= 3:                 
                overloaded.add(user_id)
                break
    
    return overloaded


if __name__ == "__main__":
    # Test your solution here
    events = [
        (1, 10), (1, 12), (1, 18),
        (3, 1), (3, 2), (3, 3)
    ]
    print(find_overloaded_users(events))  # Should print: {1, 3}

    print(find_overloaded_users([]))  # Should print: set()

    print(find_overloaded_users([(1, 1), (1, 20), (1, 40)]))  # Should print: set()
    
    # custom tests
    print(find_overloaded_users([(2, 5), (2, 8), (2, 12), (2, 15), (2, 18)]))  # {2}
    print(find_overloaded_users([(2, 0), (2, 5), (2, 9), (4, 15), (4, 19), (4, 20)]))  # {2, 4}
