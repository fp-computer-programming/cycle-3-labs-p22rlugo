# Ryan Lugo: RJL 9/29/21

team_input = input("How many points did A Team get?: ")
a_team_points = int(team_input)

if a_team_points >= 15:
    print('Gold Medal has been awarded!')
elif a_team_points >= 12:
    print("Silver Medal has been awarded!")
elif a_team_points >= 9:
    print("Bronze Medal has been awarded!")
else:
    print("The team has won no Medals..")