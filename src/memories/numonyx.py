""" numonyx.py: This provides SDRC parameters for Numonyx devices

"""

""" M65Kx002AM : SDRC parameters for a given SDRC clock rate

Device summary:
    M65G002AM -- 2Gb (4 banks x 8Mbits x 16)
    M65D002AM -- 2Gb (4 banks x 8Mbits x 32)

Datasheet : Are available from your local Numonyx distributor
 
"""
m65kx002am = [
        {
        "tCK" : 5,
        "tRFC" : 140, "tRC" : 55, "tRAS" : 40, "tRP" : 15, "tRCD" : 16.2,
        "tRRD" : 10, "tWR" : 15, "tWTR" : 2, "tCKE" : 2,
        "tXP" : 2.0 + 0.9, "tXSR" : 200,
        "arcv" : (7.8 / 0.005) - 50, "are" : 1,
        "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        {
        "tCK" : 6.06,
        "tRFC" : 140, "tRC" : 60, "tRAS" : 42, "tRP" : 18, "tRCD" : 22.5,
        "tRRD" : 12, "tWR" : 15, "tWTR" : 2, "tCKE" : 2,
        "tXP" : 1.0 + 1.1, "tXSR" : 200,
        "arcv" : (7.8 / 0.00606) - 50, "are" : 1,
        "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        {
        "tCK" : 7.5,
        "tRFC" : 140, "tRC" : 75, "tRAS" : 45, "tRP" : 22.5, "tRCD" : 30,
        "tRRD" : 15, "tWR" : 15, "tWTR" : 1, "tCKE" : 2,
        "tXP" : 1.0 + 1.3, "tXSR" : 200,
        "arcv" : (7.8 / 0.0075) - 50, "are" : 1,
        "wbst" : 0, "casl" : 3, "bl" : 2,
        },
    ]

""" M65Kx001AM : SDRC parameters for a given SDRC clock rate

Device summary:
    M65G001AM -- 1Gb (4 banks x 8Mbits x 16)
    M65D001AM -- 1Gb (4 banks x 8Mbits x 32)

Datasheet : Are available from your local Numonyx distributor
 
"""
m65kx001am = [
        {
         "tCK" : 5,
         "tRFC" : 140, "tRC" : 55, "tRAS" : 40, "tRP" : 15, "tRCD" : 15,
         "tRRD" : 10, "tWR" : 15, "tWTR" : 2, "tCKE" : 2,
         "tXP" : 2.0 + 0.9, "tXSR" : 200,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        {
         "tCK" : 6.06,
         "tRFC" : 140, "tRC" : 60, "tRAS" : 42, "tRP" : 18, "tRCD" : 22.5,
         "tRRD" : 12, "tWR" : 15, "tWTR" : 2, "tCKE" : 2,
         "tXP" : 1.0 + 1.1, "tXSR" : 200,
         "arcv" : (7.8 / 0.00606) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        {
         "tCK" : 7.5,
         "tRFC" : 140, "tRC" : 75, "tRAS" : 45, "tRP" : 22.5, "tRCD" : 30,
         "tRRD" : 15, "tWR" : 15, "tWTR" : 1, "tCKE" : 2,
         "tXP" : 1.0 + 1.3, "tXSR" : 200,
         "arcv" : (7.8 / 0.00606) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
    ]

