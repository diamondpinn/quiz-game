import tkinter as tk
from tkinter import messagebox
import random

class NigerianQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Nigerian Quiz")
        self.root.configure(bg="#e0f7fa")  # Light blue background

        self.questions = [
            {
                "question": "What is the capital of Nigeria?",
                "options": ["Abuja", "Lagos", "Kano", "Ibadan"],
                "correct_option": "Abuja"
            },
            {
                "question": "Which river is the longest in Nigeria?",
                "options": ["Niger", "Benue", "Osun", "Ogun"],
                "correct_option": "Niger"
            },
            {
                "question": "What is the largest ethnic group in Nigeria?",
                "options": ["Hausa", "Yoruba", "Igbo", "Edo"],
                "correct_option": "Hausa"
            },
            {
                "question": "Who is the first President of Nigeria?",
                "options": ["Nnamdi Azikiwe", "Olusegun Obasanjo", "Shehu Shagari", "Goodluck Jonathan"],
                "correct_option": "Nnamdi Azikiwe"
            },
            {
                "question": "Which Nigerian city is known as the 'Centre of Excellence'?",
                "options": ["Lagos", "Abuja", "Kano", "Ibadan"],
                "correct_option": "Lagos"
            },
            {
                "question": "Which country borders Nigeria to the north?",
                "options": ["Niger", "Ghana", "Cameroon", "Chad"],
                "correct_option": "Niger"
            },
            {
                "question": "What is the currency of Nigeria?",
                "options": ["Naira", "Cedi", "Rand", "Shilling"],
                "correct_option": "Naira"
            },
            {
                "question": "Which Nigerian musician is known as the 'African Giant'?",
                "options": ["Burna Boy", "Wizkid", "Davido", "Tiwa Savage"],
                "correct_option": "Burna Boy"
            },
            {
                "question": "What is the most populous city in Nigeria?",
                "options": ["Lagos", "Kano", "Ibadan", "Abuja"],
                "correct_option": "Lagos"
            },
            {
                "question": "In which year did Nigeria gain independence?",
                "options": ["1960", "1956", "1970", "1985"],
                "correct_option": "1960"
            },
            # Additional questions
            {
                "question": "What is the official language of Nigeria?",
                "options": ["English", "Hausa", "Yoruba", "Igbo"],
                "correct_option": "English"
            },
            {
                "question": "Who is the current President of Nigeria?",
                "options": ["Muhammadu Buhari", "Goodluck Jonathan", "Olusegun Obasanjo", "Yakubu Gowon"],
                "correct_option": "Muhammadu Buhari"
            },
            {
                "question": "Which Nigerian dish is made from cassava?",
                "options": ["Garri", "Jollof Rice", "Pounded Yam", "Efo Riro"],
                "correct_option": "Garri"
            },
            {
                "question": "What is the nickname for the Nigerian national football team?",
                "options": ["Super Eagles", "Black Stars", "Lions of Teranga", "Pharaohs"],
                "correct_option": "Super Eagles"
            },
            {
                "question": "Which Nigerian author wrote the novel 'Things Fall Apart'?",
                "options": ["Chinua Achebe", "Wole Soyinka", "Chimamanda Adichie", "Ben Okri"],
                "correct_option": "Chinua Achebe"
            },
            {
                "question": "What is the meaning of the Nigerian word 'Naija'?",
                "options": ["Nigeria", "Hello", "Goodbye", "Beautiful"],
                "correct_option": "Nigeria"
            },
            {
                "question": "Which city is home to the Aso Rock?",
                "options": ["Abuja", "Lagos", "Enugu", "Kano"],
                "correct_option": "Abuja"
            },
            {
                "question": "Which Nigerian river is famous for the Kainji Dam?",
                "options": ["Niger", "Benue", "Osun", "Ogun"],
                "correct_option": "Niger"
            },
            {
                "question": "What is the largest natural landmark in Nigeria?",
                "options": ["Zuma Rock", "Aso Rock", "Olumo Rock", "Idanre Hills"],
                "correct_option": "Zuma Rock"
            },
            {
                "question": "Which Nigerian state is known as the 'Gateway State'?",
                "options": ["Ogun", "Lagos", "Ondo", "Ekiti"],
                "correct_option": "Ogun"
            },
        ]

        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), bg="#e0f7fa")  # Light blue background
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), width=20, command=lambda i=i: self.check_answer(i), bg="#4fc3f7")  # Blue button
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            question = question_data["question"]
            options = question_data["options"]

            random.shuffle(options)  # Shuffle options for randomness
            correct_option = question_data["correct_option"]

            self.question_label.config(text=question)

            for i in range(4):
                self.option_buttons[i].config(text=options[i], state=tk.NORMAL, bg="#4fc3f7")  # Blue button

        else:
            self.display_score()

    def check_answer(self, selected_option):
        selected_option_text = self.option_buttons[selected_option].cget("text")
        correct_option = self.questions[self.current_question_index]["correct_option"]

        if selected_option_text == correct_option:
            self.score += 1

        self.current_question_index += 1
        self.next_question()

    def display_score(self):
        result = f"You scored {self.score} out of {len(self.questions)}"
        messagebox.showinfo("Quiz Over", result)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz = NigerianQuiz(root)
    root.mainloop()
