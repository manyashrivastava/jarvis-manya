import subprocess
import os


def open_application(command):

    command = command.lower()

    # Google Chrome
    if "chrome" in command:

        chrome_paths = [

            r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",

            os.path.expandvars(
                r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
            )

        ]

        for path in chrome_paths:

            if os.path.exists(path):

                subprocess.Popen(
                    [path]
                )

                return "Opening Google Chrome"

        return "Google Chrome is not installed in the default location"

    # VS Code
    if (
        "vs code" in command
        or "visual studio code" in command
    ):

        subprocess.Popen(
            "code",
            shell=True
        )

        return "Opening Visual Studio Code"

    # Notepad
    if "notepad" in command:

        subprocess.Popen(
            "notepad.exe"
        )

        return "Opening Notepad"

    # Calculator
    if (
        "calculator" in command
        or "calc" in command
    ):

        subprocess.Popen(
            "calc.exe"
        )

        return "Opening Calculator"

    # File Explorer
    if (
        "file explorer" in command
        or "explorer" in command
    ):

        subprocess.Popen(
            "explorer.exe"
        )

        return "Opening File Explorer"

    return None