"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": ["hxeqlzlzow!", 2], "answer": "hello!"},
        {"input": ["abcdefr", 2], "answer": "acer"},
        {"input": ["dbcoefc", 3], "answer": "doc"},
    ],
    "Extra": [
        {"input": ["spycode", 1], "answer": "spycode"},
        {"input": ["python", 6], "answer": "p"},
        {"input": ["ppy3ppy", 2], "answer": "pypy"},
        {"input": ["HELLOworld", 5], "answer": "Hw"},
        {"input": ["", 3], "answer": ""},
        {"input": ["123456789", 4], "answer": "159"},
        {"input": ["noiseMESSAGE", 2], "answer": "nieESG"}
    ]
}
