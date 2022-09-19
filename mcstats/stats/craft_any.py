from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_any',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
            [
                '.+:.+',
            ])
    ))
