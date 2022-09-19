from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'least_deaths',
        {
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:deaths']),
        reversedSort = False,
        includeZero = True
    ))