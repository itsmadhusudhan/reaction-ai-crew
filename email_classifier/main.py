from langchain_community.llms.ollama import Ollama
from crewai import Agent,Task,Crew,Process


# get the model
mistral = Ollama(model="mistral")

# create input
email = """ I am writing to you to express my interest in the position of Software Engineer at your company. 
I am a recent graduate from the University of California, 
Berkeley with a Bachelor of Science in Electrical Engineering and Computer Sciences. 
I have a strong foundation in software engineering and programming, 
and I am excited about the opportunity to work with your team to develop innovative software solutions.
I am confident that my skills and experience make me a strong candidate for this position.
I have attached my resume for your review, and I look forward to the opportunity to discuss my application with you further.
Thank you for considering my application. 
Sincerely, Someone"""

email2="""Dear Sir/Madam, I am writing to inform you that you have won a prize of $1,000,000.
Please click on the link below to claim your prize.
https://www.notascam.com/claimprize
Congratulations!"""


email3="""Hey, I hope you are doing well. I just wanted to check in and see how you are doing.
Let me know if you need anything. Take care!"""

# create agents
classifier = Agent(
    role="email classifier",
    goal="""accurately classify emails based on their importance. 
    Give every email one of the following labels: 'important', 'casual', 'spam',
    """,
    backstory="""You are an AI assistant whose only job is to classify emails accurately and honestly.
    Do not be afraid to classify an email as spam if it is spam. You job is to help users manage their emails effectively.
    """,
    verbose=True,
    allow_delegation=False,
    llm=mistral
)

responder = Agent(
    role="email responder",
    goal="""Based on the imporatance of the emails, write a concise and simple response to each email.
    If the email is 'important' write a formal response, if the email is 'casual' write a casual response. and if the email is 'spam', 
    do not respond. no matter what be very concise.""",
    backstory="""You are an AI assistant whose only job is to write short responses to emails based on their importance.
    The importance will be provided to you by the email 'classifier' agent.
    """,
    verbose=True,
    allow_delegation=False,
    llm=mistral
)

# Create tasks

classify_task=Task(
    description=f"classify both the emails '{email}', '{email2} and '{email3}'",
    agent=classifier,
    expected_output="One of those options : 'important', 'casual', 'spam'",
)

respond_task=Task(
    description=f"Respond to both the emails '{email}', '{email2} and '{email3}' based on the importance provided ny the 'classifier' agent.",
    agent=responder,
    expected_output="A very concise response to each email based on the importance provided by the 'classifier' agent."
)

# create crew
crew = Crew(
    tasks=[classify_task,respond_task],
    agents=[classifier,responder],
    verbose=2,
    process=Process.sequential
)


output= crew.kickoff()

print(output)