from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'tank',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:damage_blocked_by_shield']),
            mcstats.StatReader(['minecraft:custom','minecraft:damage_resisted'])
        ])
    ))