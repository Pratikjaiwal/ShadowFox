friends_names = ["Alice", "Bob", "Catherine", "David", "Elena"]
friends_tuples = [(friend, len(friend)) for friend in friends_names]
print("List of friends with their name lengths:")
for friend_tuple in friends_tuples:
    print(friend_tuple)
