print("Welcome to the Dictionary App!")

us_states = {
    "OH" : "Ohio",
    "IN" : "indiana",
    "VA" : "Virginia",
    "TX" : "Texas",
    "CO" : "Colorado"
}
print(f"us_state dictionary - {us_states}")




state_abv = input("State (abbreviation)?")
if state_abv in us_states:
    print(f"state ({state_abv}): {us_states[state_abv]}")
else:
    print(f"{state_abv} does not exist!")

print("Add an entry to the dictionary: ")
us_states["AK"] = "Alaska"

print(f"us_states: {us_states}")

print("using the get method to retrieve a value: ")
print(f"CO: {us_states.get("CO")}")

print("Delete an entry from the dictionary")
state_delete = us_states.pop("CO")
print(f"CO removed: {us_states}")

print("="*20)
print("keys, items, values")
print(f"keys: {us_states.keys()}")
print(f"values: {us_states.values()}")
print(f"items: {us_states.items()}")

print("Unpacking a tuple as it looks through all keys/values")
for abbv, name in us_states.items():
    print(f"{abbv}: {name}")

print("sorted - unpacking a tuples as it loops through all keys/vales")
for abbv, name in sorted(us_states.items()):
    print(f"{abbv}: {name}")
print("bye")