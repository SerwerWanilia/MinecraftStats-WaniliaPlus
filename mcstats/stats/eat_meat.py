from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_meat',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:cooked_porkchop']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_beef']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_chicken']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_mutton']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_rabbit']),
            mcstats.StatReader(['minecraft:used','minecraft:porkchop']),
            mcstats.StatReader(['minecraft:used','minecraft:beef']),
            mcstats.StatReader(['minecraft:used','minecraft:chicken']),
            mcstats.StatReader(['minecraft:used','minecraft:mutton']),
            mcstats.StatReader(['minecraft:used','minecraft:rabbit']),
            mcstats.StatReader(['minecraft:used','farmersdelight:minced_beef']),
            mcstats.StatReader(['minecraft:used','minecraft:beef_patty']),
            mcstats.StatReader(['minecraft:used','minecraft:barbecue_stick']),
            mcstats.StatReader(['minecraft:used','minecraft:dumplings']),
            mcstats.StatReader(['minecraft:used','minecraft:stuffed_potato']),
            mcstats.StatReader(['minecraft:used','minecraft:noodle_soup']),
            mcstats.StatReader(['minecraft:used','minecraft:shepherds_pie']),
            mcstats.StatReader(['minecraft:used','minecraft:dog_food']),
            mcstats.StatReader(['minecraft:used','minecraft:rabbit_stew']),
        mcstats.StatSumMatchReader(
            ['minecraft:used'],
            [
            'farmersdelight:.*beef.*',
            'farmersdelight:.*chicken.*',
            'farmersdelight:.*meat.*',
            'farmersdelight:.*bacon.*',
            'farmersdelight:.*ham.*',
            'farmersdelight:.*mutton.*',
            'farmersdelight:.*steak.*',
            ])
        ])
    ))
