import matplotlib.pyplot as plt

def plot_contact_data(messages_data):
    names = list(messages_data.keys())
    texts = [messages_data[name]["text"] for name in names]
    media = [messages_data[name]["media"] for name in names]

    x = range(len(names))

    fig, ax = plt.subplots()

    # Create bars for text
    bars_text = ax.bar(x, texts, width=0.4, label='Text', color='b', align='center')

    # Create bars for media, slightly offset to the right
    bars_media = ax.bar([i + 0.4 for i in x], media, width=0.4, label='Media', color='r', align='center')

    # Add labels and title
    ax.set_xlabel('Contacts')
    ax.set_ylabel('Count')
    ax.set_title('Text and Media Counts by Contact')
    ax.set_xticks([i + 0.2 for i in x])
    ax.set_xticklabels(names, rotation=45, ha='right')

    # Add a legend
    ax.legend()

    # Display the bar chart
    plt.tight_layout()

    return fig, ax

