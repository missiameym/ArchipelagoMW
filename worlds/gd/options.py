from dataclasses import dataclass

from Options import Choice, Range, Toggle, DeathLink, DefaultOnToggle, OptionGroup, PerGameCommonOptions

class MinDiff(Choice):
	"""
	A choice option to set the minimum difficulty level for the game.
	"""
	display_name = "Minimum Difficulty"
	option_easy = 1
	option_medium = 2
	option_hard = 3
	default = 1

class LevelAmount(Range):
	"""
	Set the maximum amount of levels that you can unlock.
	HAS TO BE LARGER THAN GOAL AMOUNT.
	"""
	display_name = "Level Amount"
	range_start = 1
	range_end = 100
	default = 20

class GoalAmount(Range):
	"""
	Set the amount of levels that you will need to finish completely.
	"""
	display_name = "Goal Amount"
	range_start = 1
	range_end = 100
	default = 5

class ChecksPerLevel(Range):
	range_start = 1
	range_end = 20
	default = 5

@dataclass
class GDOptions(PerGameCommonOptions):
	min_diff: MinDiff
	level_amount: LevelAmount
	goal_amount: GoalAmount
	checks_per_level: ChecksPerLevel