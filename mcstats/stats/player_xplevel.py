from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'player_xplevel',
        {
            'unit': 'int',
        },
        mcstats.StatReader(['waniliaplus','waniliaplus:playerXpLevel'])
    ))
