from langchain_core.tools import tool


@tool("All Previous year exam mutiple choice questions")
def all_previous_year_questions() -> str:
    """Gives all the previous year exams questions for reference"""
    print("called me")
    # questions = [{
    #     "question": "The correct statement regarding defects in solids is",
    #     "options": ["Frenkel defect is a vacancy defect",
    #                 "Schottky defect is a dislocation defect",
    #                 "Trapping of an electron in the lattices leads to the formation of F-centre",
    #                 "Schottky defect has no effect on density."
    #                 ],
    #     "year": [2021]
    # }]

    file= open("questions.json", "r")
    questions = json.load(file)
    result = map(lambda x: x, questions)
    # return list(result)

    return '\n'.join(str(x) for x in list(result))
