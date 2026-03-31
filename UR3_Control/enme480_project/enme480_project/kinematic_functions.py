import numpy as np
import sys
import math

class KinematicFunctions():


    def calculate_dh_transform(self, joint_positions):

        ####################################### Your Code Starts Here #######################################

        # TODO: DH parameters for UR3e. Modify these parameters according to the robot's configuration # a , alpha, d, theta 


        ############################# Your Code Ends Here #######################################
        

        return transform


    def inverse_kinematics(self, xWgrip, yWgrip, zWgrip, yaw_WgripDegree):
        
        return_value = np.array([0, 0, 0, 0, 0, 0])

        ####################################### Your Code Starts Here #######################################

        # TODO: Function that calculates an elbow up inverse kinematics solution for the UR3

        # Step 1: find gripper position relative to the base of UR3

        # Step 2: find x_cen, y_cen, z_cen

        # Step 3: find theta_1

        # Step 4: find theta_6

        # Step 5: find x3_end, y3_end, z3_end

        # Step 6: find theta_2, theta_3, theta_4


        ############################# Your Code Ends Here #######################################

        # print theta values (in degree) calculated from inverse kinematics
        
        # print("Correct Joint Angles: ")
        # print(str(theta_1*180/np.pi) + " " + str(theta_2*180/np.pi) + " " + \
        #         str(theta_3*180/np.pi) + " " + str(theta_4*180/np.pi) + " " + \
        #         str(theta_5*180/np.pi) + " " + str(theta_6*180/np.pi))

        # obtain return_value from forward kinematics function
        return_value = [theta_1, theta_2, theta_3, theta_4, theta_5, theta_6]

        return return_value 