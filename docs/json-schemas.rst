json-schema
-------------
The following json-schemas are used as the format definition of the input for this task. They are the result of the `Pydantic`` models defined in `src/aind_behavior_implementation_example`, and are also used to generate `src/Extensions/AindBehaviorImplementationExample.cs` via `Bonsai.Sgen`.

`Download Schema <https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.ImplementationExample/main/src/DataSchemas/aind_behavior_implementation_example.json>`_

Task Logic Schema
~~~~~~~~~~~~~~~~~
.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.ImplementationExample/main/src/DataSchemas/aind_behavior_implementation_example.json#/$defs/AindBehaviorImplementationExampleTaskLogic
   :lift_definitions:
   :auto_reference:


Rig Schema
~~~~~~~~~~~~~~
.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.ImplementationExample/main/src/DataSchemas/aind_behavior_implementation_example.json#/$defs/AindBehaviorImplementationExampleRig
   :lift_definitions:
   :auto_reference:
