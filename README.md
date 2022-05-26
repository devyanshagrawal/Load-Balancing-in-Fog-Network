# Load-Balancing-in-Fog-Network
# Problem Statement
In a fog network as shown in Figure 1.1, each fog node is connected to various IoT devices which are transmitting data continuously. Our task is to design a dynamic load balancing algorithm that will calculate the overload probability of a fog node and make optimal node selection decisions using Q-learning. The requests are then offloaded to the selected nodes.

![Screenshot 2022-05-26 at 9 07 44 AM](https://user-images.githubusercontent.com/91361896/170411170-7e200f7d-7558-4e2c-aa41-25560afd65d2.png)

# Objectives
• To minimize overloading of fog nodes.
• To make effective dynamic offloading decisions.
• To determine the number of requests to be offloaded.
• To minimize request processing time and hence its latency.

# Scope of the project
Fog nodes are considered to have limited computing resources, while the cloud is considered to have unlimited resources.A service request can be processed by offloading packets to neigh- boring fog nodes or the cloud if the node is overloaded, thus distributing the load across the network.The arrival rate of requests to the fog nodes follows Poisson distribution.

# SYSTEM DESIGN
The proposed load balancing algorithm uses Q learning which consists the following tuples
• F:setoffognodes
• M : set of IoT devices
• dm : maximum allowed delay for mth IoT device ∀m ∈ M
• tm : actual processing time for mth IoT device ∀m ∈ M
• S : set of states,where each state represents the load on fog node f ∈ F
– s1: 0–0.6(lowloadstate)
– s2: 0.6–0.8(mediumloadstate) – s3: >0.8(highloadstate)
• A:setofactionsdefinedas A={(P(B)−φ) ∪ac },whereB={bi :i=1to|F|} and ac is action representing offloading to cloud
• R(s,a): Rewardfunctioniscalculatedas,R(s,a)=tanh(D),whereD=dm-tm

# Architecture Design
The system is designed in accordance with Figure 3.1. As we can see Client-server archi- tecture is used. Here, the servers represent the fog nodes, and the sensors represent the IoT devices. All fog nodes are connected to each other and each fog node has several IoT devices connected to it. Each fog node is also connected to the cloud.

![Screenshot 2022-05-26 at 9 15 03 AM](https://user-images.githubusercontent.com/91361896/170411842-b1b603b7-fa5f-4b68-a0e2-3a58631e5aa2.png)

# Result
The packets arriving from IoT devices to the fog nodes follow Poisson distribution, since we cannot predict the exact number of packets arriving.The graph in Figure 5.1 shows the vari- ation of number of packets with probability mass function.

![Screenshot 2022-05-26 at 9 18 38 AM](https://user-images.githubusercontent.com/91361896/170412134-3fa7111b-443d-46ac-b8a3-0e81a2e71b82.png)


The Table 5.2 contains the values of the maximum expected future rewards for each state.Based on this table, we will choose the best course of action by considering the maximum Q-value for each state.At every fog node, 2n actions are available to choose from.The plot of Q-values for corresponding actions taken is shown in Figure 5.3

![Screenshot 2022-05-26 at 9 19 08 AM](https://user-images.githubusercontent.com/91361896/170412176-a47f5492-87c6-427d-b12d-229f863d44f8.png)

The algorithm was tested for 1500 iterations.Figure 5.4, 5.5, 5.6 represents the graph plotted for the reward values against number of iterations for states S1,S2,S3 respectively.

![Screenshot 2022-05-26 at 9 19 51 AM](https://user-images.githubusercontent.com/91361896/170412263-9f8fc627-409b-40ab-aeb9-dc6f8190902e.png)


The graph shown in Figure 5.7 represents the time taken to process the packets at each iteration. It is observed that the minimum time required by the system for the packets to be processed is 1.95 seconds at the 200th iteration and the maximum time is 2.1 seconds at the 700 and 900th iterations.

![Screenshot 2022-05-26 at 9 20 01 AM](https://user-images.githubusercontent.com/91361896/170412276-a307b50f-b061-4572-bff9-ed21c7a1c5d0.png)

The graphs shown in Figures 5.8, 5.9 and 5.10, represent the exploration and exploitation phase for choosing the appropriate actions in state S1, S2, S3 respectively.In Figure 5.8, the algorithm is exploring the system till 800th iteration and action {1,2} is choosing during ex- ploitation.Similarly in Figure 5.9 and Figure5.10, action {1,3} and action {1,2} are chosen during exploitation phase.

![Screenshot 2022-05-26 at 9 20 40 AM](https://user-images.githubusercontent.com/91361896/170412326-86e13123-193e-4ff7-9492-3a15f046739f.png)

![Screenshot 2022-05-26 at 9 21 13 AM](https://user-images.githubusercontent.com/91361896/170412518-b183e061-c9f4-43cc-9295-5c28d7da1b7f.png)

The graph shown in Figure 5.7 represents the time taken to process the packets at each iteration. It is observed that the minimum time required by the system for the packets to be processed is 1.95 seconds at the 200th iteration and the maximum time is 2.1 seconds at the 700 and 900th iterations.

![Screenshot 2022-05-26 at 9 21 23 AM](https://user-images.githubusercontent.com/91361896/170412523-1d97cbce-f96d-49d2-bfd6-87d058e5a9d7.png)

![Screenshot 2022-05-26 at 9 21 35 AM](https://user-images.githubusercontent.com/91361896/170412532-0575b5f0-b94c-4802-89b7-2454e1b0538f.png)

![Screenshot 2022-05-26 at 9 21 41 AM](https://user-images.githubusercontent.com/91361896/170412540-f603eba2-ee99-48a8-a204-9f3a717f90fa.png)

![Screenshot 2022-05-26 at 9 21 48 AM](https://user-images.githubusercontent.com/91361896/170412548-6abb7a50-e8d5-460a-b885-5037df80cd03.png)

# Conclusion
Bringing the edge devices closer to the computing devices and to reduce the request pro- cessing time is the need of the hour, usage of fog networks is a viable solution. As the amount of data is rapidly increasing along with increase in the number of requests from the edge devices, the fog nodes might get overloaded ,to redistribute the load we tried to implement an effective load balancing algorithm which uses Q learning to select the optimal node to offload to.The fog network is implemented using a client-server architecture. The requests arriving at the fog node follow Poisson distribution and the processing rate of each fog node follows an exponential distribution.
The future scope of this project will involve improving the methodology so that the Q- learning algorithm reduces the amount of time needed to select the best node and offloads the number of packets depending on the current overload probability of the fog node.


Tags: Reinforcement Learning, Networking, Parallel Computing, OS
