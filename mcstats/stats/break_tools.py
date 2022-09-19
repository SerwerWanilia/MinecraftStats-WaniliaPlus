# pylint: disable=duplicate-code
from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'break_tools',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:broken'],
            [
                'minecraft:.+_axe',
                'minecraft:.+_hoe',
                'minecraft:.+_pickaxe',
                'minecraft:.+_shovel',
                'minecraft:fishing_rod',
                'minecraft:flint_and_steel',
                'minecraft:shears',
		'additionaladditions:.+_axe',
		'additionaladditions:.+_hoe',
		'additionaladditions:.+_pickaxe',
		'additionaladditions:.+_shovel',
		'botania:.+_axe',
		'botania:.+_hoe',
		'botania:.+_pickaxe',
		'botania:.+_shovel',
		'alloyed:.+_axe',
		'alloyed:.+_hoe',
		'alloyed:.+_pickaxe',
		'alloyed:.+_shovel',
		'nourished_end:.+_axe',
		'nourished_end:.+_hoe',
		'nourished_end:.+_pickaxe',
		'nourished_end:.+_shovel',
		'farmersdelight:.+_knife',
            ])
    ))
