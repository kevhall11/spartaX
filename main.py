from operations import ai

def main():
   # coms = arduino.ArduinoCommunicator(port='COM3',baud_rate= 9600 )
    inp = input("enter speech")
    response = ai.ask_claude_to_decide(inp)
    print(response)


if __name__ == "__main__":
    main()