import os


def system_command(command):

    command = command.lower()

    if (
        "shutdown computer" in command
        or "shut down computer" in command
    ):

        os.system(
            "shutdown /s /t 10"
        )

        return "Computer will shut down in 10 seconds"

    if (
        "restart computer" in command
        or "restart system" in command
    ):

        os.system(
            "shutdown /r /t 10"
        )

        return "Computer will restart in 10 seconds"

    if (
        "cancel shutdown" in command
    ):

        os.system(
            "shutdown /a"
        )

        return "Shutdown cancelled"

    return None