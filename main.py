import matplotlib.pyplot as plt
from src.get_data import get_messages
from src.enhance_data import *
from src.visualize import plot_contact_data

file_path = "public/chat.txt"
messages = get_messages(file_path)
print(f"There are total {len(messages)} lines in the file")

message_data = update_contact_names(organise_message_data(messages))

fig, ax = plot_contact_data(message_data)
plt.show()
