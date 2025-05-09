# QA Automated Tests 
## Automated Testing using Selenium and Docker

### Prerequisites:

Ensure you have the following prerequisites installed on your system:

- Python latest version
- Docker

### Setting Up and Running Automated Selenium Tests:

**1. Create a Virtual Environment:**

Use Python 3.7.9 to create a virtual environment. Open your terminal and execute:
```
python3.7 -m venv myenv
```

Replace `myenv` with the desired name for your virtual environment.

**2. Activate the Virtual Environment:**

Activate the virtual environment. This ensures that your project's dependencies won't conflict with the system's. Execute:

```
source myenv/bin/activate  # On Linux or macOS
myenv\Scripts\activate     # On Windows
```

**3. Clone the GitHub Repository**

**4. Install Dependencies:**

Navigate to the project's root directory where the requirements.txt file is located, and execute:
```
pip install -r requirements.txt
```
This will install all the necessary dependencies.

***5. Run Docker:***

Ensure Docker is installed and running. Then, navigate to the directory containing the docker-compose.yml file and execute:
```
docker-compose up -d
```
This will start the required Docker containers.

***6. Verify Docker Ports:***

Confirm that the required ports specified in your `docker-compose.yml` file are available and do not conflict with other services.

***7. Run Automated Tests:***

Navigate to the test directory in your project and execute:
```
behave --format allure_behave.formatter:AllureFormatter -o ./allure-test/
```
To run the tests in parallel it is with behavex:
```
behavex features/ --parallel-processes n
```
Where n is the number of parallel processes (Ask about the maximum and minimum number of processes supported)
