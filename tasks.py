from crewai import Task
from textwrap import dedent

class DigitalMarketingTasks():
    def strategise(self,agent):
        return Task(
            description=dedent(f"""Oversee the creation of digital marketing strategies for artifical jewellery business"""),
            expected_output=dedent(f"""Guide the team on target audience selection, content creation, and social 
            media platforms selection"""),
            output_file="marketing.json",
            verbose=True,
            agent=agent,
        )

    def research(self,agent):
        return Task(
            description=dedent(f"""Find all the information about artifical jewellery business and provide it to the team"""),
            expected_output=dedent(f"""Research the artifical jewellery market, identify the target audience and 
            their preferences, pick the content topics for the social media platforms"""),
            output_file="research.json",
            verbose=True,
            agent=agent,
        )

    def analyze(self,agent):
        return Task(
            description=dedent(f"""Analyze the data to make data-driven decisions"""),
            expected_output=dedent(f"""Planout the digital marketing strategy to promote the artifical jewellery business, 
            choose the social media platforms to promote the business, pick the type of content to be posted on the 
            social media platforms"""),
            output_file="analytics.json",
            verbose=True,
            agent=agent,
        )