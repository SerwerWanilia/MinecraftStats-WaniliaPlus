from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_create',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                'create:.+'
            ])
    ))
