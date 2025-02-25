import datetime

def write_to_log(message):
    with open("new.txt", "a") as file:
        # file.write("Hello! How are you?\n")
        file.write(f"{datetime.datetime.now()}: {message}\n")
        # file.writelines(["I'm fine thanks\n", "How are you?\n"])


write_to_log("ERROR: Something went wrong")
write_to_log("INFO: Server started")