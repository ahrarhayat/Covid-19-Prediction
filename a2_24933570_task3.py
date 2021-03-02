# Student Name: Ahrar Hayat
# ID: 24933570
# Start Date: Sunday, 17 May 2020 at 5:52 pm
# Last Modified: Friday, 5 June 2020 at 12:55 am
# Description: This file uses the pyplot library to visualize the results of the task 2
# file. The x-axis shows the number of days passed, and the y-axis shows the number
# of cases
# Test scenario A, an uncontained outbreak:
# Number of days: 30
# Meeting probability: 0.6
# Patient zero health: 25 health points
# For Test scenario A with the patient zero at 25 health points, there is a 60% chance that he will visit
# a friend and infect them, there is a good chance that the friend will visit patient zero and infect him even
# more and they will get infected as a result. With the spread of so many infected people, it will lead to
# an uncontrolled outbreak
# Test scenario B, an unpredictable situation:
# Number of days: 60
# Meeting probability: 0.25
# Patient zero health: 49 health points
# For test scenario B, there is a 25% chance that each friend will visit each other and infect each other
# at times, both friends will visit each other and infect each other and it may lead to an outbreak
# and other times, a friend will only see another friend once and only infect them once and may not visit them at all.
# Since the patient zero has a health of 49, he/she can heal quite fast without spreading resulting in
# the flattening of the curve. For various tests, at times it led to an outbreak and other times
# it was flattened out.
# Test scenario C, flattening the curve:
# Number of days: 90
# Meeting probability: 0.18
# Patient zero health: 40 health points
# For test scenario C, Even though the health point of patient zero is 40, due to social distancing measure
# the patient zero has more chance not to visit any friends and healing himself/herself. In some rare cases
# the virus may spread to a few people before it dies out due to social distancing.
# Visualisation code template for FIT9136 Assignment 2.

from a2_24933570_task2 import *
from matplotlib import pyplot as plt


def visual_curve(days, meeting_probability, patient_zero_health):
    test_result = run_simulation(days, meeting_probability, patient_zero_health)
    x = []
    # make a list of days in the simulation
    for day in range(days):
        x.append(day)
    # the list of number of cases per day is assigned here
    y = test_result
    plt.plot(x, y)
    plt.xlabel('Days')
    plt.ylabel('Number of cases')
    plt.show()
    return test_result


if __name__ == '__main__':
    days = int(input('Enter the number of days in the simulation: '))
    probability = float(input('Enter the meeting probability for the simulation: '))
    patient_zero_health = float(input('Enter the health for patient zero: '))
     #print(visual_curve(90,0.18,40))
    # print(visual_curve(90, 0.18, 40))
    print(visual_curve(days,probability,patient_zero_health))
    # print(visual_curve(90, 0.18, 40))
# do not add code here (outside the main block).
