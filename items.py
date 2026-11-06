from BaseClasses import Item
from typing import NamedTuple
from .names import (gravity_hold, water_wave, power_stone, gyro_attack, star_crash, charge_kick, napalm_bomb,
                    crystal_eye, rush_coil, rush_jet, super_arrow, beat, charge_buster,
                    gravity_man_stage, wave_man_stage, stone_man_stage, gyro_man_stage, star_man_stage,
                    charge_man_stage, napalm_man_stage, crystal_man_stage, proto_man_1_stage, proto_man_2_stage, proto_man_3_stage,
                    proto_man_4_stage, e_tank, weapon_energy, health_energy, one_up)
#TODO: ALL NAMES HERE

class ItemData(NamedTuple):
    code: int
    progression: bool
    useful: bool = False  # primarily use this for incredibly useful items of their class, like Metal Blade
    skip_balancing: bool = False


class MM6Item(Item):
    game = "Mega Man 6"


robot_master_weapon_table = {
    yamato_spear: ItemData(0x0001, True,True),
    knight_crusher: ItemData(0x0002, True),
    centaur_flash: ItemData(0x0003, True),
    wind_storm: ItemData(0x0004, True),
    flame_blast: ItemData(0x0005, True),
    blizzard_attack: ItemData(0x0006, True),
    plant_barrier: ItemData(0x0007, True),
    silver_tomahawk: ItemData(0x0008, True),
}

stage_access_table = {
    yamato_man_stage: ItemData(0x0101, True),
    knight_man_stage: ItemData(0x0102, True),
    centaur_man_stage: ItemData(0x0103, True),
    wind_man_stage: ItemData(0x0104, True),
    flame_man_stage: ItemData(0x0105, True),
    blizzard_man_stage: ItemData(0x0106, True),
    plant_man_stage: ItemData(0x0107, True),
    tomahawk_man_stage: ItemData(0x0108, True),
    mr_x_1_stage: ItemData(0x0110, True, True),
    mr_x_2_stage: ItemData(0x0111, True, True),
    mr_x_3_stage: ItemData(0x0112, True, True),
    mr_x_4_stage: ItemData(0x0113, True, True),
}

extra_item_table = {
    rush_jet_adapter: ItemData(0x0011, True, True),
    rush_power_adapter: ItemData(0x0012, True, True),
    beat_b: ItemData(0x0014, True, True),
    beat_e: ItemData(0x0014, True, True),
    beat_a: ItemData(0x0014, True, True),
    beat_t: ItemData(0x0014, True, True),
    charge_buster: ItemData(0x0025, False, True),
}

filler_item_table = {
    one_up: ItemData(0x0020, False),
    weapon_energy_large: ItemData(0x0021, False),
    health_energy_large: ItemData(0x0022, False),
    weapon_energy_small: ItemData(0x0021, False),
    health_energy_small: ItemData(0x0022, False),
    e_tank: ItemData(0x0023, False, True),
}



filler_item_weights = {#TODO: COME BACK TO THESE RATIOS
    one_up: 1,
    weapon_energy_large: 2,
    health_energy_large: 2,
    weapon_energy_small: 4,
    health_energy_small: 4,
    e_tank: 1,
}

item_table = {
    **robot_master_weapon_table,
    **stage_access_table,
    **extra_item_table,
    **filler_item_table,
}

item_names = {
    "Weapons": {name for name in robot_master_weapon_table.keys()},
    "Stages": {name for name in stage_access_table.keys()},
    "Rush": {name for name in extra_item_table.keys() if "Rush" in name},
}

lookup_item_to_id: dict[str, int] = {item_name: data.code for item_name, data in item_table.items() if data.code}
