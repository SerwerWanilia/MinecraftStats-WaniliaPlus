from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_tradingpost',
        {
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:crafted','calemieconomy:trading_post']),
    ))
