from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_cachalot',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','alexsmobs:cachalot_whale'])
        ])
    ))
