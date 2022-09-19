from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_wood',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],['minecraft:.+_log', 'minecraft:.+_stem', 'biomesoplenty:.+_log', 'botania:.+_log', 'quark:.+_log', 'nourished_end:.+_stem', 'nourished_end:.+_log', 'quark:.+_stem'])
    ))
