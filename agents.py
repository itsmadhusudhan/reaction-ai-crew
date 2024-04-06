from crewai import Agent

from ai_tools import ChemistrySyllabusTool,ChemistryQuestionsTool,syllabus_tool,questions_tool
from tools.chemistry_tools import all_previous_year_questions

class ChemistryAutomationAgents():
    def __init__(self,llm):
        self.llm = llm

    def subject_manager(self):
        return Agent(
            role="Chemistry Subject Manager",
            goal="""Oversee the Chemistry mutiple choice questions generation process including
            generating new questions""",
            backstory="""As a methodical and detail oriented manager, you are responsible for overseeing the Chemistry multiple choice 
            questions. When creating the questions:
            1. Pick the topics randomly if necessary
            2. Generate new questions
            3. Ensure that the questions are accurate and error-free
            """,
            verbose=True,
            allow_delegation=True,
            llm=self.llm
        )

    def syllabus_research_manager(self):
        return Agent(
            role="Chemistry Syllabus Research Manager",
            goal="""Analyse the Chemistry syllabus to identify the key topics and concepts that should be covered in the multiple 
            choice questions""",
            backstory="""As a diligent and thorough researcher, you are responsible for analysing the Chemistry syllabus to identify 
            the key topics and concepts that should be covered in the multiple choice questions:
            1. Read and understand the Chemistry syllabus
            2. Identify the key topics and concepts that should be covered in the questions
            3. Provide the Chemistry Questions Generator with the necessary information to generate the questions
            """,
            verbose=True,
            allow_delegation=True,
            tools=[syllabus_tool],
            llm=self.llm
        )

    def previous_years_questions_collector(self):
        return Agent(
            role="Chemistry Previous Years Questions Collector",
            goal="""Collect the previous years Chemistry multiple choice questions to provide the Chemistry Questions Generator with 
            the necessary information to generate new questions""",
            backstory="""As a meticulous and detail-oriented collector, you are responsible for collecting the previous years Chemistry 
            multiple choice questions to provide the Chemistry Questions Generator with the necessary information to generate new questions:
            1. Collect the previous years questions skip to generation if not found
            2. Organise the questions based on the topics and concepts covered
            3. Provide the Chemistry Questions Generator with the necessary information to generate the questions
            """,
            verbose=True,
            allow_delegation=True,
            tools=[all_previous_year_questions],
            llm=self.llm
        )

    def questions_generator(self):
        return Agent(
            role="Chemistry Questions Generator",
            goal="""Generate new multiple choice questions based on the Chemistry syllabus. The agent should be able to generate questions""",
            backstory="""As a creative and analytical questions generator, you are responsible for generating new multiple choice
            questions:
            1. Generate new questions
            2. Ensure that the questions are accurate and error-free
            """,
            verbose=True,
            allow_delegation=True,
            llm=self.llm
        )

