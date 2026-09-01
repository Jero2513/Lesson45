import kivy
kivy.require("2.1.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from sklearn.linear_model import LinearRegression


# ==========================================
# TRAINING DATA
# ==========================================

# [hours studied, assignments, attendance, previous score, sleep]
X = [
    [1, 2, 60, 35, 5],
    [2, 3, 65, 40, 6],
    [3, 4, 70, 45, 6],
    [4, 5, 75, 50, 7],
    [5, 6, 80, 60, 7],
    [6, 7, 85, 65, 7],
    [7, 8, 90, 75, 8],
    [8, 9, 95, 80, 8],
    [9, 10, 98, 88, 8],
    [10, 10, 100, 92, 9]
]

# Exam scores
y = [
    35,
    42,
    48,
    55,
    65,
    72,
    80,
    86,
    92,
    96
]


# ==========================================
# CREATE AND TRAIN AI MODEL
# ==========================================

model = LinearRegression()

model.fit(X, y)


# ==========================================
# AI APPLICATION
# ==========================================

class StudyAIApp(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        # ----------------------------------
        # TITLE
        # ----------------------------------

        title = Label(
            text="🤖 STUDY AI",
            font_size=28,
            size_hint_y=None,
            height=60
        )

        layout.add_widget(title)

        subtitle = Label(
            text="AI Exam Score Predictor",
            font_size=18,
            size_hint_y=None,
            height=40
        )

        layout.add_widget(subtitle)


        # ----------------------------------
        # HOURS STUDIED
        # ----------------------------------

        layout.add_widget(
            Label(text="📚 Hours studied")
        )

        self.hours = TextInput(
            hint_text="Example: 6",
            multiline=False,
            input_filter="float",
            size_hint_y=None,
            height=50
        )

        layout.add_widget(self.hours)


        # ----------------------------------
        # ASSIGNMENTS
        # ----------------------------------

        layout.add_widget(
            Label(text="📝 Assignments completed")
        )

        self.assignments = TextInput(
            hint_text="Example: 7",
            multiline=False,
            input_filter="float",
            size_hint_y=None,
            height=50
        )

        layout.add_widget(self.assignments)


        # ----------------------------------
        # ATTENDANCE
        # ----------------------------------

        layout.add_widget(
            Label(text="🏫 Attendance percentage")
        )

        self.attendance = TextInput(
            hint_text="Example: 85",
            multiline=False,
            input_filter="float",
            size_hint_y=None,
            height=50
        )

        layout.add_widget(self.attendance)


        # ----------------------------------
        # PREVIOUS SCORE
        # ----------------------------------

        layout.add_widget(
            Label(text="📖 Previous test score")
        )

        self.previous = TextInput(
            hint_text="Example: 65",
            multiline=False,
            input_filter="float",
            size_hint_y=None,
            height=50
        )

        layout.add_widget(self.previous)


        # ----------------------------------
        # SLEEP
        # ----------------------------------

        layout.add_widget(
            Label(text="😴 Hours of sleep")
        )

        self.sleep = TextInput(
            hint_text="Example: 7",
            multiline=False,
            input_filter="float",
            size_hint_y=None,
            height=50
        )

        layout.add_widget(self.sleep)


        # ----------------------------------
        # PREDICT BUTTON
        # ----------------------------------

        button = Button(
            text="🎯 PREDICT EXAM SCORE",
            font_size=18,
            size_hint_y=None,
            height=65
        )

        button.bind(
            on_press=self.predict_score
        )

        layout.add_widget(button)


        # ----------------------------------
        # RESULT
        # ----------------------------------

        self.result = Label(
            text="Predicted Score: --",
            font_size=22,
            size_hint_y=None,
            height=60
        )

        layout.add_widget(self.result)


        # ----------------------------------
        # STATUS
        # ----------------------------------

        status = Label(
            text="✓ AI model trained successfully",
            font_size=14
        )

        layout.add_widget(status)

        return layout


    # ======================================
    # PREDICT SCORE
    # ======================================

    def predict_score(self, instance):

        try:

            hours = float(
                self.hours.text
            )

            assignments = float(
                self.assignments.text
            )

            attendance = float(
                self.attendance.text
            )

            previous = float(
                self.previous.text
            )

            sleep = float(
                self.sleep.text
            )


            # ------------------------------
            # VALIDATION
            # ------------------------------

            if hours < 0:
                self.result.text = "Hours cannot be negative."
                return

            if assignments < 0:
                self.result.text = "Assignments cannot be negative."
                return

            if attendance < 0 or attendance > 100:
                self.result.text = "Attendance must be 0-100%."
                return

            if previous < 0 or previous > 100:
                self.result.text = "Previous score must be 0-100%."
                return

            if sleep < 0:
                self.result.text = "Sleep hours cannot be negative."
                return


            # ------------------------------
            # SEND DATA TO AI
            # ------------------------------

            student_data = [[
                hours,
                assignments,
                attendance,
                previous,
                sleep
            ]]


            prediction = model.predict(
                student_data
            )[0]


            # Keep prediction between 0 and 100
            prediction = max(
                0,
                min(100, prediction)
            )


            # ------------------------------
            # DISPLAY RESULT
            # ------------------------------

            self.result.text = (
                f"🎯 Predicted Score: "
                f"{prediction:.2f}%"
            )


        except ValueError:

            self.result.text = (
                "⚠️ Please fill in all fields."
            )


# ==========================================
# START APPLICATION
# ==========================================

StudyAIApp().run()
