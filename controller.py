#controls the robot and sends JSON files back 
import arduino
import STT
import ai
from uagents import Agent , Context
class Controller: 
    def __init__(self, talker:arduino.ArduinoCommunicator, mode:str= 'A'):
        self.curVal = 'F'
        self.ard = talker
        self.mode = mode

    dawson = Agent(name = "Cody Dawson")

    @dawson.on_interval(period = 1.0)
    async def update(self):
        recieve = arduino.ArduinoCommunicator.recieve_JSON(self.ard)
        if(self.mode == 'A'):
            self.curVal = self.calc(inp= recieve)
        if(self.mode == 'M'):
            if(self.curVal != 'E'):
                self.curVal = self.pullSpeech()
            else:
                self.changeMode('A')
        arduino.ArduinoCommunicator.send_json(self.curVal)

    def update_inp(self, new:str):
        if(new != self.curVal):
            self.curVal = new


    def changeMode(self, newmode:str):
        self.mode = newmode

    
    def calc(self,inp):
        sensorR = int(inp['first'])
        sensorL = int(inp['second'])
        sensorF = int(inp['front'])
        if (sensorR < 15):
            self.update_inp('R')
        elif(sensorL < 15):
            self.update_inp('L')
        elif (sensorF < 15):
            if(sensorR > sensorL):
                self.update_inp('R')
            else:
                self.update_inp('L')
    

    def pullSpeech(self):
        response = ai.ask_claude_to_decide(STT.mic())
        return response
        



    
