
init python:
    class CharacterStats(BaseStatsObject):

        # Set the store.{prefix}.character_id value
        # STORE_PREFIX = "character_stats"

        # Boolean toggle for validation - defaults both True
        # VALIDATE_VALUES = False
        # COERCE_VALUES = False

        STAT_DEFAULTS = {
                'strength': 10,
                'intelligence': 10,
                'charisma': 10,
                'agility': 10,
                'endurance': 10,
                'luck': 10,
                'health': 100,
                'mana': 100,
                'stamina': 100,
                'level': 1,
                'experience': 0,
                'age': 10,
                'weight': 35,
                'height': 140
        }