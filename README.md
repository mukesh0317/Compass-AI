# COMPASS AI
### Smart Competency-Based Assessment and Personalized Learning

**Track:** AI + Education

COMPASS AI is a prototype that demonstrates skill-level competency estimation, learning-gap identification, and targeted practice suggestions from student assessment responses.

## Features
- Interactive competency dashboard
- Simplified Bayesian Knowledge Tracing (BKT) baseline
- Topic-level mastery estimates and observed accuracy
- Practice recommendations based on estimated mastery
- Upload assessment data as CSV
- Export competency profile as CSV

## Demo data format
CSV files must contain these columns:

| student | skill | correct |
|---|---|---|
| Aarav | Algebra | 1 |
| Aarav | Python Basics | 0 |

`correct` must be `1` for correct or `0` for incorrect. The bundled sample data is synthetic and is only for demonstration.

## Run locally
Python 3.10+ is recommended.

```bash
git clone https://github.com/mukesh0317/Compass-AI.git
cd Compass-AI
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install and run:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Technical approach
The prototype uses a simplified BKT-style update to estimate the probability of mastery after a sequence of responses. The model exposes learning, guessing, slip, and prior-mastery parameters so users can explore their effect.

These estimates are illustrative and have not been validated for high-stakes educational decisions. The bundled data is synthetic. Real ASSISTments data integration and formal model evaluation are future work unless separately implemented.

## Roadmap
- Integrate and preprocess an approved ASSISTments dataset
- Evaluate BKT against suitable baselines on held-out data
- Add student and faculty views
- Improve adaptive assessment and learning recommendations
- Deploy a public demo

## Project
ForgeHacks Online 2026 · AI + Education
