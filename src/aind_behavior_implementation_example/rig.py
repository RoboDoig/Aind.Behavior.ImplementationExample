# Import core types
from typing import Literal

import aind_behavior_services.rig as rig

from aind_behavior_implementation_example import __semver__


class AindBehaviorImplementationExampleRig(rig.AindBehaviorRigModel):
    version: Literal[__semver__] = __semver__
    harp_behavior: rig.harp.HarpBehavior
    screen: rig.visual_stimulation.Screen