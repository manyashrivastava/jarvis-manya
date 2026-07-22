import threading

from gui.jarvis_gui import JarvisGUI

from voice.listener import listen
from voice.speaker import speak

from commands.web_commands import open_website
from commands.app_commands import open_application
from commands.system_commands import system_command

from brain.ai_engine import get_ai_response


class JarvisController:

    def __init__(self, gui):

        self.gui = gui
        self.running = True

        # GUI ko controller se connect karna
        self.gui.controller = self

    def process_command(self, command):

        if not command:
            return

        command = command.lower().strip()

        self.gui.add_activity(
            f"[USER] {command}"
        )

        # =========================
        # EXIT COMMANDS
        # =========================

        if command in [
            "exit",
            "quit",
            "stop",
            "goodbye",
            "shutdown jarvis"
        ]:

            response = "Goodbye Manya. See you soon."

            speak(response)

            self.gui.add_activity(
                f"[JARVIS] {response}"
            )

            self.running = False

            return

        # =========================
        # WEBSITE COMMANDS
        # =========================

        response = open_website(command)

        if response:

            speak(response)

            self.gui.add_activity(
                f"[JARVIS] {response}"
            )

            return

        # =========================
        # APPLICATION COMMANDS
        # =========================

        response = open_application(command)

        if response:

            speak(response)

            self.gui.add_activity(
                f"[JARVIS] {response}"
            )

            return

        # =========================
        # SYSTEM COMMANDS
        # =========================

        response = system_command(command)

        if response:

            speak(response)

            self.gui.add_activity(
                f"[JARVIS] {response}"
            )

            return

        # =========================
        # AI RESPONSE
        # =========================

        self.gui.set_status(
            "● THINKING...",
            "#FFD700"
        )

        response = get_ai_response(command)

        speak(response)

        self.gui.add_activity(
            f"[JARVIS] {response}"
        )


# =========================================
# CONTINUOUS VOICE LISTENER
# =========================================

def voice_loop(controller):

    speak(
        "Hello Manya. Jarvis is online."
    )

    controller.gui.add_activity(
        "[SYSTEM] Jarvis is online."
    )

    while controller.running:

        try:

            controller.gui.set_status(
                "● LISTENING...",
                "#00BFFF"
            )

            command = listen()

            if command:

                controller.gui.set_status(
                    "● THINKING...",
                    "#FFD700"
                )

                controller.process_command(
                    command
                )

                controller.gui.set_status(
                    "● READY",
                    "#00FF9D"
                )

        except Exception as error:

            print(
                f"Voice Error: {error}"
            )

            controller.gui.add_activity(
                f"[ERROR] {error}"
            )

            controller.gui.set_status(
                "● ERROR",
                "#FF4444"
            )


# =========================================
# START JARVIS
# =========================================

def main():

    app = JarvisGUI()

    controller = JarvisController(
        app
    )

    # Background voice thread
    voice_thread = threading.Thread(
        target=voice_loop,
        args=(controller,),
        daemon=True
    )

    voice_thread.start()

    # Start GUI
    app.mainloop()


if __name__ == "__main__":

    main()