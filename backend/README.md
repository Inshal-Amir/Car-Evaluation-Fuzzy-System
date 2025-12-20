# Car Evaluation Fuzzy Logic Backend (KRR Project)

## Setup
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
```

## Get dataset
Place `car.data` inside `backend/data/raw/` (UCI Car Evaluation dataset).

Expected columns (7):
buying,maint,doors,persons,lug_boot,safety,class

## Run requirement proof script
```bash
python requirements_check.py
```
Outputs:
- `reports/metrics.json`
- `reports/confusion_matrix.csv`
- `reports/membership_*.png`
- `reports/baseline_vs_fuzzy.png`

## Run API for React dashboard
```bash
uvicorn api.app:app --reload --port 8000
```

Endpoints:
- GET `/health`
- GET `/metrics`
- GET `/membership`
- POST `/predict`

Example predict:
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"buying":"low","maint":"med","doors":"4","persons":"more","lug_boot":"big","safety":"high"}'
```
