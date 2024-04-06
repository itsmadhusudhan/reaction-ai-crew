from crewai_tools import BaseTool
from pydantic.v1 import BaseModel, Field
from typing import List
from langchain.agents import Tool

class Syllabus(BaseModel):
    name: str
    subTopics: List[str]

class ChemistrySyllabusTool(BaseTool):
    name: str = "Chemistry Syllabus Tool"
    description: str = "Tool to provide the Chemistry syllabus for reference"
    
    def _run(self) -> List[dict]:
        file= open("syllabus.json", "r")
        syllabus = json.load(file)
        result = map(lambda x: x, syllabus)
        return list(result)


class ChemistryQuestionsTool(BaseTool):
    name: str = "Chemistry Questions Tool"
    description:str = "Tool to provide the Chemistry questions for reference"
    
    def _run(self) -> List[dict]:
        file= open("questions.json", "r")
        questions = json.load(file)
        result = map(lambda x: x, questions)
        return list(result)


def syllabus_search() -> List[Syllabus]:
    file= open("syllabus.json", "r")
    syllabus = json.load(file)
    result = map(lambda x: Syllabus(**x), syllabus)
    return list(result)

syllabus_tool = Tool(
    name="Chemistry Syllabus Tool",
    func=syllabus_search,
    description="Tool to provide the Chemistry syllabus for reference",
)


def all_previous_year_questions() -> List[dict]:
    file= open("questions.json", "r")
    questions = json.load(file)
    result = map(lambda x: x, questions)
    return list(result)


questions_tool = Tool(
    name="Chemistry Questions Tool",
    func=all_previous_year_questions,
    description="Tool to provide the Chemistry questions for reference",
)