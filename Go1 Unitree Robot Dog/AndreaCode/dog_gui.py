#!/usr/bin/python
import sys
import time
import math
import tkinter as tk
from tkinter import Button

sys.path.append('../lib/python/amd64')
import robot_interface as sdk

class RobotControlApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Control")
        self.init_robot_interface()
        self.create_buttons()

    def init_robot_interface(self):
        HIGHLEVEL = 0xee
        LOWLEVEL = 0xff
        self.udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.123.161", 8082)
        self.cmd = sdk.HighCmd()
        self.state = sdk.HighState()
        self.udp.InitCmdData(self.cmd)

    def create_buttons(self):
        forward_button = Button(self.master, text="Forward", command=self.move_forward)
        forward_button.pack()

        backward_button = Button(self.master, text="Backward", command=self.move_backward)
        backward_button.pack()

        right_button = Button(self.master, text="Right", command=self.move_right)
        right_button.pack()

        left_button = Button(self.master, text="Left", command=self.move_left)
        left_button.pack()

        turn_left_button = Button(self.master, text="Turn Left", command=self.turn_left)
        turn_left_button.pack()

        turn_right_button = Button(self.master, text="Turn Right", command=self.turn_right)
        turn_right_button.pack()

    def move_forward(self):
        self.set_motion_params(2, 1, [0.4, 0], 0, 0.1)

    def move_backward(self):
        self.set_motion_params(2, 1, [-0.4, 0], 0, 0.1)

    def move_right(self):
        self.set_motion_params(2, 1, [0, 0.4], 0, 0.1)

    def move_left(self):
        self.set_motion_params(2, 1, [0, -0.4], 0, 0.1)

    def turn_left(self):
        self.set_motion_params(2, 1, [0, 0], -0.4, 0.1)

    def turn_right(self):
        self.set_motion_params(2, 1, [0, 0], 0.4, 0.1)

    def set_motion_params(self, mode, gait_type, velocity, yaw_speed, foot_raise_height):
        self.cmd.mode = mode
        self.cmd.gaitType = gait_type
        self.cmd.velocity = velocity
        self.cmd.yawSpeed = yaw_speed
        self.cmd.footRaiseHeight = foot_raise_height
        self.udp.SetSend(self.cmd)
        self.udp.Send()

if __name__ == '__main__':
    root = tk.Tk()
    app = RobotControlApp(root)
    root.mainloop()
