# Student Name: Ahrar Hayat
# ID: 24933570
# Start Date: Sunday, 17 May 2020 at 5:52 pm
# Last Modified: Friday, 5 June 2020 at 12:55 am
# Description: This file contains a Patient class, which is a child class of the Person
# class, this is where a simulation is run to based on a patient visiting their friend
# and infecting them too, and the result of the spread or flattening of the virus is recorded
# Task 2 code template for FIT9136 Assignment 2.

from a2_24933570_task1 import *
import numpy as np


class Patient(Person):
    health = float(100)

    def __init__(self, first_name, last_name, health):
        self.health = health
        Person.__init__(self, first_name, last_name)

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = round(new_health)

    def is_contagious(self):
        if 76 <= self.health <= 100:
            return False
        elif 74 < self.health <= 75:
            return False
        elif 50 <= self.health <= 74:
            return False
        elif 30 <= self.health <= 49:
            return True
        elif 0 <= self.health <= 29:
            return True

    def infect(self, viral_load):
        if self.health > 0:
            if self.health <= 29:
                self.health = round(self.health - (0.1 * viral_load))
            elif 29 < self.health < 50:
                self.health = round(self.health - (1 * viral_load))
            elif self.health >= 50:
                self.health = round(self.health - (2 * viral_load))
        # if the health of a person comes out to become negative, make the health zero
        elif self.health < 0:
            self.health = 0

    def sleep(self):
        if 100 > self.health > 0:
            self.health = round(self.health) + 5


def run_simulation(days, meeting_probability, patient_zero_health):
    patient_list = load_patients(75)
    patient_zero = patient_list[0]
    patient_zero.set_health(patient_zero_health)
    # contagious_list holds the number of people infected in a single day
    contagious_list = []
    # contagious_people is a list of Patient objects who are contagious
    contagious_people = []
    # a variable that keeps track of the everyday count of contagious people each day
    count_per_day = 0
    # determine if the patient zero is contagious given the entered health and add to the list of contagious
    # people if appropriate and update the count on day 0
    if patient_zero.is_contagious():
        contagious_people.append(patient_zero)
        count_per_day = len(contagious_people)
    for day in range(days):
        # check everyday and update the list of contagious people if they don't remain contagious after
        # sleeping, remove them from the list
        if len(contagious_people) > 0:
            for contagious in contagious_people:
                if not contagious.is_contagious():
                    contagious_people.remove(contagious)
                    count_per_day = len(contagious_people)
                # print('day', day, 'removed', contagious.get_name(), 'health', contagious.health,
                # contagious.is_contagious())
        # for every patient determine if they will visit a friend or not one by one and if they
        # are contagious and visit, infect the friends visited and also infect the patient
        # update the contagious people list by checking first if the friend of the
        # patient is already in the list and update the count per day accordingly
        for patient in patient_list:
            friends = patient.get_friends()
            # calculate whether this person visits his/her friends, if the meeting probability is 0.3(subtract it
            # from 1), generate a random number between 0 and 1, if the result is greater than equal to the result,
            # he/she visits the friends
            for friend in friends:
                if patient.is_contagious():
                    will_visit = False
                    probability = float(1 - meeting_probability)
                    random_val = np.random.uniform(0, 1)
                    if random_val >= probability:
                        will_visit = True
                    # if the patient visits each other, they will infect each other if they are contagious
                    if will_visit:
                        viral_load = 5 + (((patient.get_health() - 25) ** 2) / 62)
                        friend.infect(viral_load)
                        if friend.is_contagious:
                            viral_load = 5 + (((friend.get_health() - 25) ** 2) / 62)
                            patient.infect(viral_load)
                        if not contagious_people.__contains__(friend) and friend.is_contagious():
                            contagious_people.append(friend)
                            count_per_day = len(contagious_people)
                            # print('day', day, 'added', friend.get_name(), friend.get_health(), friend.is_contagious())
            # after each day all patients will sleep
            patient.sleep()
        # add the total number of cases everyday to the contagious list
        contagious_list.append(count_per_day)
    # return the final list of day-wise number of cases
    return contagious_list


# This method is a carbon copy of the load people method in task 1, except it creates a
# patient object with an added parameter of health compared to the person object
def load_patients(initial_health):
    input_handle = open('a2_sample_set.txt', 'r')
    patient_list = []
    for line in input_handle.readlines():
        split_name = line.split(': ')
        patient_name = split_name.__getitem__(0)
        patient_f_name = patient_name.split(' ').__getitem__(0)
        patient_l_name = patient_name.split(' ').__getitem__(1)
        # create a person
        patient = Patient(patient_f_name, patient_l_name, initial_health)
        patient_list.append(patient)
        input_handle.close()
    input_handle = open('a2_sample_set.txt', 'r')
    i = 0
    for line2 in input_handle.readlines():
        split_name = line2.split(': ')
        friend_names = split_name.__getitem__(1).rstrip('\n').split(', ')
        for friend_i in friend_names:
            friend_person = search_friend(friend_i, patient_list)
            patient_list[i].add_friend(friend_person)
        i += 1
    input_handle.close()
    return patient_list


if __name__ == '__main__':
    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.
    # This is a sample test case. Write your own testing code here.
    test_result = run_simulation(40, 0.18, 40)
    # print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.

    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(60, 0.25, 49)
    print(test_result)
    # sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

    test_result = run_simulation(100, 0.77, 16)
    # print(test_result)

    test_patient_list_i = load_patients(75)
    patient_0 = test_patient_list_i[0]
    patient_0.set_health(50)
    # print(len(test_patient_list_i))
    for patient in test_patient_list_i:
        # print(patient.get_name(), 'with health', patient.get_health(), ', is friends with: ')
        for friend in patient.get_friends():
            pass
            # print(friend.get_name())
        # print('\n')
    # print(np.random.uniform(0, 1))
# do not add code here (outside the main block).
