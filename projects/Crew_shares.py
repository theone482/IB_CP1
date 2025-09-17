# IB 2nd crew shares 

total_earnings = float(input("How much money was earned in total? "))
crew_members = int(input("How many crew members are there (excluding captain and first mate)? "))

captain_share = total_earnings * 0.25 # Captain gets 25%
first_mate_share = total_earnings * 0.15 # First mate gets 15%

remaining_money = total_earnings - captain_share - first_mate_share

if crew_members > 0:
crew_share = remaining_money / crew_members
else:
crew_share = 0 # No crew to share with


