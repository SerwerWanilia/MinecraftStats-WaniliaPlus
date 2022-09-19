from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_racoon',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','alexsmobs:crow'])
        ])
    ))