from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_egg',
        {
            'unit': 'int',
        },
	mcstats.StatSumReader([
        	mcstats.StatReader(['minecraft:used','minecraft:egg']),
		mcstats.StatReader(['minecraft:used','alexsmobs:emu_egg']),
	])
    ))
