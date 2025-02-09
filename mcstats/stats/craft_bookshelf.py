from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_bookshelf',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
        ['minecraft:crafted'],
        [
            '.+:.*bookshelf',
        ])
    ))
