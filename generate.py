import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    length = 1
    width = 1
    height = 1
    x = -3
    y = 3
    z = 0.5
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

    pyrosim.End()

def Generate_Body():
    # Create Robot
    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1
    x = 0
    y = 0
    z = 0.5
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z + 1], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                       type="revolute", position=".5 0 1")
    pyrosim.Send_Cube(name="BackLeg", pos=[x + .5, y, z - 1], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                       type="revolute", position="-.5 0 1")
    pyrosim.Send_Cube(name="FrontLeg", pos=[x + -.5, y, z - 1], size=[length, width, height])

    pyrosim.End()


def Generate_Brain():
    # Create World
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    #pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-1.0)
    #pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-1.0)
    #pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=-1.0)
    #pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=-1.0)
    # loop over the names
    for i in range(5):
        # loop over the motors
        for j in range(3,5):
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=random.uniform(-1.0, 1.0))


    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()
