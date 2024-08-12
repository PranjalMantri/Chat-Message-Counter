import re

# If the line starts with date and time it is a new message, else it is continuation of above message
pattern = r"\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\s*[ap]m\s*-"

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
                    del number
                else:
                    print(f"{selected_name} is not a valid name. Please enter again")
            else:
                new_name = input("Enter the name of the person to whom the number belongs to: ")

                message_data[new_name] = message_data.pop(number)
                print(f"Updated the contact list")

    
    return message_data


# to check the number of messages are accurate
matched = 0
not_matched = 0

messages = []

with open("chat.txt", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        # Check if there is date and time at the start of the message
        match = re.match(pattern, line)

        if match:
            # Strip the date and time from the message
            stripped_line = line[match.end():].strip()
            messages.append(stripped_line)
        else:
            # If no date and time are found, append the line to the previous message
            last_message = messages[-1]
            last_message += line
            messages[-1] = last_message
            
print(f"Matched pattern: {matched}")
print(f"Not matched pattern: {not_matched}")
print(f"Total messages: {len(messages)}")

# for i in range(10):
#     print(messages[i])

person_message_data = {}

for message in messages:
    if ":" in message:
        name, message = message.split(":", 1)

        message_dict = {
            "text": 0,
            "media": 0
        }

        if name not in person_message_data:
            person_message_data[name] = message_dict
        
        if "<Media omitted>" in message:
            message_type = "Media"
            person_message_data[name]["media"] += 1
        else:
            person_message_data[name]["text"] += 1


print(person_message_data)
person_message_data = update_contact_names(person_message_data)
print(person_message_data)






