import numpy as np

class key_controlling():
    """Class for manual control of vehicles (ROV and drone)"""

    def parse_keys_rov(keys: list, val: int) -> np.array:
        """Manual control of the ROV by the keyboard.
        
        Args:
            Keys(list): list of pressed keys on the keyboard;
            Val (int): the force strenght apply to the mottors

        Returns:
            np.array: an array of the commands to be sent to the ROV

        Commands of the keyboard:
            'i' --> Up            'k' --> Down
            'j' --> Yaw Left      'l' --> Right
            'w' --> Forward       's' --> Backward 
            'a' --> Strafe Left   'd' --> Right 
                  -
        """
        command = np.zeros(8)

        if 'i' in keys:                 
            command[0:4] += val    
        if 'k' in keys:                 
            command[0:4] -= val
        if 'j' in keys:                 
            command[[4,7]] += val
            command[[5,6]] -= val
        if 'l' in keys:
            command[[4,7]] -= val
            command[[5,6]] += val

        if 'w' in keys:
            command[4:8] += val
        if 's' in keys:
            command[4:8] -= val
        if 'a' in keys:
            command[[4,6]] += val
            command[[5,7]] -= val
        if 'd' in keys:
            command[[4,6]] -= val
            command[[5,7]] += val

        return command
    

    def parse_keys_drone(keys: list, val: int, val2: int, val3: int) -> np.array:
        """Manual control of the drone by the keyboard.
        
        Args:
            keys(list): list of pressed keys on the keyboard;
            val (int): the force strenght apply to the mottors
            val2 (int): the force of the spin
            val3 (int): the force of yaw

        Returns:
            np.array: an array of the commands to be sent to the ROV

        Commands of the keyboard:
            'i' --> Up               'k' --> Down
            'j' --> Yaw Rotate Left  'l' --> Yaw Rotate Right
            'w' --> Pitch Forward    's' --> Roll Right 
            'a' --> Forward          'd' --> Backward
                  -
        """
        command = np.zeros(4)
        #command[0:4] = depth_command  

        if 'i' in keys:                 
            command[3] += val
            command[3] += val    
        if 'k' in keys:                 
            command[3] -= val
            command[3] -= val
        if 'j' in keys:                 
            command[2] += val3
            command[2] += val3
        if 'l' in keys:
            command[2] -= val3
            command[2] -= val3

        if 'w' in keys:
            command[0] += val2
            command[0] += val2
        if 's' in keys:
            command[0] -= val2
            command[0] -= val2
        if 'a' in keys:
            command[1] -= val2
            command[1] -= val2
        if 'd' in keys:
            command[1] += val2
            command[1] += val2

        return command
        

