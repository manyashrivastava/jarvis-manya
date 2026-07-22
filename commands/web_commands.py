import webbrowser


def open_website(command):

    command = command.lower()

    websites = {

        "youtube": "https://www.youtube.com",

        "google": "https://www.google.com",

        "github": "https://github.com",

        "chatgpt": "https://chatgpt.com",

        "gmail": "https://mail.google.com",

        "instagram": "https://www.instagram.com",

        "facebook": "https://www.facebook.com",

        "linkedin": "https://www.linkedin.com"

    }

    for name, url in websites.items():

        if name in command:

            webbrowser.open(url)

            return f"Opening {name}"

    return None