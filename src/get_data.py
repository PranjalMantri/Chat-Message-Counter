import re


def get_messages(file_name):
    pattern = r"\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\s*[ap]m\s*-"

    messages = []

    with open(file_name, encoding="utf-8") as file:
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
    
    return messages


if __name__ == "__main__":
    messages = get_messages("public/sample-chat.txt")
    print(len(messages))

    messages = get_messages("public/chat.txt")
    print(len(messages))