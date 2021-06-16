"""
@author     Jingzhou Liu
@email      jingzhou.liu@mail.utoronto.ca
@brief      System class for a quadruped dog
"""

import numpy as np
import time
from robot.dog_robot import Dog_Robot

class Dog_System:
    """
    @brief This class provides the interface for the dog quadruped system.
    """

    def __init__(self):
        """
        Initializes the interface and defines internal variables. 
        """

        self._robot = Dog_Robot()
        


    """
    Properties
    """                                 
    @property
    def state(self):
        """
        :return: The current state of the robot. 
        """
        return self._robot.state
    
    @property
    def previous_state(self):
        """
        :return: The previous state of the robot. 
        """
        return self._robot.previous_state


    '''
    Internals
    '''
    def _update(self, state_cmd):
        """
        Updates the state internally
        :param state_cmd: Joint position command in the joint space in degrees
        """
        self._robot._update()
    
    


    '''
    Operations
    '''
    def advance(self, state_cmd):
        """
        Applies joint space position command to the robot.
        :param state_cmd: Joint position command in the joint space in degrees
        """
        self._robot.apply_command(state_cmd)
       
    