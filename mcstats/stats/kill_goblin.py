from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'kill_goblin',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:killed'],
            [
                'goblinsanddungeons:.*'
            ])
    ))
