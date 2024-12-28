# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionSet

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith

class VictoryCondition(Choice):
    """When will your run be considered finished.
    Camp Tier 4: Requires collecting Camp Donations to level up the Camp to Tier 4.
    All Rare Fish: Requires collecting all 4 rare fish: Golden Bass, Golden Manta Ray, Leedsichthys, and Diamond.
    Fish 'em All: Requires collecting a certain percentage of fish. """
    option_camp_tier_4 = 0
    option_all_rare_fish = 1
    option_fish_em_all = 2


class ExtraDonations(Range):
    """Adds extra donation items to the item pool."""
    range_type = 0
    range_end = 10
    default = 0


class RequiredFishPercent(Range):
    """ What percentage of the total fish must be caught when doing Fish 'em All."""
    range_start = 20
    range_end = 100
    default = 40


class ProgressiveRods(Toggle):
    """Makes fishing rods progress linearly, so the value of fish will increase as you acquire each rod."""
    display_name = "Progressive Fishing Rods"


class ProgressiveBait(Toggle):
    """Makes bait progress linearly, so the quality of fish will increase as you acquire each type of bait."""
    display_name = "Progressive Bait"


class ExcludedFish(OptionSet):
    """Removes all locations that involve catching the fish listed here.
    The four rare fish cannot be removed if your goal is All Rare Fish.
    All fish names in game are valid keys, and are not case-sensitive."""
    display_name = "Excluded Fish"
    default = {}
    valid_keys = {
        "Angelfish", "Anomalocaris", "Atlantic Salmon", "Axolotl", "Bluefish", "Bluegill", "Bone", "Bowfin", "Branch",
        "Bull Shark", "Carp", "Catfish", "Clownfish", "Coelacanth", "Crab", "Crappie", "Crayfish", "CREATURE",
        "Diamond", "Dogfish", "Drink Rings", "Drum", "Eel", "Flounder", "Frog", "Gar", "Golden Bass",
        "Golden Manta Ray", "Goldfish", "Great White Shark", "Grouper", "Guppy", "Hammerhead Shark", "Helicoprion",
        "Herring", "Horseshoe Crab", "King Salmon", "Koi", "Krill", "Largemouth Bass", "Leech", "Leedsichthys",
        "Lionfish", "Lobster", "Man O' War", "Manta Ray", "Marlin", "Mooneye", "Muskellunge", "Octopus", "Old Boot",
        "Oyster", "Perch", "Pike", "Plastic Bag", "Pupfish", "Rainbow Trout", "Salmon", "Sawfish", "Sea Turtle",
        "Seahorse", "Shrimp", "Snail", "Soda Can", "Squid", "Sting Ray", "Sturgeon", "Sunfish", "Swordfish", "Toad",
        "Tuna", "Turtle", "Unidentified Fish Object", "Walleye", "Weed", "Whale", "Wolffish"
    }


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:

    options["victory_condition"] = VictoryCondition
    options["extra_donations"] = ExtraDonations
    options["required_fish_percent"] = RequiredFishPercent
    options["progressive_rods"] = ProgressiveRods
    options["progressive_bait"] = ProgressiveBait
    options["excluded_fish"] = ExcludedFish

    return options