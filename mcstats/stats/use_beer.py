from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_beer',
        {
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            ['drinkbeer:beer_mug.*'])
    ))
