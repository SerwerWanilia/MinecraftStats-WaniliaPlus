from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'player_wealth',
        {
            'unit': 'int',
        },
        mcstats.StatReader(['waniliaplus','waniliaplus:playerMoney'])
    ))
