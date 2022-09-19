from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_crow',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','alexsmobs:crow'])
        ])
    ))