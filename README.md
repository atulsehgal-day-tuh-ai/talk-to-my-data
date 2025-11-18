```markdown
# Talk to My Data

## Project Overview
"Talk to My Data" is an LLM-driven framework designed for seamless interaction with Snowflake. By leveraging a language model, users can query their data repository, generate SQL queries dynamically, and gain insights from their Snowflake database while simplifying the data interaction process. The system enhances data accessibility and usability through natural language processing, making it easier for users to extract relevant information from large datasets.

## Features
- **Natural Language Queries**: Users can input queries in plain English, which the LLM translates into SQL.
- **Snowflake Integration**: Direct interaction with Snowflake using a dedicated connector for executing queries.
- **Dynamic SQL Generation**: Automatically generates and executes SQL code based on user queries.
- **Configurable Parameters**: Environment-driven settings allow easy adjustments without modifying code directly.
- **Automation Scripts**: Includes PowerShell scripts for local development and testing workflows.

## Architecture Summary
- **`src/main_app.py`**: The main entry point of the application, responsible for coordinating interactions between user inputs and processing.
- **`src/db_connector.py`**: Contains the logic required to connect to Snowflake, execute queries, and handle data fetching.
- **`src/llm_agent.py`**: Implements the logic for the LLM interface, serving as the primary agent for handling queries and generating SQL commands.
- **`utils/`**: Provides helper functions, configuration loading utilities, and tree structure generation for enhancing app functionality.
- **`configs/settings.yml`**: Mapping configuration file for various application settings.
- **`configs/dev.env`**: A file storing environment variables for local development.
- **`scripts/*.ps1`**: PowerShell scripts used for simplifying common operations and enhancing local workflow automation.
- **`.github/workflows`**: Contains configurations for automatically generating README and managing CI/CD processes.

## Folder Structure Explanation
- **`configs/`**: Holds configuration files like `settings.yaml` for application-wide settings and `dev.env` for environment variables.
- **`sandbox/`**: Temporary space for experimentation, including trial scripts and exploratory testing. Not intended for definitive tests.
- **`scripts/`**: Contains automation scripts, particularly PowerShell scripts for executing local commands and setup processes.
- **`src/`**: The core directory housing main application logic, including file definitions for the LLM agent and database interactions.
- **`utils/`**: Implements utility scripts for common tasks like configuration loading, helper functions, and generating tree structures.
- **`requirements.txt`**: Lists the required Python packages and versions for the application environment.
- **`bundle.yaml`**: Configuration file presumably used to manage service bundles or dependencies.
- **`.github/workflows/`**: Automates workflows related to development, including README generation and continuous integration.

## Setup Instructions
1. **Python Version Requirement**: Ensure Python 3.8 or higher is installed on your system.
2. **Creating Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Installing Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Setting Up `dev.env`**: 
   - Navigate to `configs/` and create a file named `dev.env`.
   - Populate it with the necessary environment variables:
   ```env
   SNOWFLAKE_ACCOUNT=your_account
   SNOWFLAKE_USER=your_user
   SNOWFLAKE_PASSWORD=your_password
   SNOWFLAKE_ROLE=your_role
   SNOWFLAKE_DATABASE=your_db
   SNOWFLAKE_SCHEMA=public
   SNOWFLAKE_WAREHOUSE=your_wh
   OPENAI_API_KEY=your_api_key
   ```

5. **Verifying Snowflake Connectivity**: Run a test script to check the connection with Snowflake, available in the `sandbox/` directory.

## Running the Application
- To run the application via Python:
   ```bash
   python src/main_app.py
   ```
- Alternatively, use PowerShell to execute:
   ```powershell
   .\scripts\run_local.ps1
   ```
- Environment variables from `dev.env` are loaded automatically when the application starts.

## Description of `configs/`
- **`settings.yaml`**: Contains key-value pairs for different configurable settings within the application.
- **`dev.env` Variables**:
  - `SNOWFLAKE_ACCOUNT`: Your Snowflake account identifier.
  - `SNOWFLAKE_USER`: Username for Snowflake access.
  - `SNOWFLAKE_PASSWORD`: Password linked with the Snowflake user.
  - `SNOWFLAKE_ROLE`: Role that dictates permissions within Snowflake.
  - `SNOWFLAKE_DATABASE`: The specific database to be queried within Snowflake.
  - `SNOWFLAKE_SCHEMA`: Default schema used for queries, typically set to `public`.
  - `SNOWFLAKE_WAREHOUSE`: The Snowflake warehouse for executing queries.
  - `OPENAI_API_KEY`: Your API key for accessing OpenAI's services.

## Description of `utils/`
- **`config_loader.py`**: Loads configuration settings from YAML and environment files, ensuring application parameters are correctly set.
- **`generate_tree.py`**: Provides functions for generating tree structures or hierarchical representations of data, facilitating better visualization.
- **`helper.py`**: Contains miscellaneous helper functions to support various application functionalities, including error handling and data conversion.

## Description of `sandbox/`
The `sandbox/` directory serves as an experimental environment for developers. It is not a formal testing suite but a space to run trial scripts and develop new functionalities without impacting the core application. Feel free to experiment with Snowflake queries, LLM interactions, and other functionalities safely here.

## Example Usage
### Snowflake Query Example
Using the LLM agent, you might input a natural language query such as:
- "Show me the total sales last quarter."
The LLM translates this to:
```sql
SELECT SUM(sales) FROM sales_data WHERE sale_date >= '2023-01-01' AND sale_date < '2023-04-01';
```

### CLI Example
To initiate a query via command line, you can execute:
```bash
python src/main_app.py "What were the top-selling products?"
```

### Simple Workflow Example
1. Activate your virtual environment.
2. Ensure the necessary configurations are set in `dev.env`.
3. Run `src/main_app.py`.
4. Enter your natural language query when prompted.

## Contribution Guidelines
- **Branching Strategy**: Develop features in their own branches named after the feature (e.g., `feature/query-optimization`).
- **PR Expectations**: Ensure all code is tested, and relevant documentation is updated before submitting a pull request.
- **Naming Conventions**: Use `snake_case` for variable and function names. Class names should use `CamelCase`.
- **Adding New Modules**: Ensure to document new modules thoroughly and consider updating the README if necessary to reflect new functionalities.

## License Section
This project is licensed under the MIT License. See the `LICENSE` file for more details.
```
