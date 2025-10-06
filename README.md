# SaaS Product Intelligence Researcher

This project is a web-based application designed to research and identify profitable SaaS (Software as a Service) opportunities. It consists of a backend AI agent that processes data and a frontend UI to display the findings in a clear, visual format.

## Features

This project is a functional prototype that includes:

*   **Backend Agent (Python/Flask):**
    *   A Flask server located in the `agent/` directory.
    *   An API endpoint (`/api/research`) that triggers the research logic.
    *   A `researcher.py` module that simulates data collection and applies four key validation filters:
        1.  **Low Marketing Spend:** Identifies products growing organically.
        2.  **Proven Demand:** Looks for evidence of real revenue.
        3.  **Simple to Maintain:** Favors small teams and simple tech stacks.
        4.  **Profitability:** Checks for claims or evidence of profitability.
    *   The agent's behavior is defined by the instructions in `prompt.md`.

*   **Frontend UI (HTML/CSS/JS):**
    *   A clean user interface located in the `ui/` directory.
    *   A "Start Research" button to initiate the process.
    *   The UI fetches the structured JSON report from the backend and renders it into a human-readable format, including validated opportunities, near misses, and market trends.

*   **Continuous Integration:**
    *   A GitHub Actions workflow defined in `.github/workflows/main.yml` automatically checks that the application can be installed and run correctly, ensuring code quality and stability.

## How to Run Locally

To run this application on your local machine, follow these steps.

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies

Install the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 3. Run the Backend Server

Start the Flask backend server. It will run on `http://127.0.0.1:5001`.

```bash
python agent/main.py
```

Keep this terminal window open.

### 4. Run the Frontend UI

Open a **second terminal window** and start a simple web server to serve the `ui` directory. This will run on `http://localhost:8000`.

```bash
python -m http.server --directory ui 8000
```

### 5. View the Application

Open your web browser and navigate to:

**[http://localhost:8000](http://localhost:8000)**

Click the "Start Research" button to see the application in action.

## Note on Deployment

The GitHub Actions workflow included in this repository is for **Continuous Integration (CI)** purposes. It automatically verifies that the application can be installed and runs without errors after each code change.

This workflow **does not deploy the application to a live, public URL**. To test and use the application, please follow the "How to Run Locally" instructions above.