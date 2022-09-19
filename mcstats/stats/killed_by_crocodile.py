from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'killed_by_crocodile',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed_by','alexsmobs:crocodile'])
        ])
    ))
