from http import client
import threading
from threading import *
import socket
import math
from time import sleep
import numpy as np

import random
import time
############################################### VARIABLES #################################
D = []  #list of reward values
queue_length = 0
processing_power = 1000
location_to_start = {
    'L' : 0,
    'M' : 1,
    'H' : 2
}

actions = [1,2,3,12,13,23,123]
processing_powers=[1000,1200,900]
servers = [8020,8001,8002]
latency = 1
port = 8002
Q=np.array(np.zeros([3,7]))
L_offload = 0
########################################################################################

def ser():
    global D
    global queue_length
    global processing_power
    global location_to_start
    global processing_powers
    global actions
    global Q
    global latency
    global port
    global L_offload
    srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Server started..")

    srvsocket.bind(('localhost', port))

    print("Binded..")

    srvsocket.listen(40)

    print("Started Listening..")

    def NewClientSocketHandler(cli, ip):
        global D
        global queue_length
        global processing_power
        global location_to_start
        global processing_powers
        global actions
        global latency
        global Q
        global port
        global L_offload
        print("The new has socket id: ",cli)
        print("The message got for cliet socket: ",cli)
        a = cli.recv(256)
        strings = str(a, 'utf8')
        
        ########################################## Q Learning ######################
        def rewards(D):
            print("Reward : {}".format(min(D)))
            return min(D)

        def Qlearning(pkt):
            global processing_power
            global location_to_start
            global processing_powers
            global queue_length
            global actions
            global Q
            global latency
            global D
            global L_offload
            
            def pktrelease():
                global processing_power
                mu = processing_power
                w = 0.5
                Lq = (w*mu)**2/(1+w*mu)
                return Lq
            latency=1
            inst_lam=pkt
            Lq = pktrelease() #expected Lq
            L_offload = int(inst_lam - Lq)
            print("L offload = {}".format(L_offload))
            state=0
            mu = processing_power
            m=queue_length/mu #m = cur_Lq/mu
            if m<0.4:
                state=0
            elif m<0.6:
                state=1
            else:
                state=2   


            # if queue_length>0 and queue_length < processing_power:
            #     queue_length = 0
            # elif queue_length>processing_power:
            #     queue_length = queue_length-processing_power

            def QlearningProcess():
                global location_to_start
                global processing_powers
                global queue_length
                global actions
                global D
                alpha = 0.9
                global Q
                
                global L_offload
                # for i in range(1000):
                print("L offload = {}".format(L_offload))
                playable_actions = []
                for j in range(7):
                        playable_actions.append(j)
                next_action = np.random.choice(playable_actions)
                print(next_action)
                action_len = len(str(actions[next_action]))
                if action_len==1:
                    print("L offload = {}".format(L_offload))
                    print(1111111111111111111111)
                    # L_offload = str(L_offload)
                    # L_offload = L_offload[1:]
                    L_offload = int(L_offload)
                    if actions[next_action] == 1:
                        queue_length = queue_length+L_offload
                    elif actions[next_action] == 2:
                        L_offload = 's'+str(L_offload)+str(port)    
                        # cli1(servers[next_action],L_offload)
                        tt3 = Thread(target=cli1(servers[next_action],str(L_offload)))
                        tt3.start()
                    elif actions[next_action] == 3:
                        L_offload = 's'+str(L_offload)+str(port)    
                        # cli1(servers[next_action],L_offload)
                        tt4 = Thread(target=cli1(servers[next_action],str(L_offload)))
                        tt4.start()
                elif action_len==2:
                    loc = str(actions[next_action])
                    print("L offload = {}".format(L_offload))
                    print(222222222222222222222222222222222)
                    loc1 = int(loc[0])
                    loc2 = int(loc[1])
                    # L_offload = str(L_offload)
                    # L_offload = L_offload[2:]
                    L_offload = int(L_offload)
                    L_offload1 = int(L_offload/2)
                    L_offload2 = L_offload - L_offload1

                    if loc1 == 1:
                        queue_length = queue_length+L_offload1
                    elif loc1 == 2:
                        L_offload = 's'+str(L_offload1)+str(port)    
                        # cli1(servers[loc1-1],L_offload)
                        tt5 = Thread(target=cli1(servers[loc1-1],str(L_offload)))
                        tt5.start()
                    elif loc1 == 3:
                        L_offload = 's'+str(L_offload1)+str(port)    
                        # cli1(servers[loc1-1],L_offload)    
                        tt6 = Thread(target=cli1(servers[loc1-1],str(L_offload)))
                        tt6.start()

                    if loc2 == 3:
                        queue_length = queue_length+L_offload2
                    elif loc2 == 2:
                        L_offload = 's'+str(L_offload2)+str(port)    
                        # cli1(servers[loc2-1],L_offload)
                        tt7 = Thread(target=cli1(servers[loc2-1],str(L_offload)))
                        tt7.start()
                    elif loc2 == 1:
                        L_offload = 's'+str(L_offload2)+str(port)    
                        # cli1(servers[loc2-1],L_offload) 
                        tt8 = Thread(target=cli1(servers[loc2-1],str(L_offload)))
                        tt8.start()    

                elif action_len==3:
                    loc = str(actions[next_action])
                    loc1 = int(loc[0])
                    loc2 = int(loc[1])
                    loc3 = int(loc[2])
                    print("L offload = {}".format(L_offload))
                    print(333333333333333333333333)
                    # L_offload = str(L_offload)
                    # L_offload = L_offload[1:]
                    L_offload = int(L_offload)
                    L_offload1 = int(L_offload/3)
                    L_offload2 = int(L_offload/3)
                    L_offload3 = L_offload - L_offload1-L_offload2

                    if loc1 == 3:
                        queue_length = queue_length+L_offload1
                    elif loc1 == 2:
                        L_offload = 's'+str(L_offload1)+str(port)    
                        # cli1(servers[loc1-1],L_offload1)
                        tt9 = Thread(target=cli1(servers[loc1-1],str(L_offload1)))
                        tt9.start()  
                    elif loc1 == 1:
                        L_offload = 's'+str(L_offload1)+str(port)    
                        # cli1(servers[loc1-1],L_offload1)    
                        tt10 = Thread(target=cli1(servers[loc1-1],str(L_offload1)))
                        tt10.start()  

                    if loc2 == 3:
                        queue_length = queue_length+L_offload2
                    elif loc2 == 2:
                        L_offload = 's'+str(L_offload2)+str(port)    
                        # cli1(servers[loc2-1],L_offload2)
                        tt11 = Thread(target=cli1(servers[loc2-1],str(L_offload2)))
                        tt11.start()  
                    elif loc2 == 1:
                        L_offload = 's'+str(L_offload2)+str(port)    
                        # cli1(servers[loc2-1],L_offload2) 
                        tt12 = Thread(target=cli1(servers[loc2-1],str(L_offload2)))
                        tt12.start()  

                    if loc3 == 3:
                        queue_length = queue_length+L_offload3
                    elif loc3 == 2:
                        L_offload = 's'+str(L_offload3)+str(port)    
                        # cli1(servers[loc3-1],L_offload3)
                        tt13 = Thread(target=cli1(servers[loc3-1],str(L_offload3)))
                        tt13.start()  
                    elif loc3 == 1:
                        L_offload = 's'+str(L_offload3)+str(port)    
                        # cli1(servers[loc3-1],L_offload3)   
                        tt14 = Thread(target=cli1(servers[loc3-1],str(L_offload3)))
                        tt14.start()      
                # print("dfjgvfhbgjnbhdgvsjfgvfbjkn")
                
                # global D
                time.sleep(3)
                reward = rewards(D)
                Q[state][next_action]=alpha*(reward)+(1-alpha)*Q[state][next_action]
                D = []
                
                # if len(D) == action_len:
                #     Qq()
                print(Q)
                next_state = np.argmax(Q[state,])
                print("Action: "+ str(actions[next_state]))
                print("Number of pkts to be offloaded: " + str(Lq))
            QlearningProcess()    
        #get the num
        print(strings)
        if strings[0]=="s":
            po = strings[1:-4]
            por = int(strings[-4:])
            queue_length=queue_length+int(po)
            dd = latency-(queue_length)/processing_power
            dd = 'd'+str(dd)
            # cli1(por,dd)
            tt18 = Thread(target=cli1(por,dd))
            tt18.start()  
            
        elif strings[0]=="c":
            Qlearning(int(strings[1:]))
            
        elif strings[0]=="d":
            D.append(math.tanh(float(strings[1:])))
            
            
        
        

    while True:
        print("Waiting for the incoming connections..")
        cli, ip = srvsocket.accept()
        cli.send(bytes("CONNECT_SUCCESSFUL", encoding='utf8'))

        threading._start_new_thread( NewClientSocketHandler, (cli, ip))


def cli(port):
    clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clisocket.connect(('localhost', port))
    print("The client has been connected..")
    print("The message from the server: ", clisocket.recv(256).decode())

    print("Please keep proving the messages to send to server..")

    msg = input("Please write the message (String in quotes): ")
    # var_incidate_d = 0
    # msg = 60
    clisocket.send(bytes(msg, encoding='utf8'))


def cli1(port,msg):
    global queue_length
    clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clisocket.connect(('localhost', port))
    print("The client has been connected..")
    print("The message from the server: ", clisocket.recv(256).decode())

    print("Please keep proving the messages to send to server..")

    # var_incidate_d = 0
    # msg = 60
    print(queue_length)
    clisocket.send(bytes(msg, encoding='utf8'))


def thr1():
    tt0 = Thread(target=ser)
    tt0.start()

# def thr2(port):
#     tt3 = Thread(target=cli1(port,msg))
#     tt3.start()

def thh():
    global queue_length
    global processing_power
    while True:
        time.sleep(5) 
        if queue_length>0 and queue_length < processing_power:
            queue_length = 0
        elif queue_length>processing_power:
            queue_length = queue_length-processing_power
            
t20 = Thread(target=thh)
t20.start()      

t1 = Thread(target=thr1)
t1.start()

# strt = input("Type 'start' to establish the connections: ")

# if strt == "start":
#     while True:
#         n = int(input("Enter the server to send the mssg{2,3,4}: "))
#         if n==2:
#             t2 = Thread(target=thr2(8001))
#             t2.start()
#         elif(n==3):
#             t3 = Thread(target=thr2(8002))
#             t3.start()
#         else:
#             t4 = Thread(target=thr2(8003))
#             t4.start()