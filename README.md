````markdown
# Car Evaluation Fuzzy System

This project implements a fuzzy logic based car evaluation system using a Mamdani Fuzzy Inference System, along with a baseline crisp model and a web-based dashboard for visualization and interaction.

---

## Repository Link

Clone the project from GitHub using the following command:

```bash
git clone https://github.com/Inshal-Amir/Car-Evaluation-Fuzzy-System.git
cd Car-Evaluation-Fuzzy-System
````

---

## Project Structure

* `backend/`
  Contains all Python code including fuzzy system, experiments, tests, API, and report generation.

* `dashboard/`
  React-based web interface for interacting with the fuzzy system.

* `venv/`
  Python virtual environment (recommended to create at root level).

---

## Virtual Environment Setup

It is strongly recommended to create the virtual environment in the **root directory** of the project.

### macOS / Linux

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\activate
```

Make sure the virtual environment is set as the Python interpreter in your IDE.

If an existing virtual environment does not work, delete it and create a new one using the steps above.

---

## Backend Setup

After activating the virtual environment, move to the backend directory:

```bash
cd backend
```

Install required Python libraries:

```bash
pip install -r requirements.txt
```

---

## Generating Reports

To generate all experiment reports (metrics, confusion matrix, sensitivity analysis, ablation study), run the following command while staying in the `backend` directory:

```bash
python3.11 ./requirements_check.py
```

All generated reports will be saved inside the `backend/reports` folder.

---

## Running Unit Tests

Ensure the virtual environment is enabled and run:

```bash
python3.11 -m pytest
```

This will execute tests for membership functions, rule base, and inference pipeline.

---

## Running Backend API (for Dashboard)

To enable API endpoints for the web dashboard, run the following command from the `backend` directory:

```bash
python3.11 -m uvicorn api.app:app --reload --port 8000
```

The API will be available at:

```
http://localhost:8000
```

---

## Running the Dashboard

After starting the backend API, move back to the root directory:

```bash
cd ..
```

Then navigate to the dashboard folder:

```bash
cd dashboard
```

Install Node.js dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

Open the provided local host URL (usually `http://localhost:5173`) in your browser to access the web interface.

---

## Notes

* Ensure Node.js and npm are installed before running the dashboard.
* Always activate the virtual environment before running backend commands.
* Keep the virtual environment in the root directory to avoid path issues.

---

## License

This project is intended for academic and educational purposes.

```
```
