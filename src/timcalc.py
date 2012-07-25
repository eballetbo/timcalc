""" timecalc.py : Timings calculator

"""

from memories import hynix, micron, numonyx, sdrc

if __name__ == '__main__':
    memories = {
                 "M65Kx001AM" :  numonyx.m65kx001am,
                 "M65Kx002AM" :  numonyx.m65kx002am,
                 "MT29CxGxxMAxAPxxx" : micron.mt29cxgxxmaxapxxx,
                 "H9DH4GHxxJAPER" : hynix.h9dh4ghxxjaper,
                 "H9DH1GH51JMPER" : hynix.h9dh1gh51jmper
                }
    # Print all timings
    for key in memories.keys():
        print key
        for item in memories[key]:
            print sdrc.SDRC(item)
            print "\n"
