#modules
import sys
import os

#board layout size
p = 5
m = 24
n = 5

class Package:
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

#empty class that 
#class Process(Package P):
    

# populate function will help modified matrix values from default
# hard code
def populate():
    #create and define process board
    for i in range(p):
        for j in range(2,n):
            for k in range(m):
                P_board = [i][j][k] = 0

    P_board[0][0][0] = a
    P_board[0][0][1] = b
    P_board[0][0][2] = s1
    P_board[0][0][3] = r3
    P_board[0][0][4] = k
    P_board[1][0][0] = a
    P_board[0][0][0] = a
    P_board[0][0][0] = a
    P_board[0][0][0] = a
    P_board[0][0][0] = a
    P_board[0][0][0] = a
    P_board[0][0][0] = a
    P_board[0][0][0] = a
    P_board[0][0][0] = a
    P_board[0][0][0] = a




# Sender is a helper function will get payload and send it to
# designated target
def sender(Process P):
    for i in range(p):
        for j in range(2,n):
            for k in range(m):
                if(P[i][j][k] == )




# reciever is a helper function that will help the process the
# payload for some process
def recieve(Process P):
    (message,time_Stamp) = recieve()
    time = max(time_Stamp, time) + 1


# First to be called, this function will help us increment the clock counter in a
# a process locally before each event and send its payload to reciever.
def loader_One(Process P):
    time = time + 1
    P.time_Stamp = 1
    sender(P)



def main():

    #initialize process board
    populate()

    #Create events here


if __name__ == '__main__':
    main()
