from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_ender_eye',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','endrem:black_eye']),
            mcstats.StatReader(['minecraft:used','endrem:cold_eye']),
            mcstats.StatReader(['minecraft:used','endrem:corrupted_eye']),
            mcstats.StatReader(['minecraft:used','endrem:lost_eye']),
            mcstats.StatReader(['minecraft:used','endrem:nether_eye']),
            mcstats.StatReader(['minecraft:used','endrem:old_eye']),
            mcstats.StatReader(['minecraft:used','endrem:rogue_eye']),
            mcstats.StatReader(['minecraft:used','endrem:cursed_eye']),
            mcstats.StatReader(['minecraft:used','endrem:evil_eye']),
            mcstats.StatReader(['minecraft:used','endrem:guardian_eye']),
            mcstats.StatReader(['minecraft:used','endrem:magical_eye']),
            mcstats.StatReader(['minecraft:used','endrem:wither_eye']),
            mcstats.StatReader(['minecraft:used','endrem:witch_eye']),
            mcstats.StatReader(['minecraft:used','endrem:undead_eye']),
            mcstats.StatReader(['minecraft:used','endrem:exotic_eye'])
        ])
    ))
