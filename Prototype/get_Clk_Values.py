#modules
import sys
import os


class Process:
    #Private variables
    __message = None
    __time = None

    # Setup constructors
    def __init__(self, message, time_Stamp):
        self.__message = message
        self.__time_Stamp = time_Stamp

    # Set functions
    def set_Message(self, message):
        self.__message = message

    def set_Time(self,time_Stamp):
        self.__time_Stamp = time_Stamp

    # Get functions
    def get_Message(self):
        return str(self.__message)

    def get_Time(self):
        return int(self.__time_Stamp)

# Sender is a helper function will get payload and send it to
# designated target
def sender(Process P, target):




# reciever is a helper function that will help the process the
# payload for some process
def recieve(Process P):
    (message,time_Stamp) = recieve()
    time = max(time_Stamp, time)+1




# This function will help us increment the clock counter in a
# a process locally before each event and send its payload to reciever.
def loader_One(Process P):
    time = time + 1
    P.time_Stamp = 1
    sender(P, target)


def main():
    # Create 3 processes
    P1 = Process(" ", 0)
    P2 = Process(" ", 0)
    P3 = Process(" ", 0)

    #Create events here


if __name__ == '__main__':
    main()
