import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Here I had opened the file in a read mode
    with open(t, 'r') as file:
        # Created a list containing integer values from each line of the file
        #also here strip is used for removing any whitespace from front or back
        snowfall_data = [int(line.strip()) for line in file]

    ranges = [0] * 6 

# This is a for loop which is used for aggregating snowfall values into range
    for value in snowfall_data:
        if value <= 10:
            ranges[0] += 1
        elif 11 <= value <= 20:
            ranges[1] += 1
        elif 21 <= value <= 30:
            ranges[2] += 1
        elif 31 <= value <= 40:
            ranges[3] += 1
        elif 41 <= value <= 50:
            ranges[4] += 1
        else:
            ranges[5] += 1

    plt.bar(['0-10', '11-20', '21-30', '31-40', '41-50', '51-60'], ranges)

    plt.xlabel('Snowfall Range (cm)')  
    plt.ylabel('Number of Occurrences')  
    plt.title('Snowfall Accumulation Ranges')  

    plt.show()

graphSnowfall('snow_data.txt')
