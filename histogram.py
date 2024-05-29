import os

# FILE OPENING
def fileOpen(name):
    input_file = name + ".txt"

    try:
        data_input = open(input_file, 'rt') #read in data in text form
    except FileNotFoundError:
        print("Error, Input")
        exit(1) 

    try:
        data_output = open("py_histogram.txt", 'w') #write out to here
    except FileNotFoundError:
        print("Error, Output")
        exit(1) 
    
    return (data_input, data_output)

# FILE CLOSING
def fileClose(data_input, data_output):
    data_input.close()
    data_output.close()

intervals = []
data_holder = []
    
def read(data_input):

    line_one = data_input.readline().strip() # reads in the number of intervals
    num_interval = int(line_one)  
    line_two = data_input.readline().strip() # reads in the amount of data
    amount_data = int(line_two) 
    
    for _ in range(num_interval):  
        next_line = data_input.readline().strip().split() #read in the pair
        start, end = map(int, next_line)
        intervals.append((start, end))



    data_line = data_input.readline().strip()  # reads the raw data line
    data_values = data_line.split()  # split the data line into individual values

    for value in data_values:
        data_holder.append((int)(value))

    data_holder.sort()  # sort the data

def build(data_output):
    interval_freqs = []

    for start, end in intervals:  # goes through the intervals
        frequency = sum(start <= value <= end for value in data_holder)  # how many data values are in current interval
        interval_freqs.append(frequency)  # enters frequency for the interval

    # MAKING HISTOGRAM
    data_output.write("DATA HISTOGRAM \n")
    for (start, end), freq in zip(intervals, interval_freqs):  # goes through the intervals
        data_output.write(f"{start}-{end} | {' x ' * freq}\n")
    
    data_output.write("---------------------------------------\n")


def main():
    data_input, data_output = fileOpen("data2")
    read(data_input)
    build(data_output)
    fileClose(data_input, data_output)

if __name__ == "__main__":
    main()
