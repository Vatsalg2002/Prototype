# Weather Condition Recommendation Project

## Overview

This project aims to provide weather-related recommendations based on the user's current live location. The application fetches the user's location, retrieves weather data, and processes it to generate user-friendly recommendations. The project uses several agents working sequentially to load, summarize, and analyze weather and pollution data, ultimately providing actionable recommendations.

## Project Structure

```
.
├── utils.py
├── index.py
├── agents.py
├── .env
├── weather_data.json
├── requirements.txt
└── README.md
```

### File Descriptions

- **utils.py**: Contains utility functions, including a tool to load weather data from a JSON file.
- **index.py**: Contains functions to fetch the user's location and retrieve weather data from an external API.
- **agents.py**: Defines various agents and tasks using the CrewAI framework to process the weather data and provide recommendations. This script initiates the entire process.
- **.env**: Environment file that stores API keys and other sensitive information.
- **weather_data.json**: JSON file generated after running the project, storing the user's live location weather conditions fetched from the API.
- **requirements.txt**: File that lists all the dependencies needed for the project.
- **README.md**: Documentation file that provides an overview of the project and instructions for running it.

## Instructions to Run the Project

### Prerequisites

1. **Python 3.8+**: Ensure you have Python installed.
2. **pip**: Ensure you have pip installed for package management.
3. **Environment Variables**: modify the `.env` file in the project root directory with the following content:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    SERPER_API_KEY=your_serper_api_key_here
    ```

### Install Dependencies

Install the required packages by running:

```bash
pip install -r requirements.txt
```

### Generate Recommendations

To fetch the user's current location, retrieve weather data, and generate recommendations, run:

```bash
python agents.py
```

This script performs the following steps:
1. Fetches the user's location based on their IP address.
2. Calls an external API to get the current weather conditions for the retrieved location.
3. Saves the weather data to a JSON file (`weather_data.json`).
4. Loads the weather data from the JSON file.
5. Uses the CrewAI framework to process the data through various agents:
    - **Weather Data Loader**: Loads weather data.
    - **Data Summarizer**: Summarizes the weather data in a human-readable format.
    - **Pollution Expert**: Analyzes pollution data based on AQI.
    - **Environmentalist**: Provides information on environmental conditions and improvement actions.
    - **Recommendation Writer**: Generates recommendations based on summarized data.
6. Prints the final recommendations to the console.

### Example Output

The output will include detailed information about the current weather conditions, pollution levels, and environmental factors, along with recommendations for actions to take based on these conditions.

## Environment Variables

Ensure you have the following API keys stored in the `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `SERPER_API_KEY`: Your Serper API key.

## Conclusion

This project provides a comprehensive solution for generating weather-related recommendations based on real-time data. By following the instructions above, you can run the project and obtain useful insights and recommendations for the current weather conditions in your location.
