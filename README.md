# Talk to My Data

## Project Overview
Talk to My Data is an innovative project that provides a user-friendly interface powered by a Large Language Model (LLM) for seamless interaction with Snowflake, a popular cloud data platform. Users can issue natural language queries, and the system translates these into SQL queries, executes them against Snowflake, and delivers the results back to the user. This project offers utilities, configuration management tools, automation scripts, and facilitates easy connectivity with Snowflake, enhancing the querying experience for data analysts and developers.

## Features
- Natural language processing to convert user queries into SQL
- Direct communication with the Snowflake database
- Easy-to-use configuration management
- Automation scripts for efficient operation
- Utilities for handling various tasks related to data interaction

## Architecture Summary
The architecture of Talk to My Data is centered around a modular design that separates concerns for better maintainability. The system primarily consists of:
- A database connector (`db_connector.py`) for interfacing with Snowflake
- An LLM agent (`llm_agent.py`) for processing natural language queries
- The main application logic (`main_app.py`) that orchestrates the overall process

## Folder Structure Explanation
The repository is organized as follows:

- `.gitignore`: Specifies files and folders ignored by Git.
- `.vscode`: Contains configuration files for Visual Studio Code.
- `README.md`: This README file.
- `bundle.yaml`: A configuration file for various deployment settings.
- `configs/`: Contains configuration files for application settings.
- `folder_structure.txt`: Documentation of the folder structure.
- `requirements.txt`: Lists the dependencies required for the project.
- `sandbox/`: A directory for experimentation and testing scripts.
- `scripts/`: Automation scripts for local and deployment tasks.
- `src/`: The main source code for the application.
- `utils/`: Utility functions and helper scripts.

## Setup Instructions
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/talk-to-my-data.git
   cd talk-to-my-data
   ```

2. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure connection properties by populating the `settings.yaml` file in the `configs/` directory with your Snowflake and OpenAI credentials.

## Running the Application
To run the application, execute the following command in the root of the project:
```bash
python src/main_app.py
```
Follow the prompts to interact with the application through natural language queries.

## configs/ Explanation
The `configs/` directory contains configuration files, primarily `settings.yaml`, where users specify their Snowflake connection configurations, including account details, credentials, and OpenAI API keys. This file centralizes connection management for easier access and modification.

## utils/ Explanation
The `utils/` directory provides utility scripts that facilitate various support functions:
- `config_loader.py`: Loads and manages configuration settings.
- `generate_tree.py`: Assists in generating hierarchical representations of data or SQL structures.
- `helper.py`: Contains miscellaneous helper functions used throughout the application.

## sandbox/ Explanation
The `sandbox/` directory is intended for scratch experiments and testing. It includes various scripts and notebooks for trial and exploration, such as:
- `test_connection.py`: Tests the connection to the Snowflake database.
- `test_langchain.py`: Experiments with language model integrations.
- Various other test scripts to validate functionality without affecting the main application.

## Example Usage
Once the application is running, you can type in natural language queries such as:
- "Show me the sales data for the last quarter."
- "What are the top 5 products in terms of revenue?"

The system will translate your query into SQL, execute it, and return the relevant results.

## Contribution Guidelines
Contributions to Talk to My Data are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature/YourFeature`).
5. Open a pull request detailing your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.