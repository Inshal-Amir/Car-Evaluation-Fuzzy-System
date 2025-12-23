# Car Evaluation Fuzzy System

This project implements a fuzzy logic based car evaluation system using a Mamdani Fuzzy Inference System, along with a baseline crisp model and a web-based dashboard for visualization and interaction.

---

## Repository Link

Clone the project from GitHub using the following commands:

```bash
git clone https://github.com/Inshal-Amir/Car-Evaluation-Fuzzy-System.git
cd Car-Evaluation-Fuzzy-System
````

---

## Project Structure

* backend/
  Contains all Python code including fuzzy logic modules, experiments, tests, API services, and report generation scripts.

* dashboard/
  React-based web interface used to interact with the fuzzy system through API calls.

* venv/
  A pre-generated Python virtual environment is included in the repository and is placed in the root directory. Users should try to activate this first before creating a new one.

---

## Virtual Environment Setup (Important)

Since the repository already includes a `venv/` folder, the first step is to try activating it.

### Step 1: Activate the existing venv (recommended first attempt)

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
.\venv\Scripts\activate
```

---

### Step 2: Verify the venv is actually active (must do)

After activation, run this command to check which `pip` is being used:

#### macOS / Linux

```bash
which pip
```

#### Windows (PowerShell)

```powershell
where pip
```

✅ If the output path points inside your project folder (for example it contains `Car-Evaluation-Fuzzy-System/venv/`), then the virtual environment is successfully enabled.

❌ If the output path points to a system Python directory or some unrelated location, then the venv did not activate properly and you should create a new one.

You can also verify using:

```bash
python --version
pip --version
```

The displayed `pip` path should contain the project’s `venv` directory.

---

### Step 3: If the existing venv is not working, delete and recreate it

Delete the old `venv/` folder manually (or using commands below).

#### macOS / Linux (optional delete command)

```bash
rm -rf venv
```

#### Windows (PowerShell optional delete command)

```powershell
rmdir /s /q venv
```

Now create a new virtual environment in the root directory:

#### macOS / Linux

```bash
python3.11 -m venv venv
source venv/bin/activate
```

#### Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\activate
```

After recreating, verify again:

* macOS/Linux: `which pip`
* Windows: `where pip`

---

## Backend Setup

After confirming that the virtual environment is active, move to the backend directory:

```bash
cd backend
```

Install required Python dependencies:

```bash
pip install -r requirements.txt
```

---

## Generating Reports

To generate all experiment reports including evaluation metrics, confusion matrices, sensitivity analysis, and ablation study, run the following command while staying in the backend directory:

```bash
python3.11 ./requirements_check.py
```

All generated outputs are saved in:

* backend/reports/

---

## Running Unit Tests

Ensure the virtual environment is enabled, then run this command from the backend directory:

```bash
python3.11 -m pytest
```

This runs unit tests for:

* membership functions
* rule base validation
* inference pipeline correctness

---

## Running Backend API (for Dashboard)

To enable API endpoints for the web dashboard:

1. Ensure the virtual environment is active
2. Ensure dependencies are installed
3. Run the following command from the backend directory:

```bash
python3.11 -m uvicorn api.app:app --reload --port 8000
```

Backend will run at:

```text
http://localhost:8000
```

---

## Running the Dashboard

After starting the backend API, move back to the root directory:

```bash
cd ..
```

Go to the dashboard folder:

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

Open the localhost link shown in the terminal (commonly):

```text
http://localhost:5173
```

---

## Important Notes

* Always ensure the correct virtual environment is active before running backend commands.
* Verify activation using `which pip` (macOS/Linux) or `where pip` (Windows).
* Keep the virtual environment in the root directory to avoid path issues.
* Ensure Node.js and npm are installed before running the dashboard.
* In your IDE, select the interpreter from the project `venv/` directory.

---

## License

This project is developed for academic and educational purposes.