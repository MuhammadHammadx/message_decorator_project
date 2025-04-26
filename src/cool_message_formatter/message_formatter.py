# message_formatter.py
def rectangle_message(message):
    """
    This function takes a message and returns it inside a rectangle made with * symbols.
    """

    # Find the length of the longest line
    max_length = max(len(line) for line in message.split('\n'))

    # Create the top and bottom border
    border = '*' * (max_length + 4)

    # Create the middle part with message lines
    lines = []
    for line in message.split('\n'):
        # Add * on both sides and adjust spaces
        lines.append(f"* {line.ljust(max_length)} *")

    # Combine all parts together
    final_message = border + '\n' + '\n'.join(lines) + '\n' + border
    return final_message
