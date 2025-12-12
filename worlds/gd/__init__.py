import json
import os

from Utils import visualize_regions
from worlds.AutoWorld import World, WebWorld
from BaseClasses import ItemClassification, Region, Location, Item, Tutorial, MultiWorld
from typing import Dict, Any

from .Items import GDItem, create_gd_items
from .Levels import level_table
from .Locations import location_table
from .Regions import create_gd_regions
from .options import GDOptions

class GDWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide for setting up Geometry Dash to be played in Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Sputnik Dev Team"]
    )]


def generate_locations():
    generated_locations = {}
    for i in range(100):
        for j in range(20):
            generated_locations[f"Level { i + 1 } - {(j+1)*5}% Complete"] = 0x100 + i * 100 + j
    return generated_locations


def generate_items():
    generated_items = {}
    for i in range(100):
        generated_items[f"Progressive Level { i + 1 }"] = 0x100 + (i + 1) * 100
    generated_items["Filler"] = 1
    return generated_items

items = generate_items()
locations = generate_locations()

class GDWorld(World):
    """
    Jump and fly your way through danger in this rhythm-based action platformer!
    Minimal implementation: mappings, item creation, regions, locations, itempool and completion condition.
    """
    game = "Geometry Dash"
    web = GDWebWorld()
    options_dataclass = GDOptions
    options: GDOptions

    item_name_to_id = items
    location_name_to_id = locations

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.itempool = []
        for name in items.keys():
            print(name)

    def create_item(self, name: str) -> "Item":
        item_id = self.item_name_to_id[name]
        return GDItem(name, ItemClassification.progression, item_id, player=self.player)

    def create_items(self) -> None:
        create_gd_items(self)
        self.multiworld.push_precollected(self.create_item("Progressive Level 1"))

    def create_regions(self) -> None:
        create_gd_regions(self)

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Level Complete", self.player, self.options.goal_amount)