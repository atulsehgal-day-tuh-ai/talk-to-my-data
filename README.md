# Talk to My Data

## Project Overview

Talk to My Data provides an innovative interface for interacting with Snowflake using a large language model (LLM). Users can formulate queries in natural language, which the system interprets, translates into SQL, executes against a Snowflake database, and then returns the results. This project aims to simplify data access and manipulation, making it more intuitive for users.

## Features

- Natural language query processing
- SQL generation from natural language
- Seamless integration with Snowflake
- Result retrieval and display
- Configuration management
- Automation scripts for deployment and management

## Architecture Summary

The architecture of Talk to My Data consists of several components:
- **LLM Agent**: Responsible for interpreting natural language queries and generating corresponding SQL statements.
- **Database Connector**: Facilitates interaction with the Snowflake database.
- **Main Application**: Orchestrates the flow of data between the user inputs, LLM agent, and the database connector.

## Folder Structure Explanation

The repository has the following folder structure:

```
.
├── .gitignore
├── .vscode
├── README.md
├── bundle.yaml
├── configs
├── folder_structure.txt
├── requirements.txt
├── sandbox
├── scripts
└── src
└── utils
```

- **.gitignore**: Specifies files and directories that should be ignored by Git.
- **.vscode**: Contains settings for Visual Studio Code, facilitating an efficient development environment.
- **configs/**: Configuration files for setting application parameters.
- **sandbox/**: Contains scripts and notebooks for testing and experimentation.
- **scripts/**: Automation scripts for running the application locally.
- **src/**: The source code for the application, including key modules and components.
- **utils/**: Utility functions for configuration loading and helper functions.

## Setup Instructions

To set up the project:

1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Navigate to the project directory:
   ```bash
   cd talk-to-my-data
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the settings in `configs/settings.yaml` with your Snowflake credentials and other necessary details.

## Running the Application

To run the application locally, execute the following command:

```bash
python src/main_app.py
```

Ensure that all configurations are set correctly in the `settings.yaml` file.

## configs/ Explanation

The `configs/` directory contains configuration files as YAML. The main file, `settings.yaml`, stores essential parameters like your Snowflake account credentials, role, database, schema, and API keys required for connecting to external services.

## utils/ Explanation

The `utils/` directory comprises utility scripts that assist with various functionalities:
- **config_loader.py**: Handles loading configurations from the settings file.
- **generate_tree.py**: Contains functions to generate hierarchical data structures for ease of handling.
- **helper.py**: Offers miscellaneous helper functions used throughout the project.

## sandbox/ Explanation

The `sandbox/` directory is designated for scratch experiments and proofs of concept. It includes test scripts and Jupyter notebooks for testing database connections and experimenting with SQL generation and querying logic. This space allows developers to iterate quickly without affecting the main codebase.

## Example Usage

1. Start the application as mentioned in the "Running the Application" section.
2. Input a natural language query, such as:
   ```
   "Show me the sales data for the last quarter."
   ```
3. The application will convert the input into SQL, execute it, and return the results from the Snowflake database.

## Contribution Guidelines

We welcome contributions to improve the project. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and open a pull request.

Make sure to adhere to the project's coding standards and test your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.