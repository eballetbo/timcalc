""" micron.py: This provides SDRC parameters for Micron devices

"""

""" MT29CxGxxMAxAPxxx : SDRC parameters for a given SDRC clock rate

Device summary:
    MT29C4G48MAYAPAKQ-5 IT, MT29C4G48MAZAPAKQ-5 IT,
    MT29C4G48MAZAPAKQ-6 IT, MT29C4G96MAZAPCJG-5 IT,
    MT29C4G96MAZAPCJG-6 IT, MT29C8G96MAZAPDJV-5 IT,
    MT29C8G96MAZAPDJV-6 IT

Datasheet : Are available from your local Micron distributor
 
"""
mt29cxgxxmaxapxxx = [
        { # 200 MHz
         "tCK" : 5,
         "tRFC" : 72, "tRC" : 55, "tRAS" : 40, "tRP" : 15, "tRCD" : 15,
         "tRRD" : 10, "tWR" : 15, "tWTR" : 2, "tCKE" : 1,
         "tXP" : 2, "tXSR" : 112.5,
         "arcv" : (7.8 / 0.005) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 185 MHz
         "tCK" : 5.4,
         "tRFC" : 72, "tRC" : 58.2, "tRAS" : 42, "tRP" : 16.2, "tRCD" : 16.2,
         "tRRD" : 10.8, "tWR" : 15, "tWTR" : 2, "tCKE" : 1,
         "tXP" : 2, "tXSR" : 112.5,
         "arcv" : (7.8 / 0.0054) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 166 MHz
         "tCK" : 6.06,
         "tRFC" : 72, "tRC" : 60, "tRAS" : 42, "tRP" : 18, "tRCD" : 18,
         "tRRD" : 12, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 112.5,
         "arcv" : (7.8 / 0.00606) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        },
        { # 133 MHz
         "tCK" : 7.5,
         "tRFC" : 72, "tRC" : 67.5, "tRAS" : 45, "tRP" : 22.5, "tRCD" : 22.5,
         "tRRD" : 15, "tWR" : 15, "tWTR" : 1, "tCKE" : 1,
         "tXP" : 1, "tXSR" : 112.5,
         "arcv" : (7.8 / 0.0075) - 50, "are" : 1,
         "wbst" : 0, "casl" : 3, "bl" : 2,
        }
    ]
