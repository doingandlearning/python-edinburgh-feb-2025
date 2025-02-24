def print_msg():
    """
    A function that prints a message
    Returns: None
    """
    print("Hello!")

print_msg()

def print_msg(message, speaker="Kevin", volume="normal"):
    print(f"{speaker} (at {volume} volume): {message}")


print_msg("Hello", "Nick", "quiet")

print_msg("Hi", "Stephen")
print_msg("Python is great")
print_msg(message="Functions are cool!", volume="excited")
