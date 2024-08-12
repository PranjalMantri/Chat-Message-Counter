
def organise_message_data(messages):
    message_data = {}

    for message in messages:
        if ":" in message:
            name, message = message.split(":", 1)

            message_dict = {
                "text": 0,
                "media": 0
            }

            if name not in message_data:
                message_data[name] = message_dict
            
            if "<Media omitted>" in message:
                message_type = "Media"
                message_data[name]["media"] += 1
            else:
                message_data[name]["text"] += 1

    return message_data


def update_contact_names(message_data):
    for number in list(message_data.keys()):
        if number.startswith("+") or not any(char.isalpha() for char in number):
            print(f"The number {number} is not associated with any name.")

            print("Here are the existing names in the contact list")
            for existing_name in message_data.keys():
                if existing_name != number and not (existing_name.startswith("+")):
                    print(f" - {existing_name}")
            
            choice = input("Does this number belong to any of the above given names? (yes/no): ").strip().lower()

            if choice == "yes":
                selected_name = input("Please enter the name to whom the number belongs to: ").strip()

                if selected_name in message_data:
                    message_data[selected_name]["text"] += message_data[number]["text"]
                    message_data[selected_name]["media"] += message_data[number]["media"]
                    print(f"Data from {number} has been appended to {selected_name}")
                    del message_data[number]
                else:
                    print(f"{selected_name} is not a valid name. Please enter again")
            else:
                new_name = input("Enter the name of the person to whom the number belongs to: ")

                message_data[new_name] = message_data.pop(number)
                print(f"Updated the contact list")

    
    return message_data