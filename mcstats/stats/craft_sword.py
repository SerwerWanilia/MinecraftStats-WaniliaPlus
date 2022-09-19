from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_sword',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            ['minecraft:.+_sword',
            'nourished_end:voidsteel_sword',
            'additionaladditions:.+_sword',
            'alloyed:.+_sword',
            'botania:.+_sword'
	])
    ))
