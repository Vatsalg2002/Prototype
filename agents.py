"""
This script sets up and runs a series of collaborative agents using CrewAI for real-time air quality monitoring and prediction.

Key functionalities include:
1. Loading weather data from a JSON file.
2. Summarizing weather data in a human-readable format.
3. Providing detailed information on pollution based on the Air Quality Index (AQI).
4. Offering insights and actions for improving environmental conditions.
5. Writing recommendations on whether it is safe to go outside based on the summarized data.

The script leverages the following main components:
- Agents: Defined roles for specific tasks including Weather Data Loader, Data Summarizer, Pollution Expert, Environmentalist, and Recommendation Writer.
- Tasks: Specific tasks assigned to each agent, detailing their goals and expected outputs.
- Crew: A collection of agents and tasks, configured to execute in a sequential process.

External Libraries and Tools Used:
- CrewAI: For creating and managing agents and tasks.
- LangChainOpenAI: For utilizing OpenAI's language models.
- SerperDevTool: For additional functionality related to the Serper API.
- dotenv: For loading environment variables.
- utils: Custom utility functions (e.g., load_weather_data).

The script initializes by calling a main function to create the weather data JSON file, sets up environment variables for API keys, defines each agent and their respective tasks, and then kicks off the crew to perform the defined tasks in sequence.

To run the script, ensure all required dependencies are installed and necessary environment variables are set.
"""


import os
from utils import load_weather_data
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from crewai_tools import  SerperDevTool

# Import the main function from index.py
from index import main as create_weather_data_json

# Call the main function to create the weather data JSON file
create_weather_data_json()

#getting the api keys from the environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

weather_data_loader = Agent(
    role="Weather Data Loader",
    goal = "your goal is to load the weather data that is being stored in json format",
    backstory="You are a file loader that will load up the weather data from the json file",
    verbose=True,
    allow_delegation=True,
    tools=[load_weather_data, SerperDevTool()],
    llm=ChatOpenAI(model_name="gpt-4", temperature=0.7),
)

data_summarizer = Agent(
    role="Data Summarizer",
    goal="your goal is to summarize the weather data that is being loaded from the weather data loader agent and you have to summarize it in a simple language that is understandaqble by a normal person who dont even have some weather knowledge aprt from this also return a overview of the weather conditions including aqi(Air quality index)",
    backstory="You are a experienced employeethat summarize the data of weather data that is being loaded from the weather data loader agent in a human readable format in a simple language (json format)",
    verbose=True,
    allow_delegation=True,
    tools=[SerperDevTool()],
    # tool = [],
    llm=ChatOpenAI(model_name="gpt-4", temperature=0.7),
)

pollution_expert = Agent(
    role="Pollution Expert",
    goal="your goal is to give the information about the pollution in the area based on the aqi(Air Quality Index) you have to tell the current pollution conditions and also the precautions that should be taken by the person to avoid the pollution related diseases",
    backstory="You are a expert that gives best information related on pollution data and give best knowledge about the precautions that should be taken to avoid the pollution related diseases",
    verbose=True,
    allow_delegation=True,
    tools=[SerperDevTool()],
    # tool = [],
    llm=ChatOpenAI(model_name="gpt-4", temperature=0.7),
)

enviromentalist = Agent(
    role="Enviromentalist",
    goal="your goal is to give the information about the enviroment based on the aqi(Air Quality Index) and as a human being what can we do to improve the enviroment/pollution conditions in the area",
    backstory="You are a expert that gives best information related on enviroment data",
    verbose=True,
    allow_delegation=True,
    tools=[SerperDevTool()],
    # tool = [],
    llm=ChatOpenAI(model_name="gpt-4", temperature=0.7),
)

recommendation_writer = Agent(
    role="Recommendation Writer",
    goal="your goal is to write the recommendations based on the summarized data done by data summarizer agent and you have to write the recommendations reagrding whether the person should go outside the home , if yes then what precaustions should be taken and if no then what are the reasons for not going outside the home",
    backstory="You are a expert that gives best recommendation related on weather data",
    verbose=True,
    allow_delegation=True,
    tools=[SerperDevTool()],
    # tool = [],
    llm=ChatOpenAI(model_name="gpt-4", temperature=0.7),
)


weather_data_loader_task = Task(
    description="Load the weather data from the json file",
    agent=weather_data_loader,
    expected_output="The weather data should be loaded from the json file and returned in json format",
)

data_summarizer_task = Task(
    description="Summarize the weather data in concise json format and return ",
    agent=data_summarizer,
    expected_output="""
    The weather data should be summarized in a human-readable format
    expected output json format
    {
        {
            "weather_overview": {
                "current_conditions": {
                    "Description of current weather conditions",
                    ...
                    }
        }
    }
    """,
)

pollution_expert_task = Task(
    description="Give the information about the pollution in the area based on the aqi(Air Quality Index)",
    agent=pollution_expert,
    expected_output="""
    The pollution over view should be given based on the aqi(Air Quality Index) with current pollution conditions discussing its hazardnous and possible reasons fot it and also the precautions that should be taken by the person to avoid the pollution related diseases
    expected output
    {
        {
            "pollution_overview": {
        "current_conditions": {
            "Description of current pollution conditions",
            ...
            }
        "hazardous_effects": {
            "Explanation of hazardous effects of current pollution levels",
            ...
            }
        "possible_reasons": {
            "Discussion of possible reasons for current pollution levels",
            ...
            }
        "precautions": {
            "Precautions to be taken to avoid pollution-related diseases",
            ...
        }
        },
        "health_recommendations": {
        ...
        ,}

    }
    """
)
enviromentalist_task = Task(
    description="Give the information about the enviroment based on the aqi(Air Quality Index) and as a human being what can we do to improve the enviroment/pollution conditions in the area",
    agent=enviromentalist,
    expected_output=
    """
        The enviroment over view should be given based on the aqi(Air Quality Index) and as a human being what can we do to improve the enviroment/pollution conditions in the area
        expected output
        {
            "environment_overview": {
                ...
            },
            "improvement_actions": {
                "description": "Actions that can be taken by individuals to improve environment/pollution conditions"
            }
        }

    """
)


recommendation_writer_task = Task(
    description="Write the recommendations based on the summarized data, write recommendations for whether the person should go outside the home or not, and if yes then what precautions should be taken and if no then what are the reasons for not going outside the home in json format",
    agent=recommendation_writer,
    expected_output="""
    The recommendations should be written based on the summarized data with recommendations for going outside the house if yes mention the precautions, if not then tell the reason in json format
    expected json format
    {
        "weather_overview": {
            "current_conditions": {
                "description": "Description of current weather conditions",
                "temperature": "Temperature details",
                ....
            }
        },
        "pollution_overview": {
            "current_conditions": {
                "description": "Description of current pollution conditions",
                "aqi": "Current AQI value",
                ...
            },
            "hazardous_effects": {
                "description": "Explanation of hazardous effects of current pollution levels"
                ...
            },
            "possible_reasons": {
                "description": "Discussion of possible reasons for current pollution levels"
                ...
            },
            "precautions": {
                "description": "Precautions to be taken to avoid pollution-related diseases"
                ...
            }
        },
        "environment_overview": {
            ...
        },
        "improvement_actions": {
                "description": "Actions that can be taken by individuals to improve environment/pollution conditions"
        }
    }

    """,    
)


crew = Crew(
    agents=[weather_data_loader, data_summarizer, pollution_expert, enviromentalist  ,recommendation_writer],
    tasks=[weather_data_loader_task, data_summarizer_task, pollution_expert_task, enviromentalist_task , recommendation_writer_task],
    # llm=Ollama_openhermes,
    version=2,
    process=Process.sequential,
)

# kickoff the crew

result = crew.kickoff()
print(result)
