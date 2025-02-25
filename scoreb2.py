import tkinter as tk

class BasketballScoreTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Basketball Score Tracker")

        self.team1_score = 0
        self.team2_score = 0
        self.running = False
        self.time_left = 10 * 60  # 10 minutes in seconds

        # Create the layout
        self.create_widgets()

    def create_widgets(self):
        # Team 1 Score
        self.team1_label = tk.Label(self.root, text="Home", font=("Helvetica", 18))
        self.team1_label.grid(row=0, column=0, padx=10, pady=10)

        self.team1_score_label = tk.Label(self.root, text="0", font=("Helvetica", 18))
        self.team1_score_label.grid(row=1, column=0, padx=10, pady=10)

        self.team1_score_button = tk.Button(self.root, text="Add Point", command=self.add_point_team1)
        self.team1_score_button.grid(row=2, column=0, padx=10, pady=10)

        # Team 2 Score
        self.team2_label = tk.Label(self.root, text="Away", font=("Helvetica", 18))
        self.team2_label.grid(row=0, column=2, padx=10, pady=10)

        self.team2_score_label = tk.Label(self.root, text="0", font=("Helvetica", 18))
        self.team2_score_label.grid(row=1, column=2, padx=10, pady=10)

        self.team2_score_button = tk.Button(self.root, text="Add Point", command=self.add_point_team2)
        self.team2_score_button.grid(row=2, column=2, padx=10, pady=10)

        # Timer
        self.timer_label = tk.Label(self.root, text="10:00", font=("Helvetica", 18))
        self.timer_label.grid(row=0, column=1, padx=10, pady=10)

        # Control Buttons
        self.start_stop_button = tk.Button(self.root, text="Start/Stop Timer", command=self.toggle_timer)
        self.start_stop_button.grid(row=2, column=1, padx=10, pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=1, padx=10, pady=10)




