# Import core types
from typing import Literal

import aind_behavior_services.rig as rig
import aind_behavior_services.rig.harp as harp
import aind_behavior_services.rig.visual_stimulation as visual_stimulation

from aind_behavior_implementation_example import __semver__


class AindBehaviorImplementationExampleRig(rig.Rig):
    version: Literal[__semver__] = __semver__
    harp_behavior: harp.HarpBehavior
    screen: visual_stimulation.ScreenAssembly