# WEBFISHING Manual APWorld
A manual APWorld for implementning WEBFISHING into the Archipelago randomizer.

## Locations
The following are all locations that must be checked:
- Catching a fish (one location for each quality, so 6 locations per fish)
- Completing quests (Unending quests excluded)

## Items
The following are all items that may be received:
- Fishing Rods
- Rod Upgrades
- Bait
- Fishing Buddies
- Fishing Buddy Upgrades
- Cosmetic Vouchers (Used to claim a cosmetic item from the shop)
- Consumable Vouchers (Used to claim a consumable item from the shop / vending machine)

## Goals
### Reach Camp Tier 4
Requires you to collect 10 donations for each tier ($10, $100, $500 respectively). The item pool has 10 of each donation by default, but more can be added with the "Extra Donations" YAML option.
### All Rare Fish
Requires you to catch all 4 "Rare Fish" - Being the Golden Bass, Golden Manta Ray, Leedsichthys, and Diamond.
- Fishing Rods are forced to "Progressive"
- The 4 "Rare Fish" are unable to be excluded in your YAML
### Fish 'em All
Requires completing a designated percentage of the journal (40% by default). The required percentage can be set from 20% to 100% in your YAML.
- The actual number of fish required varies depending on how many fish have been excluded.

## Custom YAML Options
### Victory Condition
Sets the victory condition for your world to one of the 3 mentioned above.

### Extra Donations
Sets how many extra donation items are added to the pool when your victory condition is set to "Camp Tier 4." Up to 10 extra donations may be added per tier.

### Required Fish Percent
Sets the percentage of the journal that must be completed when your victory condition is set to "Fish 'em All." The required percent can be set from 20% to 100%.

### Progressive Rods
If enabled, fishing rods will be made progressive. The Spectral Rod is excluded. Fishing rods will be obtained in the following order:
1. Simple Fishing Rod
2. Traveler's Fishing Rod
3. Collector's Fishing Rod
4. Shining Collector's Fishing Rod
5. Opulent Collector's Fishing Rod
6. Glistening Collector's Fishing Rod
7. Radiant Collector's Fishing Rod
8. Alpha Collector's Fishing Rod
9. Prosperous Fishing Rod

### Progressive Bait
If enabled, bait will be made progressive. Bait will be obtained in the following order:
1. Worms
2. Crickets
3. Leeches
4. Minnows
5. Squids
6. Nautiluses

### Excluded Fish
Any fish listed here will have all locations related to them removed. The 4 "Rare Fish" will not be removed if your victory condition is set to "All Rare Fish." 
