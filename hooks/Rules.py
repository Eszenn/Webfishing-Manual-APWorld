from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

from .Helpers import get_required_fish

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(world: World, multiworld: MultiWorld, state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def hasEnoughFish(world: World, multiworld: MultiWorld, state: CollectionState, player: int):

    progressive_rods = world.options.progressive_rods.value

    available_fish = 0

    fish_by_rod = {
        "Simple Fishing Rod": 7,
        "Traveler's Fishing Rod": 15,
        "Collector's Fishing Rod": 14,
        "Shining Collector's Fishing Rod": 12,
        "Glistening Collector's Fishing Rod": 6,
        "Opulent Collector's Fishing Rod": 7,
        "Radiant Collector's Fishing Rod": 4,
        "Alpha Collector's Fishing Rod": 4,
        "Prosperous Fishing Rod": 4,
        "Spectral Rod": 5
    }

    bait_count = state.count_group("Bait", player)

    if progressive_rods:
        number_of_rods = state.count("Progressive Fishing Rod", player)
        fish_numbers = list(fish_by_rod.values())

        for i in range(number_of_rods):
            for bait in range(bait_count):
                available_fish += fish_numbers[i]

        if state.has("Spectral Rod", player):
            for bait in range(bait_count):
                available_fish += fish_by_rod["Spectral Rod"]

    else:
        for rod, fish in fish_by_rod.items():
            for bait in range(bait_count):
                if state.has(rod, player):
                    available_fish += fish

    return available_fish >= get_required_fish(world)
