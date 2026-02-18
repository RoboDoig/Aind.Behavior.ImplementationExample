import datetime
import logging
import os
from typing import Any, Dict, Literal, Optional, Union
from pathlib import Path

import git
from aind_behavior_curriculum import Stage, TrainerState
from aind_behavior_services.rig import Rig
import aind_behavior_services.rig.harp as harp
import aind_behavior_services.rig.visual_stimulation as visual_stimulation
from aind_behavior_services.session import Session
from aind_behavior_services.task import Task
from aind_behavior_implementation_example.task_logic import AindBehaviorImplementationExampleTaskLogic, AindBehaviorImplementationExampleTaskParameters, Trial
from aind_behavior_implementation_example.rig import AindBehaviorImplementationExampleRig
from pydantic import Field

TASK_NAME = "RandomTask"
LIB_CONFIG = rf"local\AindBehavior.db\{TASK_NAME}"

task_logic = AindBehaviorImplementationExampleTaskLogic(
    task_parameters=AindBehaviorImplementationExampleTaskParameters(
        max_trial_time=60,
        initial_delay_time=5,
        trials=[
            Trial(temporal_frequency=1, target_interval=1),
            Trial(temporal_frequency=2, target_interval=2),
            Trial(temporal_frequency=1, target_interval=1),
            Trial(temporal_frequency=2, target_interval=2),
            Trial(temporal_frequency=1, target_interval=1)
        ]
    ),
)

example_trainer_state = TrainerState(
    stage=Stage(name="example_stage", task=task_logic), curriculum=None, is_on_curriculum=False
)

rig = AindBehaviorImplementationExampleRig(
    rig_name="test_rig",
    computer_name="test_computer",
    data_directory=Path("../temp_data"),
    harp_behavior=harp.HarpBehavior(port_name="COM13"),
    screen=visual_stimulation.ScreenAssembly()
)

def create_fake_subjects():
    subjects = ["Plimbo", "Algernon"]
    for subject in subjects:
        os.makedirs(f"{LIB_CONFIG}/Subjects/{subject}", exist_ok=True)
        with open(f"{LIB_CONFIG}/Subjects/{subject}/task.json", "w", encoding="utf-8") as f:
            f.write(task_logic.model_dump_json(indent=2))
        with open(f"{LIB_CONFIG}/Subjects/{subject}/trainer_state.json", "w", encoding="utf-8") as f:
            f.write(example_trainer_state.model_dump_json(indent=2))
            

def create_fake_rig():
    computer_name = os.getenv("COMPUTERNAME")
    os.makedirs(_dir := f"{LIB_CONFIG}/Rig/{computer_name}", exist_ok=True)
    with open(f"{_dir}/rig1.json", "w", encoding="utf-8") as f:
        f.write(rig.model_dump_json(indent=2))
        
        