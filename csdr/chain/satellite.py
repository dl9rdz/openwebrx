from csdr.chain.demodulator import ServiceDemodulator
from csdr.module.satellite import SatDumpModule

from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class NoaaAptDemodulator(ServiceDemodulator):
    def __init__(self, satellite: int = 19, service: bool = False):
        d = datetime.utcnow()
        self.outFolder  = "/tmp/satdump/NOAA{0}-{1}".format(satellite, d.strftime('%y%m%d-%H%M%S'))
        self.sampleRate = 50000
        workers = [
            SatDumpModule(mode = "noaa_apt",
                sampleRate = self.sampleRate,
                outFolder  = self.outFolder,
                options    = {
                    "satellite_number" : satellite,
                    "start_timestamp"  : int(d.timestamp())
                }
            )
        ]
        # Connect all the workers
        super().__init__(workers)

    def getFixedAudioRate(self) -> int:
        return self.sampleRate

    def supportsSquelch(self) -> bool:
        return False


class MeteorLrptDemodulator(ServiceDemodulator):
    def __init__(self, symbolrate: int = 72, service: bool = False):
        d = datetime.utcnow()
        self.outFolder  = "/tmp/satdump/METEOR-{0}".format(d.strftime('%y%m%d-%H%M%S'))
        self.sampleRate = 150000
        mode = "meteor_m2-x_lrpt_80k" if symbolrate == 80 else "meteor_m2-x_lrpt"
        workers = [
            SatDumpModule(mode = mode,
                sampleRate = self.sampleRate,
                outFolder  = self.outFolder,
                options    = { "start_timestamp" : int(d.timestamp()) }
            )
        ]
        # Connect all the workers
        super().__init__(workers)

    def getFixedAudioRate(self) -> int:
        return self.sampleRate

    def supportsSquelch(self) -> bool:
        return False


class ElektroLritDemodulator(ServiceDemodulator):
    def __init__(self, symbolrate: int = 72, service: bool = False):
        d = datetime.utcnow()
        self.outFolder  = "/tmp/satdump/ELEKTRO-{0}".format(d.strftime('%y%m%d-%H%M%S'))
        self.sampleRate = 400000
        mode = "elektro_lrit"
        workers = [
            SatDumpModule(mode = mode,
                sampleRate = self.sampleRate,
                frequency = 1691000000,
                outFolder  = self.outFolder,
                options    = { "start_timestamp" : int(d.timestamp()) }
            )
        ]
        # Connect all the workers
        super().__init__(workers)

    def getFixedAudioRate(self) -> int:
        return self.sampleRate

    def supportsSquelch(self) -> bool:
        return False
