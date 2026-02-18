import os

import aind_behavior_services.rig as rig

from aind_behavior_implementation_example.rig import (
    AindBehaviorImplementationExampleRig,
)

rig = AindBehaviorImplementationExampleRig(
    rig_name="test_rig",
    harp_behavior=rig.harp.HarpBehavior(port_name="COM13"),
    visual_display=rig.visual_stimulation.Screen()
)

def main(path_seed: str = "./local/{schema}.json"):
    os.makedirs(os.path.dirname(path_seed), exist_ok=True)
    models = [rig]

    for model in models:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
