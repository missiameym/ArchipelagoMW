from BaseClasses import Item, ItemClassification

class GDItem(Item):
    game: str = "Geometry Dash"

def create_gd_items(world):
    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    for i in range(world.options.level_amount):
        item_name = f"Progressive Level { i + 1 }"
        for j in range(world.options.checks_per_level):
            world.itempool.append(GDItem(item_name, ItemClassification.progression, world.item_name_to_id[item_name], world.player))
    for i in range(total_location_count - len(world.itempool)):
        world.itempool.append(GDItem("Filler", ItemClassification.filler, world.item_name_to_id["Filler"], world.player))

    world.multiworld.itempool += world.itempool