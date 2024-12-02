import tkinter as tk
import time
import random

class ReactionTest:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reaction Time Test")
        self.root.geometry("400x300")
        
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack(fill="both", expand=True)
        
        # Initialize variables
        self.start_time = 0
        self.waiting_for_green = False
        
        # Create initial red screen
        self.canvas.configure(bg="red")
        self.text = self.canvas.create_text(
            200, 150,
            text="Click when green",
            font=("Arial", 20),
            fill="white"
        )
        
        # Bind click event
        self.canvas.bind("<Button-1>", self.handle_click)
        
        # Start the test
        self.start_test()
        
        self.root.mainloop()
    
    def start_test(self):
        # Random delay between 1-5 seconds
        delay = random.uniform(1, 5)
        self.root.after(int(delay * 1000), self.turn_green)
        self.waiting_for_green = True
    
    def turn_green(self):
        self.canvas.configure(bg="green")
        self.start_time = time.time()
        self.waiting_for_green = False
    
    def handle_click(self, event):
        if self.waiting_for_green:
            # Clicked too early
            self.canvas.configure(bg="red")
            self.canvas.itemconfig(self.text, text="Too early! Click to try again", fill="white")
            self.waiting_for_green = False
        elif not self.waiting_for_green and self.start_time > 0:
            # Calculate reaction time
            reaction_time = (time.time() - self.start_time) * 1000  # Convert to milliseconds
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(
                self.text,
                text=f"Reaction time: {reaction_time:.0f}ms\nClick to try again",
                fill="black"  # Change text color to black for white background
            )
            print(f"Reaction time: {reaction_time:.0f}ms")  # Debug print
            self.start_time = 0
        else:
            # Reset and start new test
            self.canvas.configure(bg="red")
            self.canvas.itemconfig(self.text, text="Click when green", fill="white")
            self.start_test()

if __name__ == "__main__":
    ReactionTest()
