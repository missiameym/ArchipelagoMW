from BaseClasses import Region, Entrance, Location, Item, ItemClassification
from worlds.gd import GDItem


def connect_regions(world, from_name: str, to_name: str, entrance_name: str, i) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    entrance = entrance_region.connect(exit_region, entrance_name)
    entrance.access_rule = lambda state, level=i + 1: state.has(f"Progressive Level { level }", world.player)
    return entrance


def create_gd_regions(world):
    region = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(region)

    for i in range(world.options.level_amount):
        region = Region(f"Level { i + 1 }", world.player, world.multiworld)
        percentage_per_check = 100 // world.options.checks_per_level

        for j in range(world.options.checks_per_level):
            location_name = f"Level { i + 1 } - {percentage_per_check * (j + 1)}% Complete"
            location = Location(
                world.player,
                location_name,
                world.location_name_to_id[location_name],
                region
            )

            location.access_rule = lambda state, level=i + 1, check=j + 1: state.has(f"Progressive Level { level }", world.player, check)
            region.locations.append(location)


        event_location = Location(world.player, f"Level { i + 1 } Complete", None, region)
        event_location.access_rule = lambda state, level=i + 1: state.has(f"Progressive Level { level }", world.player, world.options.checks_per_level)
        region.locations.append(event_location)
        event_location.place_locked_item(GDItem("Level Complete", ItemClassification.progression, None, world.player))

        world.multiworld.regions.append(region)
        connect_regions(world, "Menu", f"Level { i + 1 }", f"Menu -> Level { i + 1 }", i)