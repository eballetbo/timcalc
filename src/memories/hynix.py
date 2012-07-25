""" hynix.py: This provides SDRC parameters for Hynix devices

"""

""" H9DH4GHxxJAPER : SDRC parameters for a given SDRC clock rate

Device summary:
    H9DH4GH4JJAPER series - NAND 4Gb(x16) / Mobile DDR 4Gb(x32)
    H9DH4GH2GJAPER series - NAND 4Gb(x16) / Mobile DDR 1Gb(x32)

Datasheet : Are available from your local Hynix distributor
 
"""
h9dh4ghxxjaper = [
        { # 200 MHz
         "tCK" : 5,
         "tRFC" : 90, "tRC" : 40 + 15, "tRAS" : 40, "tRP" : 15, "tRCD" : 15,
         "tRRD" : 10, "tWR" : 15, "tWTR" : 2, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 140,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 185 MHz
         "tCK" : 5.4,
         "tRFC" : 90, "tRC" : 42 + 16.2, "tRAS" : 42, "tRP" : 16.2, "tRCD" : 16.2,
         "tRRD" : 10.8, "tWR" : 15, "tWTR" : 2, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 140,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 166 MHz
         "tCK" : 6.06,
         "tRFC" : 90, "tRC" : 42 + 18, "tRAS" : 42, "tRP" : 18, "tRCD" : 18,
         "tRRD" : 12, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 140,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 133 MHz
         "tCK" :  7.5,
         "tRFC" : 90, "tRC" : 45 + 22.5, "tRAS" : 45, "tRP" : 22.5,
         "tRCD" : 22.5, "tRRD" : 15, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 140,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 100 MHz
         "tCK" : 10,
         "tRFC" : 90, "tRC" : 50 + 30, "tRAS" : 50, "tRP" : 30, "tRCD" : 30,
         "tRRD" : 15, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 140,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
    ]

""" H9DH1GH51JMPER : SDRC parameters for a given SDRC clock rate

Device summary:
    H9DH1GH51JMPER series - NAND 1Gb(x16) / Mobile DDR 512Mb(x32)

Datasheet : Are available from your local Hynix distributor
 
"""
h9dh1gh51jmper = [
        { # 200 MHz
         "tCK" : 5,
         "tRFC" : 72, "tRC" : 40 + 15, "tRAS" : 40, "tRP" : 15, "tRCD" : 15,
         "tRRD" : 10, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 120,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 185 MHz
         "tCK" : 5.4,
         "tRFC" : 72, "tRC" : 42 + 16.2, "tRAS" : 42, "tRP" : 16.2, "tRCD" : 16.2,
         "tRRD" : 10.8, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 120,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 166 MHz
         "tCK" : 6.06,
         "tRFC" : 72, "tRC" : 42 + 18, "tRAS" : 42, "tRP" : 18, "tRCD" : 18,
         "tRRD" : 12, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 120,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 133 MHz
         "tCK" :  7.5,
         "tRFC" : 72, "tRC" : 45 + 22.5, "tRAS" : 45, "tRP" : 22.5,
         "tRCD" : 22.5, "tRRD" : 15, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 120,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 100 MHz
         "tCK" : 10,
         "tRFC" : 72, "tRC" : 50 + 30, "tRAS" : 50, "tRP" : 30, "tRCD" : 30,
         "tRRD" : 15, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 120,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
    ]
