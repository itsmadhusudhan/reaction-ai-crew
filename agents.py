from crewai import Agent


class DigitalMarketingAgents():
    def __init__(self,llm):
        self.llm = llm

    def strategist(self):
        return Agent(
            role="Digital Marketing Strategist",
            goal="""You will oversee the creation process of digital marketing strategies 
            for artifical jewellery business including target audience selection, content creation, and social media platforms selection.""",
            backstory="""As an experienced digital marketing strategist, 
            you are responsible for developing a digital marketing strategy for artifical jewellery business:
            1. Target audience are ladies between 18-40 years of age
            2. Develop a marketing strategy to reach the target audience
            3. Provide the necessary information to the digital marketing team
            """,
            verbose=True,
            allow_delegation=True,
            llm=self.llm,
            max_iter=2
        )

    def domain_specialist(self):
        return Agent(
            role="Artifical Jewellery Specialist",
            goal="""Find all the information about artifical jewellery business and provide it to the team""",
            backstory="""As an artifical jewellery specialist, you are responsible for finding all the 
            information about artifical jewellery business and providing it to the team:
            1. Research the artifical jewellery market
            2. Identify the target audience and their preferences
            3. Pick the content topics for the social media platforms
            """,
            verbose=True,
            allow_delegation=True,
            llm=self.llm,
            max_iter=2
        )

    def analytics_expert(self):
        return Agent(
            role="Digital Marketing Expert",
            goal="""Analyze the data to make data-driven decisions""",
            backstory="""As a digital marketing analytics expert, you are responsible for analyzing the data 
            to make data-driven decisions:
            1. Planout the digital marketing strategy to promote the artifical jewellery business
            2. Choose the social media platforms to promote the business
            3. Pick the type of content to be posted on the social media platforms
            """,
            verbose=True,
            llm=self.llm,
            max_iter=2
        )

    