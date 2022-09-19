from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_hamburger',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:crafted','farmersdelight:hamburger'])
        ])
    ))
