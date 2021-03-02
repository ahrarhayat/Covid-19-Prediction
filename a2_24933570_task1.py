# Student Name: Ahrar Hayat
# ID: 24933570
# Start Date: Sunday, 17 May 2020 at 5:52 pm
# Last Modified: Friday, 5 June 2020 at 12:55 am
# Description: This file contains a Person class. Names of people and their friends
# are read from a text file and objects of the people are created and are linked with
# objects of their friends
# Task 1 code template for FIT9136 Assignment 2.


class Person:
    name = str('unknown')
    friends = []

    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name
        self.friends = []

    def add_friend(self, friend_person):
        self.friends.append(friend_person)

    def get_name(self):
        return self.name

    def get_friends(self):
        return self.friends


# this method searches for a person in a given list by matching with a given person's name

def search_friend(friend_name, person_list):
    for person_1 in person_list:
        if person_1.get_name() == friend_name:
            return person_1


def load_people():
    input_handle = open('a2_sample_set.txt', 'r')
    person_list = []
    line_counter = 0
    for line in input_handle.readlines():
        line_counter += 1
        split_name = line.split(': ')
        person_name = split_name.__getitem__(0)
        person_f_name = person_name.split(' ').__getitem__(0)
        person_l_name = person_name.split(' ').__getitem__(1)
        # create a person object with the extracted first and last name from the file
        person = Person(person_f_name, person_l_name)
        person_list.append(person)
        input_handle.close()
    # print(person_list.__len__())
    input_handle = open('a2_sample_set.txt', 'r')
    # i determines the position of the person object (parallel to the file) in the list will add friends
    i = 0
    # iterate through the file lines again and this time extract the name of the friends, find them
    # in the person list and add the object as friends to the corresponding person
    for line2 in input_handle.readlines():
        split_name = line2.split(': ')
        friend_names = split_name.__getitem__(1).rstrip('\n').split(', ')
        for friend_i in friend_names:
            friend_person = search_friend(friend_i, person_list)
            person_list[i].add_friend(friend_person)
            # print(friend_person.get_name(),person_list[i].get_name())
        i += 1
    input_handle.close()
    # return the list created
    return person_list


if __name__ == '__main__':
    # To visualize the objects linked to each other as friends
    person_list_i = load_people()
    print('Size of list', len(person_list_i))
    print('\n')
    for person in person_list_i:
        print(person.get_name(), ': ', end='')
        for friend in person.get_friends():
            print(friend.get_name(), ', ', end='')
        print('\n')

# do not add code here (outside the main block).
