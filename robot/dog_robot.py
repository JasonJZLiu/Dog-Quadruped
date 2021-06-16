"""
@author     Jingzhou Liu
@email      jingzhou.liu@mail.utoronto.ca
@brief      Robot class for a quadruped dog
"""

from adafruit_servokit import ServoKit
import numpy as np
import time

class Dog_Robot:
    """
    @brief This class provides the servo interface for dog
    """

    def __init__(self):
        """
        Initializes the interface and defines internal variables. 
        """
        self.default_state = [0, 0, 0,
                              0, 0, 0,
                              0, 0, 0,
                              0, 0, 0]
        self._state = self.default_state
        self._previous_state = self.default_state

        self._default_servo_positions = [90, 75, 85,
                                         100, 80, 105,
                                         100, 75, 85,
                                         90, 80, 100]

        self._previous_servo_positions = self._default_servo_positions
                                        
        self._joint_to_channel_mapping = [1,  2,  3,
                                          10,  6,  5,
                                          14,  13, 12,
                                          8,  4,  9]

        self._servos = ServoKit(channels = 16)


    """
    Properties
    """                                 
    @property
    def state(self):
        """
        :return: The current state of the robot. 
        """
        return self._state
    
    @property
    def previous_state(self):
        """
        :return: The previous state of the robot. 
        """
        return self._previous_state


    '''
    Internals
    '''
    def _update(self, state_cmd):
        """
        Updates the state internally
        :param state_cmd: Joint position command in the joint space in degrees
        """
        self._previous_state = self._state.copy()
        self._state = state_cmd
    

    def _servo_positions(self, state):
        """
        Mapping from joint space to actuator space
        :return: The current servo positions
        """
        servo_positions = state.copy()
        delta = [state[i]-self.previous_state[i] for i in range(12)]

        for i in [0,3,6,9]:
            servo_positions[i] += self._default_servo_positions[i]
            servo_positions[i+1] += self._default_servo_positions[i+1]
            servo_positions[i+2] += delta[i+1] + self._default_servo_positions[i+2]

        return servo_positions
    

    def _apply_servo_commands(self, current_servo_commands, previous_servo_commands, time_delay):
        servo_position = previous_servo_commands.copy()
        flag = True

        while flag:
            if servo_position == current_servo_commands:
                flag = False
            else:
                for i in range(12):
                    if servo_position[i] < current_servo_commands[i]-3:
                        servo_position[i] += 3
                    elif servo_position[i] > current_servo_commands[i]+3:
                        servo_position[i] -= 3
                    else:
                        servo_position[i] = current_servo_commands[i]
        
                for i in range(12):
                    self._servos.servo[self._joint_to_channel_mapping[i]].angle = servo_position[i]
                time.sleep(time_delay)
            
    

    '''
    Operations
    '''
    def apply_command(self, state_cmd):
        """
        Applies joint space position command to the robot.
        :param state_cmd: Joint position command in the joint space in degrees
        """
        self._update(state_cmd)
        current_servo_positions = self._servo_positions(self._state)

        time_delay = 0.025
        self._apply_servo_commands(current_servo_positions, self._previous_servo_positions, time_delay)

        self._previous_servo_positions = current_servo_positions
    