
def main():
    user_name = "theprakash"
    user_age = 27
    age_limit = 18
    total_ticket = 12
    booked_ticket = 0
    if (user_age >= age_limit):
        print(f"Hello {user_name}")
        print("book ticket")
        booked_ticket = 4
        print(f"you booked {booked_ticket}")
        print("Available Tickets",total_ticket - booked_ticket)
    else:
        print("not eligible")
    return
main()