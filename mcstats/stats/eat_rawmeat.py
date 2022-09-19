from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_rawmeat',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:porkchop']),
            mcstats.StatReader(['minecraft:used','minecraft:beef']),
            mcstats.StatReader(['minecraft:used','minecraft:chicken']),
            mcstats.StatReader(['minecraft:used','minecraft:mutton']),
            mcstats.StatReader(['minecraft:used','minecraft:rabbit']),
            mcstats.StatReader(['minecraft:used','minecraft:minced_beef']),
            mcstats.StatReader(['minecraft:used','minecraft:chicken_cuts']),
            mcstats.StatReader(['minecraft:used','minecraft:bacon']),
            mcstats.StatReader(['minecraft:used','minecraft:mutton_chops']),
            mcstats.StatReader(['minecraft:used','minecraft:frog_leg'])
        ])
    ))
