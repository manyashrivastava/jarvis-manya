import customtkinter as ctk
import tkinter as tk
import threading
import time


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class JarvisGUI(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(
            "J.A.R.V.I.S. - Personal AI Assistant"
        )

        self.geometry(
            "1200x750"
        )

        self.minsize(
            1000,
            650
        )

        self.configure(
            fg_color="#050810"
        )

        self.is_running = True
        self.angle = 0

        # Controller main.py se connect hoga
        self.controller = None

        self.create_interface()

        self.animate_core()

    # =================================
    # MAIN INTERFACE
    # =================================

    def create_interface(self):

        # =============================
        # SIDEBAR
        # =============================

        self.sidebar = ctk.CTkFrame(
            self,
            width=230,
            corner_radius=0,
            fg_color="#080D18"
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="J.A.R.V.I.S.",
            font=("Arial", 25, "bold"),
            text_color="#00BFFF"
        )

        self.logo.pack(
            pady=(35, 5)
        )

        self.subtitle = ctk.CTkLabel(
            self.sidebar,
            text="PERSONAL AI SYSTEM",
            font=("Arial", 10),
            text_color="#6F8299"
        )

        self.subtitle.pack(
            pady=(0, 40)
        )

        # Sidebar buttons
        self.create_sidebar_button(
            "⌂  Dashboard"
        )

        self.create_sidebar_button(
            "◉  Voice Assistant"
        )

        self.create_sidebar_button(
            "◈  Memory"
        )

        self.create_sidebar_button(
            "⚙  Settings"
        )

        # System status
        self.status = ctk.CTkLabel(
            self.sidebar,
            text="●  SYSTEM ONLINE",
            font=("Arial", 12, "bold"),
            text_color="#00FF9D"
        )

        self.status.pack(
            side="bottom",
            pady=(0, 15)
        )

        self.status_title = ctk.CTkLabel(
            self.sidebar,
            text="SYSTEM STATUS",
            font=("Arial", 11, "bold"),
            text_color="#6F8299"
        )

        self.status_title.pack(
            side="bottom",
            pady=(0, 70)
        )

        # =============================
        # MAIN AREA
        # =============================

        self.main_area = ctk.CTkFrame(
            self,
            fg_color="#050810",
            corner_radius=0
        )

        self.main_area.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =============================
        # HEADER
        # =============================

        self.header = ctk.CTkFrame(
            self.main_area,
            height=70,
            fg_color="#080D18",
            corner_radius=0
        )

        self.header.pack(
            fill="x"
        )

        self.header_title = ctk.CTkLabel(
            self.header,
            text="JARVIS CONTROL CENTER",
            font=("Arial", 18, "bold"),
            text_color="#FFFFFF"
        )

        self.header_title.pack(
            side="left",
            padx=30,
            pady=20
        )

        self.clock = ctk.CTkLabel(
            self.header,
            text="",
            font=("Arial", 13),
            text_color="#00BFFF"
        )

        self.clock.pack(
            side="right",
            padx=30
        )

        self.update_clock()

        # =============================
        # CONTENT
        # =============================

        self.content = ctk.CTkFrame(
            self.main_area,
            fg_color="#050810"
        )

        self.content.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        # =============================
        # AI CORE SECTION
        # =============================

        self.core_section = ctk.CTkFrame(
            self.content,
            fg_color="#080D18",
            corner_radius=20
        )

        self.core_section.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 15)
        )

        self.core_title = ctk.CTkLabel(
            self.core_section,
            text="ARTIFICIAL INTELLIGENCE CORE",
            font=("Arial", 14, "bold"),
            text_color="#6F8299"
        )

        self.core_title.pack(
            pady=(25, 10)
        )

        self.canvas = tk.Canvas(
            self.core_section,
            width=450,
            height=420,
            bg="#080D18",
            highlightthickness=0
        )

        self.canvas.pack(
            expand=True
        )

        self.core_status = ctk.CTkLabel(
            self.core_section,
            text="● READY",
            font=("Arial", 16, "bold"),
            text_color="#00FF9D"
        )

        self.core_status.pack(
            pady=(0, 20)
        )

        # =============================
        # RIGHT PANEL
        # =============================

        self.right_panel = ctk.CTkFrame(
            self.content,
            width=320,
            fg_color="#080D18",
            corner_radius=20
        )

        self.right_panel.pack(
            side="right",
            fill="y"
        )

        self.right_panel.pack_propagate(
            False
        )

        self.activity_title = ctk.CTkLabel(
            self.right_panel,
            text="ACTIVITY MONITOR",
            font=("Arial", 14, "bold"),
            text_color="#6F8299"
        )

        self.activity_title.pack(
            pady=(25, 15)
        )

        self.activity_box = ctk.CTkTextbox(
            self.right_panel,
            width=270,
            height=250,
            corner_radius=12,
            fg_color="#050810",
            text_color="#B7C7D9",
            font=("Consolas", 12)
        )

        self.activity_box.pack(
            padx=20,
            pady=10
        )

        self.activity_box.configure(
            state="disabled"
        )

        # =============================
        # ACTIVATE BUTTON
        # =============================

        self.voice_button = ctk.CTkButton(
            self.right_panel,
            text="🎙  ACTIVATE JARVIS",
            height=50,
            corner_radius=12,
            font=("Arial", 14, "bold"),
            fg_color="#0066CC",
            hover_color="#0088FF",
            command=self.activate_jarvis
        )

        self.voice_button.pack(
            padx=25,
            pady=20,
            fill="x"
        )

        # =============================
        # COMMAND INPUT
        # =============================

        self.input_box = ctk.CTkEntry(
            self.right_panel,
            placeholder_text="Type a command...",
            height=40,
            corner_radius=10
        )

        self.input_box.pack(
            padx=25,
            pady=(0, 10),
            fill="x"
        )

        self.send_button = ctk.CTkButton(
            self.right_panel,
            text="SEND COMMAND",
            height=40,
            command=self.send_command
        )

        self.send_button.pack(
            padx=25,
            pady=5,
            fill="x"
        )

    # =================================
    # SIDEBAR BUTTONS
    # =================================

    def create_sidebar_button(self, text):

        button = ctk.CTkButton(
            self.sidebar,
            text=text,
            anchor="w",
            height=45,
            corner_radius=8,
            fg_color="transparent",
            hover_color="#101C30",
            text_color="#B7C7D9",
            font=("Arial", 13),
            command=lambda: self.sidebar_action(text)
        )

        button.pack(
            padx=15,
            pady=5,
            fill="x"
        )

    # =================================
    # SIDEBAR ACTIONS
    # =================================

    def sidebar_action(self, button_name):

        if "Dashboard" in button_name:

            self.add_activity(
                "[SYSTEM] Dashboard selected."
            )

        elif "Voice Assistant" in button_name:

            self.add_activity(
                "[SYSTEM] Voice Assistant selected."
            )

            self.activate_jarvis()

        elif "Memory" in button_name:

            self.add_activity(
                "[SYSTEM] Memory module selected."
            )

        elif "Settings" in button_name:

            self.add_activity(
                "[SYSTEM] Settings selected."
            )

    # =================================
    # ACTIVATE JARVIS
    # =================================

    def activate_jarvis(self):

        self.set_status(
            "● LISTENING...",
            "#00BFFF"
        )

        self.add_activity(
            "[VOICE] Listening for command..."
        )

        if self.controller:

            threading.Thread(
                target=self.listen_once,
                daemon=True
            ).start()

    # =================================
    # LISTEN ONCE
    # =================================

    def listen_once(self):

        try:

            from voice.listener import listen

            command = listen()

            if command and self.controller:

                self.set_status(
                    "● THINKING...",
                    "#FFD700"
                )

                self.controller.process_command(
                    command
                )

                self.set_status(
                    "● READY",
                    "#00FF9D"
                )

        except Exception as error:

            self.add_activity(
                f"[ERROR] {error}"
            )

            self.set_status(
                "● ERROR",
                "#FF4444"
            )

    # =================================
    # SEND TEXT COMMAND
    # =================================

    def send_command(self):

        command = self.input_box.get().strip()

        if not command:

            return

        self.input_box.delete(
            0,
            "end"
        )

        self.set_status(
            "● THINKING...",
            "#FFD700"
        )

        if self.controller:

            threading.Thread(
                target=self.controller.process_command,
                args=(command,),
                daemon=True
            ).start()

    # =================================
    # STATUS UPDATE
    # =================================

    def set_status(self, text, color):

        self.after(
            0,
            lambda: self.core_status.configure(
                text=text,
                text_color=color
            )
        )

    # =================================
    # ACTIVITY LOG
    # =================================

    def add_activity(self, message):

        self.after(
            0,
            self._add_activity,
            message
        )

    def _add_activity(self, message):

        self.activity_box.configure(
            state="normal"
        )

        self.activity_box.insert(
            "end",
            message + "\n"
        )

        self.activity_box.see(
            "end"
        )

        self.activity_box.configure(
            state="disabled"
        )

    # =================================
    # ANIMATED CORE
    # =================================

    def animate_core(self):

        if not self.is_running:

            return

        self.canvas.delete(
            "all"
        )

        center_x = 225
        center_y = 210

        for radius in [
            150,
            125,
            100
        ]:

            self.canvas.create_oval(
                center_x - radius,
                center_y - radius,
                center_x + radius,
                center_y + radius,
                outline="#0066CC",
                width=2
            )

        self.canvas.create_arc(
            center_x - 150,
            center_y - 150,
            center_x + 150,
            center_y + 150,
            start=self.angle,
            extent=90,
            outline="#00BFFF",
            width=5
        )

        self.canvas.create_oval(
            center_x - 65,
            center_y - 65,
            center_x + 65,
            center_y + 65,
            fill="#0066CC",
            outline="#00BFFF",
            width=4
        )

        self.canvas.create_text(
            center_x,
            center_y,
            text="JARVIS",
            fill="white",
            font=("Arial", 18, "bold")
        )

        self.angle += 4

        self.after(
            40,
            self.animate_core
        )

    # =================================
    # CLOCK
    # =================================

    def update_clock(self):

        current_time = time.strftime(
            "%H:%M:%S"
        )

        self.clock.configure(
            text=current_time
        )

        self.after(
            1000,
            self.update_clock
        )


if __name__ == "__main__":

    app = JarvisGUI()

    app.mainloop()