# CPU-Schedulers

## Overview

CPU-Schedulers is a web-based application designed to simulate and visualize different CPU scheduling algorithms. Developed using Flask, a lightweight WSGI web application framework in Python, this project aims to provide an interactive educational tool for understanding how various CPU scheduling strategies work in operating systems.

## Features

CPU-Schedulers offers simulations of four fundamental CPU scheduling algorithms:

- **First-Come, First-Served (FCFS) Scheduling**: Processes are serviced in the order they arrive in the ready queue without preemption.
- **Shortest-Job-First (SJF) Scheduling**: The process with the shortest execution time in the ready queue is selected next.
- **Priority Scheduling**: Processes are serviced based on priority, with higher priority processes being selected first.
- **Round-Robin (RR) Scheduling**: Each process is assigned a time slice or quantum, after which it is placed back in the ready queue, ensuring all processes share CPU time equitably.

## Usage
Upon accessing the CPU-Schedulers application, you will be presented with a simple user interface where you can choose the scheduling algorithm you want to simulate: FCFS, SJF, Priority, or Round-Robin. Depending on the selected algorithm, you may need to enter additional details for each process, such as burst time or priority.
After selecting an algorithm and inputting the necessary process details, submit the form to view the simulation results. The application visualizes the scheduling order, displaying each process's waiting time and highlighting the operational flow according to the chosen scheduling strategy.
