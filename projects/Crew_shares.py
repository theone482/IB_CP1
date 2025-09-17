# IB 2nd crew shares 
def calculate_shares(total_earnings, crew_count):
    total_shares = 7 + 3 + crew_count
    share_value = total_earnings / total_shares
    captain_earnings = 7 * share_value
    first_mate_earnings = 3 * share_value
    crew_total_share = share_value
    crew_remaining = crew_total_share - 500
    print(f"How much was earned: ${total_earnings:,.2f}")
    print(f"How many crew members are there (not including the captain and first mate): {crew_count}")
    print(f"The captain gets: ${captain_earnings:,.2f}")
    print(f"The first mate gets: ${first_mate_earnings:,.2f}")
    print(f"Crew still needs: ${crew_remaining:,.2f}")
calculate_shares(50000.00, 30)


