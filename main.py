import re

pattern = r"\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\s*[ap]m\s*-"

matched = 0
not_matched = 0

messages = []

with open("sample-chat.txt", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if re.match(pattern, line):
            matched += 1
            messages.append(line)
        else:
            not_matched += 1
            last_message = messages[-1]
            last_message += line
            messages[-1] = last_message
            
print(f"Matched pattern: {matched}")
print(f"Not matched pattern: {not_matched}")
print(f"Total messages: {len(messages)}")