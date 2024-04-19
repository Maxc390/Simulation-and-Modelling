import random
import csv
import math

# Constants
Q_LIMIT = 100
BUSY = 1
IDLE = 0

# Global variables
next_event_type = 0
num_custs_delayed = 0
num_delays_required = 0
num_events = 0
num_in_q = 0
server_status = 0
area_num_in_q = 0.0
area_server_status = 0.0
mean_interarrival = 0.0
mean_service = 0.0
sim_time = 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_last_event = 0.0
time_next_event = [0.0] * 3
total_of_delays = 0.0

def initialize():
    global sim_time, server_status, num_in_q, time_last_event, num_custs_delayed
    global total_of_delays, area_num_in_q, area_server_status, time_next_event

    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0

    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0

    # Initialize event list.Since no customers are present, the departure
    #(service completion) event is eliminated from consideration.
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30
#timing function
def timing():
    """Timing function to determine the next event."""
    global sim_time, next_event_type

    min_time_next_event = float('inf')
    next_event_type = 0

    # Find minimum time and event type efficiently
    for i in range(1, num_events + 1):
        if time_next_event[i ] < min_time_next_event:
            min_time_next_event = time_next_event[i ]
            next_event_type = i

    # Update simulation clock
    sim_time = min_time_next_event

def arrive():
    global sim_time, num_in_q, server_status, num_custs_delayed, total_of_delays

    # Schedule next arrival.
    time_next_event[1] = sim_time + expon(mean_interarrival)

    if server_status == BUSY:
        # Server is busy, so increment the number of customers in the queue.
        num_in_q += 1
        #The queue has overflowed, so stop the simulation.
        if num_in_q > Q_LIMIT:
            print(f"\nOverflow of the array time_arrival at time {sim_time}")
            exit(2)
        #There is still room in the queue, so store the time of arrival of the arriving customer at the (new) end of time_arrival.
        time_arrival[num_in_q] = sim_time
    else:
        # Server is idle, so arriving customer has a delay of zero.
        delay = 0.0
        total_of_delays += delay
        #Increment the number of customers delayed, and make server busy.
        num_custs_delayed += 1
        server_status = BUSY

        # Schedule a departure (service completion).
        time_next_event[2] = sim_time + expon(mean_service)

def depart():
    global sim_time, num_in_q, server_status, num_custs_delayed, total_of_delays
    #Check to see whether the queue is emptyand and eliminate the
    #departure (service completion) event from consideration..
    if num_in_q == 0:
        # The queue is empty, so make the server idle.
        server_status = IDLE
        time_next_event[2] = float('inf')
    else:
        # The queue is notempty, so decrement the number of customers in the queue.
        num_in_q -= 1

        # Compute the delay of the customer who is beginning service and update the total delay accumulator.
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        #Increment the number of customers delayed, and schedule departure.
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)

        # Move each customer in the queue (if any) up one place.
        time_arrival[:num_in_q] = time_arrival[1:num_in_q + 1]

def report():
    global total_of_delays, num_custs_delayed, area_num_in_q, area_server_status, sim_time

    # Compute and write estimates of the measures of performance.
    avg_delay_in_queue = total_of_delays / num_custs_delayed
    avg_num_in_queue = area_num_in_q / sim_time
    server_utilization = area_server_status / sim_time

    with open("mm1.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([f"Average delay in queue {avg_delay_in_queue:.3f} minutes"])
        csv_writer.writerow([f"Average number in queue {avg_num_in_queue:.3f}"])
        csv_writer.writerow([f"Server utilization {server_utilization:.3f}"])
        csv_writer.writerow([f"Time simulation ended {sim_time:.3f} minutes"])

def update_time_avg_stats():
    global sim_time, time_last_event, area_num_in_q, area_server_status

    # Compute time since the last event and update the last-event-time marker.
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    # Update area under the number-in-queue function.
    area_num_in_q += num_in_q * time_since_last_event

    # Update area under the server-busy indicator function.
    area_server_status += server_status * time_since_last_event

def expon(mean):
    # Return an exponential random variate with mean "mean".
    return -mean * math.log(random.random())

def read_input(filename="mm1.in"):
    try:
        with open(filename, "r") as infile:
            values = list(map(float, infile.readline().split()))
            if len(values) != 3:
                raise ValueError("Expected 3 values in the input file, found {}".format(len(values)))
            return values
    except Exception as e:
        print("Error reading input from {}: {}".format(filename, e))
        exit(1)



def main():
    global mean_interarrival, mean_service, num_delays_required, num_events

    # Open input files.
    mean_interarrival, mean_service, num_delays_required = read_input()

    # Specify the number of events for the timing function.
    num_events = 2

    # Write report heading and input parameters.
    with open("mm1.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([f"Single-server queueing system"])
        csv_writer.writerow([f"Mean interarrival time {mean_interarrival:.3f} minutes"])
        csv_writer.writerow([f"Mean service time {mean_service:.3f} minutes"])
        csv_writer.writerow([f"Number of customers {num_delays_required}"])

    # Initialize the simulation.
    initialize()

    # Run the simulation while more delays are still needed.
    while num_custs_delayed < num_delays_required:
        # Determine the next event.
        timing()

        # Update time-average statistical accumulators.
        update_time_avg_stats()

        # Invoke the appropriate event function.
        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()

    # Invoke the report generator and end the simulation.
    report()

if __name__ == "__main__":
    main()

