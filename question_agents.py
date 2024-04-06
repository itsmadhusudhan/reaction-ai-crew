from crewai import Agent

from tools.chemistry_tools import all_previous_year_questions


def chemistry_professor(llm):
    return Agent(
        role="Senior Chemistry professor",
        goal="""To prepare questions for karnataka common entrance test chemistry exam. Including a few questions 
        from the previous year exams""",
        backstory="""You are a senior chemistry professor with over 20 years of experience in teaching chemistry.""",
        verbose=True,
        llm=llm,
        allow_delegation=True,
        tools=[all_previous_year_questions],
    )
