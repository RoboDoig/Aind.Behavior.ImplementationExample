import logging
from typing import Literal, List

import aind_behavior_services.task_logic.distributions as distributions
from aind_behavior_services.task_logic import AindBehaviorTaskLogicModel, TaskParameters
from pydantic import Field, BaseModel

from aind_behavior_implementation_example import (
    __semver__,
)

logger = logging.getLogger(__name__)

# ==================== MAIN TASK LOGIC CLASSES ====================
class Trial(BaseModel):
    temporal_frequency: float = Field(ge=0)
    target_interval: float = Field(ge=0)

class AindBehaviorImplementationExampleTaskParameters(TaskParameters):
    """
    Complete parameter specification for the implementation-example task.
    """
    trials: List[Trial]
    max_trial_time: float
    initial_delay_time: float

class AindBehaviorImplementationExampleTaskLogic(AindBehaviorTaskLogicModel):
    """
    Main task logic model for the implementation-example task.
    """

    version: Literal[__semver__] = __semver__
    name: Literal["AindBehaviorImplementationExample"] = Field(default="AindBehaviorImplementationExample", description="Name of the task logic", frozen=True)
    task_parameters: AindBehaviorImplementationExampleTaskParameters = Field(description="Parameters of the task logic")
