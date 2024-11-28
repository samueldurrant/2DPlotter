#import controllers.controllers as controller
import concurrent.futures
class Executor:
    def __init__(self, file):
        self.file = file
        with open(self.file, 'r') as f:
            self.execute(f.read())

        # Component Initialisation
        # Solenoid
        solenoid_pin = 1

        # Motors
        step_type = 'Full'

        # Left Motor
        dir_pin_left=13
        step_pin_left=19
        enable_pin_left=12
        mode_pins_left=(16, 17, 20)

        # Motor 2
        dir_pin_right=24
        step_pin_right=18
        enable_pin_right=4
        mode_pins_right=(21, 22, 27)
        #self.solenoid = controller.Solenoid(solenoid_pin)
        #self.left_motor = controller.StepperMotor(enable_pin_left, step_pin_left, dir_pin_left, mode_pins_left, step_type)
        #self.right_motor = controller.StepperMotor(enable_pin_right, step_pin_right, dir_pin_right, mode_pins_right, step_type)

    def execute(self, rle_instructions):
        start_pointer = end_pointer = 0
        while start_pointer < len(rle_instructions):
            if rle_instructions[end_pointer].isdigit():
                end_pointer += 1
            else:
                self.interface(rle_instructions[end_pointer], int(rle_instructions[start_pointer:end_pointer] or 1))
                end_pointer += 1
                start_pointer = end_pointer

    def interface(self, instruction, iterations):
        match instruction:
            case "U":
                self.pen_up(iterations)
            case "D":
                self.pen_down(iterations)
            case "L":
                self.rotate_left(iterations)
            case "R":
                self.rotate_right(iterations)
            case "F":
                self.move_forward(iterations)

    def pen_up(self, iters):
        for i in range(iters):
            print("PU")
            #self.solenoid.disengage()

        # pick pen up solenoid control here
        pass

    def pen_down(self, iters):
        for i in range(iters):
            print("PD")
            #self.solenoid.engage()
        # put down pen solenoid control here
        pass

    def move_forward(self, iters):
        for i in range(iters):
            print("MF")
            with concurrent.futures.ThreadPoolExecutor() as threadexecutor:
                #t1 = threadexecutor.submit(self.left_motor.run, 1, True)
                #t1 = threadexecutor.submit(self.right_motor.run, 1, True)
                pass

        # put go forward motor control here

    def rotate_right(self, iters):
        for i in range(iters):
            print("RR")
            with concurrent.futures.ThreadPoolExecutor() as threadexecutor:
                #t1 = threadexecutor.submit(self.left_motor.run, 1, True)
                #t1 = threadexecutor.submit(self.right_motor.run, 1, False)
                pass
        # put turn right motor control here
        pass

    def rotate_left(self, iters):
        for i in range(iters):
            print("RL")
            with concurrent.futures.ThreadPoolExecutor() as threadexecutor:
                #t1 = threadexecutor.submit(self.left_motor.run, 1, False)
                #t1 = threadexecutor.submit(self.right_motor.run, 1, True)
                pass
        pass

file = "Input/nflcxf.txt"
executor = Executor(file)