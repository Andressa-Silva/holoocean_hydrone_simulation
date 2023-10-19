import holoocean
import numpy as np

class conf():

    def __init__(self) -> None:
        self.cfg = None

    def configure(self):
        
        self.cfg = {

            "name": "test_rgb_camera",
            "world": "SimpleUnderwater",
            "package_name": "Ocean",
            "main_agent": "auv0",
            "ticks_per_sec": 60,
            "agents": [
                {
                    "agent_name": "auv0",
                    "agent_type": "UavAgent",
                    "sensors": [
                        {
                            "sensor_type": "IMUSensor"
                        }
                    ],
                    "control_scheme": 0,
                    "location": [0, 0, -5]
                },
                {
                    "agent_name": "auv1",
                    "agent_type": "HoveringAUV",
                    "sensors": [
                        {
                            "sensor_type": "DVLSensor"
                        }
                    ],
                    "control_scheme": 0,
                    "location": [0, 2, -5]
                }
            ]
        }

        return self.cfg






    '''cfg = {
        "name": "UAV",
        "world": "SimpleUnderwater",
        "package_name": "Ocean",
        "main_agent": "auv0",
        "ticks_per_sec": 200,
        "agents":[
            {
                "agent_name": "auv0",
                "agent_type": "UavAgent",
                "sensors": [
                    {
                        "sensor_type": "AcousticBeaconSensor",
                        "socket": "AUV_BeaconSocket",
                        "location": [0,0,0],
                         "configuration": {
                            "id": 0
                        }
                    }
                ],
                "control_scheme": 0,
                "location": [0.0, 0.0, 15.0],
                "rotation": [0.0, 0.0, 0.0]
            },
            {
                "agent_name": "auv1",
                "agent_type": "HoveringAUV",
                "sensors": [
                    {
                        "sensor_type": "AcousticBeaconSensor",
                        "socket": "ROV_BeaconSocket",
                        "location": [0,0,0],
                        "configuration": {
                            "id": 1
                        }
                            
                    }
                ],
                "control_scheme": 0,
                "location": [0.0, 0.0, -5.0],
                "rotation": [0.0, 0.0, 0.0]
            }
        ],

        "window_width":  1280,
        "window_height": 720
    }'''
