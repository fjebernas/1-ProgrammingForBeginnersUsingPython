

def SlambookRequest():
    print("Hello! Im gonna ask some questions about ya!")

    details = [None] * 6

    details[0] = input("Name: ")
    details[1] = int(input("Age: "))
    details[2] = input("Favorite color: ")
    details[3] = input("Favorite movie: ")
    details[4] = int(input("Mobile number: "))
    details[5] = input("Motto in life: ")

    return details


print(SlambookRequest())