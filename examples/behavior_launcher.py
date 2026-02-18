import asyncio
import logging
from pathlib import Path

from _mocks import (
    LIB_CONFIG,
    create_fake_subjects,
    create_fake_rig
)

from pydantic_settings import CliApp

from clabe import resource_monitor
from clabe.apps import CurriculumApp, CurriculumSettings, PythonScriptApp
from clabe.launcher import Launcher, LauncherCliArgs, experiment
from clabe.pickers import DefaultBehaviorPicker, DefaultBehaviorPickerSettings
from aind_behavior_services.session import Session
from aind_behavior_implementation_example.rig import AindBehaviorImplementationExampleRig
from aind_behavior_implementation_example.task_logic import AindBehaviorImplementationExampleTaskLogic

logger = logging.getLogger(__name__)

@experiment()
async def demo_experiment(launcher: Launcher) -> None:
    picker = DefaultBehaviorPicker(
        launcher=launcher,
        settings=DefaultBehaviorPickerSettings(config_library_dir=LIB_CONFIG),
        experimenter_validator=lambda _: True,
    )
    
    session = picker.pick_session(Session)
    rig = picker.pick_rig(AindBehaviorImplementationExampleRig)
    launcher.register_session(session, rig.data_directory)
    trainer_state, task = picker.pick_trainer_state(AindBehaviorImplementationExampleTaskLogic)
    _temp_trainer_state_path = launcher.save_temp_model(trainer_state)
    
def main():
    create_fake_subjects()
    create_fake_rig()
    behavior_cli_args = CliApp.run(
        LauncherCliArgs,
        cli_args=[
            "--debug-mode",
            "--allow-dirty",
            "--skip-hardware-validation"
        ],
    )
    launcher = Launcher(settings=behavior_cli_args)
    launcher.run_experiment(demo_experiment)
    
    return None
    
if __name__ == "__main__":
    main()