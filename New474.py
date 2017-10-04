
#modules
import sys
import os

#board dimensions

#number of rows max
n = 5

#number of columns max (max of number of events)
m = 24

#number of processes max
p = 9

#global dictionary keeping track of send commands
sARR = {}
rARR = {}
#global time variable
time = 0

#send Flag
sFlag = 1

class Package:
    #Private variables

    # Setup constructors
    def __init__(self, message = "0", time_Stamp = 0):
        self.message = message
        self.time_Stamp = time_Stamp

    # Set functions
    def set_Message(self, message):
        self.message = message

    def set_Time(self,time_Stamp):
        self.time_Stamp = time_Stamp

    # Get functions
    def get_Message(self):
        return str(self.message)

    def get_Time(self):
        return int(self.time_Stamp)

    # functions that perform local calculations


    def local_Count(self,time):
        global sFlag
        if self.message == "0":
            return
        elif (self.message[0] == "s"):
            self.time_Stamp = time
            self.sendV()

        elif(self.message[0]== "r"):
            self.recV()
        elif(self.message== "NULL"):
            self.time_Stamp = 0
        else:
            self.time_Stamp = time
            # P.time_Stamp = time
            return self.time_Stamp
    #check if corresponding send function is in sARR
    #if so, compare previous object time_Stamp to sARR timestamp and select max
   
    def recV(self):
        global rARR
        global time
        if(self.message == "r1"):
            if('s1' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s1']) 
               time = self.time_Stamp
        elif(self.message == "r2"):
            if('s2' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s2'])
               time = self.time_Stamp
        elif(self.message == "r3"):
            if('s3' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s3']) 
               time = self.time_Stamp
        elif(self.message == "r4"):
            if('s4' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s4'])
               time = self.time_Stamp       
        elif(self.message == "r5"):
            if('s5' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s5'])
               time = self.time_Stamp
        elif(self.message == "r6"):
            if('s6' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s6'])
               time = self.time_Stamp
        elif(self.message == "r7"):
            if('s7' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s7'])
               time = self.time_Stamp
        elif(self.message == "r8"):
            if('s8' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s8'])
               time = self.time_Stamp
        elif(self.message == "r9"):
            if('s9' in sARR):
               self.time_Stamp = max(self.time_Stamp,sARR['s9'])
               time = self.time_Stamp
        else:
            print("recieve function does not exist")
  
    def sendV(self):
        global sARR
        global sFlag
        if (self.message in sARR and self.time_Stamp < sARR[self.message]):        
            return
        else:
            sFlag += 1  
            sARR[self.message] = self.time_Stamp + 1
         

#create the board size
P_board1 = [[[Package() for col in range(m)] for row in range(n)]for proc in range (p)]

#fixed values for P_board1
P_board1[0][0][0].set_Message("a")
P_board1[0][0][1].set_Message("s1")
P_board1[0][0][2].set_Message("r3")
P_board1[0][0][3].set_Message("b")
P_board1[1][0][0].set_Message("c")
P_board1[1][0][1].set_Message("r2")
P_board1[1][0][2].set_Message("s3")
P_board1[2][0][0].set_Message("r1")
P_board1[2][0][1].set_Message("d")
P_board1[2][0][2].set_Message("s2")
P_board1[2][0][3].set_Message("e")



def main():

    global sARR
    global time
    global sFlag


    #get range input from user 
    p = int(input("Enter a number of processes: "))
    n = int(input("Enter a number of rows: "))
    m = int(input("Enter a number of columns: "))

    #get individual message input from user
    for z in range(p):
        for x in range(n):
            for y in range(m):
                P_board1[z][x][y].message = input("Enter an event Value: ")


    #printing messages
    for z in range(p):
        print('\n')
        for x in range(n):
            print('\n')
            for y in range(m):
                if (P_board1[z][x][y].message == "0"):
                    print(P_board1[z][x][y].message, end = " ") 
                else:
                    print(P_board1[z][x][y].message, end = " ")



    #goes through the array of packages and updates by calling local time
    #continues to do so if any send functions are read (sFlag)
    while(sFlag > 0):
        sFlag = 0
        for k in range(p):
           
            for i in range(n): 
                time = 1              
                for j in range(m):
                    e = P_board1[k][i][j]
                    if(P_board1[k][i][j].message == "0"):
                        break
                    else:
                        e.local_Count(time);
                        time += 1
                        temp_val = e.get_Time()
                        P_board1[k][i][j].set_Time(e.get_Time())
       

    #outputting timevalues of messages
    for z in range(p):    
        print('\n')
        for x in range(n):
            print('\n')
            for y in range(m):
                if (P_board1[z][x][y].message == "0"):
                    print(P_board1[z][x][y].message, end = " ") 
                else:
                    print(P_board1[z][x][y].get_Time(), end = " ")

    print(sARR)
    
    
     

if __name__ == '__main__':
    main()
