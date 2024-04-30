
def week_day():
    week_day_names = [
        "Mon","Tue",
        "Wed","Thu",
        "Fri","Sat",
        "Sun"
    ]
    
    match week_day_names[5]:
        case "Mon":
            print("paneer")
        case "Tue":
            print("fish curry")
        case "Wed":
            print("egg curry")
        case "Thu":
            print("roti_dalmaa")
        case "Fri":
            print("chiken_fry")
        case "Sat":
            print("salat")
        case "Sun":
            print("roaming outside")
        
    return

def main():
    week_day()
    return
main()