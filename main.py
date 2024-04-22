from crewai import Task, Crew,Process
from langchain_community.llms.ollama import Ollama
from agents import DigitalMarketingAgents
from tasks import DigitalMarketingTasks
from dotenv import load_dotenv

def main():
    load_dotenv()
    ollama_mistral = Ollama(model="mistral")

    # Create Agents
    agents = DigitalMarketingAgents(ollama_mistral)

    strategist = agents.strategist()
    domain_specialist = agents.domain_specialist()
    analytics_expert = agents.analytics_expert()

    # Create Tasks
    tasks =DigitalMarketingTasks()

    strategise = tasks.strategise(strategist)
    research = tasks.research(domain_specialist)
    analyze = tasks.analyze(analytics_expert)

    # Create Crew
    crew = Crew(
        agents=[strategist,domain_specialist,analytics_expert],
        tasks=[strategise,research,analyze],
        manager_llm=ollama_mistral,
        verbose=2,
        process=Process.hierarchical,
    )

    # kickoff crew
    data = crew.kickoff()

    print("##########\n")
    print("Crew usage",crew.usage_metrics)
    print("##########\n")
    print(data)
    print("##########\n")
    print(strategise.output)
    print("##########\n")
    print(research.output)
    print("##########\n")
    print(analyze.output)


if __name__ == "__main__":
    main()