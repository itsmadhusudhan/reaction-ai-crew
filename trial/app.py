from crewai import Task, Crew,Process
from langchain_community.llms.ollama import Ollama
from question_agents import chemistry_professor
from dotenv import load_dotenv

from agents import ChemistryAutomationAgents
from trial.tasks import ChemistryAutomationTasks
import os

load_dotenv()

ollama_mistral = Ollama(model="mistral")
os.environ['OPENAI_API_KEY']=""

# def run():
#     professor = chemistry_professor(ollama_mistral)
#     task = Task(
#         description="""Generate 10 multiple choice questions. Take all the 
#         questions from the previous year questions""",
#         verbose=True,
#         agent=professor,
#         expected_output="10 Multiple choice questions in valid JSON format"
#     )

#     crew = Crew(
#         agents=[professor],
#         tasks=[task],
#         verbose=2,
#         manager_llm=ollama_mistral
#     )

#     data = crew.kickoff()

#     with open("questions.json", "w") as f:
#         f.write(data)

#     return data


# if __name__ == "__main__":
#     print("## Welcome to Reaction AI Crew")
#     print('-------------------------------')
#     result = run()
    
#     print("\n\n########################")
#     print("########################\n")
#     # print(result)


# Create agents
agents = ChemistryAutomationAgents(ollama_mistral)

subject_manager = agents.subject_manager()
topic_selector = agents.topic_selector()

# syllabus_research_manager = agents.syllabus_research_manager()
# previous_years_questions_collector = agents.previous_years_questions_collector()
questions_generator = agents.questions_generator()

# # create tasks
tasks = ChemistryAutomationTasks()

manage_subject_task = tasks.manage_subject(subject_manager)
# manage_syllabus_search_task = tasks.manage_syllabus_search(syllabus_research_manager)
# collect_previous_years_questions_task = tasks.collect_previous_years_questions(previous_years_questions_collector)
topic_selection_task=tasks.topic_selection(topic_selector)
generate_questions_task = tasks.generate_questions(questions_generator)


crew = Crew(
    agents=[
        subject_manager,
        topic_selector,
        # syllabus_research_manager,
        # previous_years_questions_collector,
        questions_generator
    ],
    tasks=[
        manage_subject_task,
        topic_selection_task,
        # manage_syllabus_search_task,
        # collect_previous_years_questions_task,
        generate_questions_task
    ],
    verbose=2,
    process=Process.hierarchical,
    manager_llm=ollama_mistral
)

data = crew.kickoff()

print("Crew usage",crew.usage_metrics)

print("Results:")
print(data)


