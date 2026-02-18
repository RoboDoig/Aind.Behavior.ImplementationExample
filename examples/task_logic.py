import os

import aind_behavior_services.task_logic.distributions as distributions
from aind_behavior_curriculum import Stage, TrainerState

from aind_behavior_implementation_example.task_logic import (
    AindBehaviorImplementationExampleTaskLogic,
    AindBehaviorImplementationExampleTaskParameters,
    Trial
)


task_logic = AindBehaviorImplementationExampleTaskLogic(
    task_parameters=AindBehaviorImplementationExampleTaskParameters(
        trials=[
            Trial(temporal_frequency=1, target_interval=1),
            Trial(temporal_frequency=1, target_interval=1),
            Trial(temporal_frequency=1, target_interval=1),
            Trial(temporal_frequency=2, target_interval=2),
            Trial(temporal_frequency=2, target_interval=2)
        ]
    ),
)


def main(path_seed: str = "./local/example_{schema}.json"):
    example_task_logic = task_logic
    example_trainer_state = TrainerState(
        stage=Stage(name="example_stage", task=example_task_logic), curriculum=None, is_on_curriculum=False
    )
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [example_task_logic, example_trainer_state]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
