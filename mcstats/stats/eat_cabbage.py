from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_cabbage',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','farmersdelight:cabbage_rolls'])
        ])
    ))
