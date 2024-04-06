from crewai import Task
from textwrap import dedent


class ChemistryAutomationTasks():
    def manage_subject(self, agent):
        return Task(
            description=dedent(f"""Oversee the Chemistry mutiple choice questions generation 
            process.
            Here is the sample json format for the questions:
            [
                {{
                    "question": "What is the capital of France?",
                    "options": ["Paris", "London", "Berlin", "Madrid"],
                    "answer": "Paris",
                    "explanation": "Paris is the capital of France.",
                    "topic": "Geography"
                }},
                {{
                    "question": "What is the capital of Spain?",
                    "options": ["Paris", "London", "Berlin", "Madrid"],
                    "answer": "Madrid",
                    "explanation": "Madrid is the capital of Spain.",
                    "topic": "Geography"
                }}
            ]
            """),
            output_file="output.json",
            verbose=True,
            agent=agent,
            expected_output=dedent(f"""Generate 10 multiple choice questions that are a valid JSON format and ensure that the 
            questions are accurate and error-free.""")
        )

    def manage_syllabus_search(self, agent):
        return Task(
            description=dedent(f"""Analyse the Chemistry syllabus to identify the key topics and concepts that should be covered 
            in the multiple choice questions"""),
            verbose=True,
            agent=agent,
            expected_output=dedent(f"""Provide the Chemistry Questions Generator with the necessary information to generate the questions""")
        )

    def collect_previous_years_questions(self,agent):
        return Task(
            description=dedent(f"""Collect the previous years Chemistry multiple choice questions to provide the Chemistry Questions 
            Generator with the necessary information to generate new questions"""),
            verbose=True,
            agent=agent,
            expected_output=dedent(f"""Provide the Chemistry Questions Generator with the necessary information to generate the questions""")
        )

    def generate_questions(self,agent):
        return Task(
            description=dedent(f"""Generate new multiple choice questions."""),
            verbose=True,
            agent=agent,
            expected_output=dedent(f"""Generate 10 multiple choice questions that are a valid JSON format.""")
        )

