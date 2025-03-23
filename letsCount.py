import tkinter as tk
from tkinter import messagebox
import random

class CountingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Counting Game for Kids")
        self.root.geometry("800x600")
        self.root.configure(bg="#fbe7c6")  # Light Peach Background

        self.current_number = 0
        self.score = 0

        # Title Label
        self.title_label = tk.Label(
            root, text="Counting Game!", font=("Comic Sans MS", 28, "bold"),
            bg="#fbe7c6", fg="#ff6f61"
        )
        self.title_label.pack(pady=20)

        # Instruction Label
        self.instruction_label = tk.Label(
            root, text="Count the stars and type your answer below:",
            font=("Comic Sans MS", 18), bg="#fbe7c6", fg="#4a90e2"
        )
        self.instruction_label.pack(pady=10)

        # Canvas for Stars
        self.canvas = tk.Canvas(root, width=600, height=300, bg="#fff9c4")
        self.canvas.pack(pady=20)

        # Answer Entry
        self.answer_entry = tk.Entry(root, font=("Comic Sans MS", 20), justify="center")
        self.answer_entry.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(
            root, text="Submit", font=("Comic Sans MS", 16, "bold"),
            bg="#4a90e2", fg="#ffffff", command=self.check_answer
        )
        self.submit_button.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(
            root, text=f"Score: {self.score}", font=("Comic Sans MS", 20, "bold"),
            bg="#fbe7c6", fg="#ffcc00"
        )
        self.score_label.pack(pady=10)

        # Start Game
        self.generate_stars()

    def generate_stars(self):
        """Generate a random number of stars on the canvas."""
        self.canvas.delete("all")  # Clear previous stars
        self.current_number = random.randint(1, 10)  # Random number of stars
        star_image = tk.PhotoImage(file="star.png")  # Use an image of a star
        self.star_image = star_image  # Prevent garbage collection

        for i in range(self.current_number):
            x = random.randint(50, 550)
            y = random.randint(50, 250)
            self.canvas.create_image(x, y, image=star_image)

    def check_answer(self):
        """Check if the user's answer is correct."""
        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a number!")
            return

        if user_answer == self.current_number:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct!", "Great job! You counted correctly!")
            self.generate_stars()
        else:
            messagebox.showerror("Try Again", f"Oops! The correct number was {self.current_number}.")
            self.generate_stars()

        self.answer_entry.delete(0, tk.END)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    game = CountingGame(root)
    root.mainloop()