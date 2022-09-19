from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_nightmare',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:killed','alexsmobs:centipede_head']),
            mcstats.StatReader(['minecraft:killed','alexsmobs:crimson_mosquito']),
            mcstats.StatReader(['minecraft:killed','alexsmobs:tarantula_hawk']),
            mcstats.StatReader(['minecraft:killed','alexsmobs:void_worm']),
            mcstats.StatReader(['minecraft:killed','alexsmobs:mungus']),
            mcstats.StatReader(['minecraft:killed','alexsmobs:cosmaw']),
            mcstats.StatReader(['minecraft:killed','alexsmobs:laviathan']),
        ])
    ))
