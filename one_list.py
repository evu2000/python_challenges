""" Merge individual members of a list containing lists """

my_list = [[1,2],[3,4],[5]]

print([individual_member for individual_list in my_list for individual_member in individual_list])
