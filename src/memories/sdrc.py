
import math

class SDRC():
    """ This class serves to calculate some registers for the SDRC Subsystem  

    The SDRC subsystem module provides connectivity between the device POP-ed
    SDRAM memory components. The module includes support for low-powe
    double-data-rate SDRAM (LPDDR1).
    
    See AM/DM37x Multimedia Device Silicon Revision 1.x TRM (chapter 10)

    """
    def __init__(self, sdrc):
        """ Hold pre-computed set of SDRC AC timing parameters

        The AC parameters can be independently programmed (standard JEDEC LPDDR1
        terminology is used here) in clock cycles for each of the two memory
        areas through different registers.

        SDRC_ACTIM_CTRL register has following timings:
            tRFC -- AUTO REFRESH to ACTIVE / AUTO REFRESH command period
                    (autoReFresh Cycle time)
            tRC  -- ACTIVE to ACTIVE command period (Row Cycle time)
            tRAS -- ACTIVE to PRECHARGE command period
            tRP  -- PRECHARGE command period (Row Precharge time)
            tRCD -- ACTIVE to READ or WRITE delay (Row-to-Column Delay time)
            tRRD -- ACTIVE bank A to ACTIVE bank B delay
            tWR  -- WRITE Recovery time (also known as tDPL)
            tDAL -- Auto precharge write recovery + precharge time
            tWTR -- Internal Write to Read command delay (also known as tCDLR)
            tCKE -- CKE min pulse width (high and low pulse width)
            tXP  -- Exit Power-Down to next valid command delay
            tXSR -- Self-Refresh exit to next valid command delay
        
        SDRC_RFR_CTRL register has following timings:
            arcv -- Autorefresh counter value to set the refresh period. The
                    autorefresh RW 0x0000 counter is uploaded with the result
                    of: (tREFI / tCK) - 50
            are  -- Autorefresh enable
                    0x0: Autorefresh is disabled
                    0x1: Counter is loaded with ARCV: 1 autorefresh command
                         when autorefresh counter reaches 0.
                    0x2: Counter is loaded with 4 * ARCV: Burst of 4
                         autorefresh commands when autorefresh counter
                         reaches 0.
                    0x3: Counter is loaded with 8 * ARCV: Burst of 8
                         autorefresh commands when autorefresh counter
                         reaches 0.
        SDRC_MR register has following timings:
            wbst -- WBST Write burst support must be zero.
                    0x0: Write burst equals read burst
                    0x1: Write burst disable (single write access only)
            casl -- CAS latency as defined by clock periods
                    0x1: CAS latency = 1
                    0x2: CAS latency = 2
                    0x3: CAS latency = 3
                    0x4: CAS latency = 4
                    0x5: CAS latency = 5
            bl   -- Memory burst length
                    0x1: Burst length = 2 - SDR memory only
                    0x2: Burst length = 4 - DDR memory only
                    0x3: Burst length = 8 - Not supported

        Keyword arguments :
            sdrc -- List of AC timing parameters
                    For example, a typical list of AC timing parameters looks
                    like :
                    sdrc = {
                        "tCK" : 5,
                        "tRFC" : 140, "tRC" : 55, "tRAS" : 40, "tRP" : 15,
                        "tRCD" : 15, "tRRD" : 10, "tWR" : 15, "tWTR" : 2,
                        "tCKE" : 2, "tXP" : 2.0 + 0.9, "tXSR" : 200,
                        "arcv" : (tREFI / tCK) - 50, "are" : 1,
                        "wbst" : 0, "casl" : 3, "bl" : 2,
                        }
        TODO:
           Calculation for SDRC_MCFG register, for example (0x02584019|B_ALL)

        """
        self.timings = sdrc
        # Calculates SDRC AC characteristics measured in clock periods
        self.timings_in_clocks = dict(sdrc) # copy
        # Following timings are in ns, each term must be converted and rounded up.
        timings = ["tRFC", "tRC", "tRAS", "tRP", "tRCD", "tRRD", "tWR", "tXSR"]
        for tim in timings:
            self.timings_in_clocks[tim] = self.round_up(sdrc[tim] / sdrc["tCK"])
        # tDAL is tWR + tRP, each term is rounded up to the next higher integer.
        self.timings_in_clocks["tDAL"] = self.round_up(sdrc["tWR"] / sdrc["tCK"]) + self.round_up(sdrc["tRP"] / sdrc["tCK"])
        # Following timings must be rounded up
        timings = ["tXP", "arcv"]
        for tim in timings:
            self.timings_in_clocks[tim] = self.round_up(sdrc[tim])

    def timings_in_clocks(self):
        """ Returns AC timing parameters in clocks cycles. """
        return self.timings_in_clocks

    def round_up(self, a):
        """ Returns round up value of a. """
        return int(math.ceil(a))

    def trfc(self, a):
        """ AUTO REFRESH to ACTIVE / AUTO REFRESH command period
        
        Register: SDRC_ACTIM_CTRLA_p TRFC[31:27]
        """
        return ((a & 0x1f) << 27)

    def trc(self, a):
        """ ACTIVE to ACTIVE command period (Row Cycle time)
        
        Register: SDRC_ACTIM_CTRLA_p TRC[26:22]
        """
        return ((a & 0x1f) << 22)

    def tras(self, a):
        """ ACTIVE to PRECHARGE command period
        
        Register: SDRC_ACTIM_CTRLA_p TRAS[21:18]
        """
        return ((a & 0xf) << 18)

    def trp(self, a):
        """ PRECHARGE command period (Row Precharge time)
        
        Register: SDRC_ACTIM_CTRLA_p TRP[17:15]
        """
        return ((a & 0x7) << 15)

    def trcd(self, a):
        """ ACTIVE to READ or WRITE delay (Row-to-Column Delay time)
        
        Register: SDRC_ACTIM_CTRLA_p TRCD[14:12]
        """
        return ((a & 0x7) << 12)

    def trrd(self, a):
        """ ACTIVE bank A to ACTIVE bank B delay
        
        Register: SDRC_ACTIM_CTRLA_p TRFC[11:9]
        """
        return ((a & 0x7) << 9)

    def twr(self, a):
        """ WRITE Recovery time (also known as tDPL)
        
        Register: SDRC_ACTIM_CTRLA_p TWR[8:6]
        """
        return ((a & 0x7) << 6)

    def tdal(self, a):
        """ Auto precharge write recovery + precharge time
        
        Register: SDRC_ACTIM_CTRLA_p TDAL[4:0]
        """
        return ((a & 0xf) << 0)

    def twtr(self, a):
        """ Internal Write to Read command delay (also known as tCDLR)
        
        Register: SDRC_ACTIM_CTRLB_p TWTR[17:16]
        """
        return ((a & 0x3) << 16)

    def tcke(self, a):
        """ CKE min pulse width (high and low pulse width)
        
        Register: SDRC_ACTIM_CTRLB_p TCKE[14:12]
        """
        return ((a & 0x7) << 12)

    def txp(self, a):
        """ Exit Power-Down to next valid command delay
        
        Register: SDRC_ACTIM_CTRLB_p TXP[10:8]
        """
        return ((a & 0x7) << 8)

    def txsr(self, a):
        """ Self-Refresh exit to next valid command delay
        
        Register: SDRC_ACTIM_CTRLB_p TXSR[7:0]
        """
        return ((a & 0xff) << 0)

    def rfr_ctrl_arcv(self, a):
        """ Autorefresh counter value to set the refresh period
        
        Register: SDRC_RFR_CTRL_p ARCV[23:8]
        """
        return ((a & 0xffff) << 8)

    def rfr_ctrl_are(self, a):
        """ Autorefresh enable
        
        Register: SDRC_RFR_CTRL_p ARE[1:0]
        """
        return ((a & 0x3) << 0)

    def mr_wbst(self, a):
        """ WBST Write burst support must be zero
        
        Register: SDRC_MR_p WBST[9]
        """
        return ((a & 0x1) << 9)

    def mr_casl(self, a):
        """ CAS latency as defined by clock periods
        
        Register: SDRC_MR_p CASL[6:4]
        """
        return ((a & 0x7) << 4)

    def mr_bl(self, a):
        """  Memory burst length
        
        Register: SDRC_MR_p BL[2:0]
        """
        return ((a & 0x7) << 0)

    def actim_ctrla(self):
        """ Returns the hexadecimal value to program to SDRC_ACTIM_CTRLA """
        retval = (self.trfc(self.timings_in_clocks["tRFC"])
                  | self.trc(self.timings_in_clocks["tRC"])
                  | self.tras(self.timings_in_clocks["tRAS"])
                  | self.trp(self.timings_in_clocks["tRP"])
                  | self.trcd(self.timings_in_clocks["tRCD"])
                  | self.trrd(self.timings_in_clocks["tRRD"])
                  | self.twr(self.timings_in_clocks["tWR"])
                  | self.tdal(self.timings_in_clocks["tDAL"]))
        return hex(retval)

    def actim_ctrlb(self):
        """ Returns the hexadecimal value to program to SDRC_ACTIM_CTRLB """
        retval = (self.twtr(self.timings_in_clocks["tWTR"])
                  | self.tcke(self.timings_in_clocks["tCKE"])
                  | self.txp(self.timings_in_clocks["tXP"])
                  | self.txsr(self.timings_in_clocks["tXSR"]))
        return hex(retval)

    def rfr_ctrl(self):
        """ Returns the hexadecimal value to program to SDRC_RFR_CTRL """
        retval = (self.rfr_ctrl_arcv(self.timings_in_clocks["arcv"])
                  | self.rfr_ctrl_are(self.timings_in_clocks["are"]))
        return hex(retval)

    def mr(self):
        """ Returns the hexadecimal value to program to SDRC_MR """
        retval = (self.mr_wbst(self.timings_in_clocks["wbst"])
                  | self.mr_casl(self.timings_in_clocks["casl"])
                  | self.mr_bl(self.timings_in_clocks["bl"]))
        return hex(retval)

    def __str__(self):
        """ The informal string representation of SDRC object """
        return "tCK : %s ns\nactim ctrla : %s\nactim ctrlb : %s" \
               "\nrfr_ctrl : %s\nmr : %s\ntimings : %s" % (
               self.timings_in_clocks["tCK"],
               self.actim_ctrla(),
               self.actim_ctrlb(),
               self.rfr_ctrl(),
               self.mr(),
               self.timings_in_clocks)
