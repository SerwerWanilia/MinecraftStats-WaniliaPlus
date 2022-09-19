from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_geode',
        {
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','tetra:block_geode'])
    ))
