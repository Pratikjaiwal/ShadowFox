justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]
num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After recruiting Batgirl and Nightwing:", justice_league)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to the beginning:", justice_league)
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)
new_members = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league = new_members
print("After assembling a new team:", justice_league)
justice_league.sort()
new_leader = justice_league[0]
print("Sorted Justice League:", justice_league)
print("New Leader:", new_leader)
print("BONUS: The new leader is predicted to be:", new_leader)