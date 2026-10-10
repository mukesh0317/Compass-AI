
# COMPASS AI
### Smart Competency-Based Assessment and Personalized Learning Platform

**Track:** AI + Education

COMPASS AI is an AI-powered educational platform designed to move beyond traditional marks-based assessment. It analyzes student assessment responses to estimate competency at individual skill and topic levels, identify learning gaps, track progress, and support personalized learning recommendations.

## Problem Statement

Traditional education systems primarily evaluate students through marks and grades. However, overall scores do not always reveal which concepts a student has mastered or where additional support is required.

Students often struggle to identify their specific weaknesses, while educators need better insights into individual learning progress.

COMPASS AI addresses this challenge by focusing on **skill-level competency estimation, continuous progress tracking, and personalized learning support**.

## Our Solution

COMPASS AI aims to transform assessment data into actionable learning insights. By analyzing student responses over time, the platform seeks to build evolving competency profiles and guide students toward the topics they need to improve.

## Key Features

- **Competency Estimation:** Estimate student mastery at individual skill and topic levels.
- **Skill-Gap Detection:** Identify concepts that require additional practice.
- **Progress Tracking:** Monitor competency changes across successive assessments.
- **Personalized Learning:** Recommend targeted practice based on identified weaknesses.
- **Competency Analytics:** Present student progress in an understandable dashboard.
- **Adaptive Assessment:** Planned extension to adjust questions based on estimated competency.

## How It Works

1. **Assessment Input:** Collect student responses and associate each question with a relevant skill or topic.
2. **Data Preprocessing:** Clean and organize assessment data for analysis.
3. **Competency Estimation:** Use machine learning techniques to estimate the student's mastery of each skill.
4. **Skill-Gap Identification:** Analyze competency estimates to identify topics that need improvement.
5. **Learning Recommendations:** Suggest targeted practice activities for weaker areas.
6. **Progress Monitoring:** Update competency profiles as additional assessment evidence becomes available.

## AI and Machine Learning Approach

### Bayesian Knowledge Tracing (BKT)

BKT is the proposed baseline model for estimating whether a student has mastered a particular skill based on successive assessment responses. It models the evolution of knowledge over time while accounting for learning, guessing, and mistakes.

### Additional Models

Logistic Regression and XGBoost are candidate approaches for comparison and predictive analysis, depending on the available features and evaluation objectives.

Model performance will be assessed using suitable evaluation metrics and held-out data. Actual results will be documented after implementation and testing.

## Dataset

**ASSISTments Skill Builder 2009–2010 Dataset**

The dataset provides student interaction and assessment-response records that can be used to investigate learning patterns and skill-level knowledge estimation.

Dataset source: [ASSISTments Data](https://sites.google.com/site/assistmentsdata/)

The dataset will be used subject to its applicable access conditions and data-use terms. Data preprocessing and skill mapping are required before model development.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Competency Estimation | Bayesian Knowledge Tracing |
| Candidate ML Models | Logistic Regression, XGBoost |
| Backend | FastAPI |
| Frontend | React |
| Database | PostgreSQL |
| Development Environment | Google Colab, Git, GitHub |

The final technology stack will reflect the components implemented in the working application.

## Proposed Architecture

```text
Student Assessment Responses
            |
            v
     Data Preprocessing
            |
            v
    Competency Estimation
        (BKT Baseline)
            |
            v
     Student Competency
          Profile
            |
            v
      Skill-Gap Detection
            |
            v
   Personalized Practice
      Recommendations
            |
            v
      Progress Dashboard
```

## Getting Started

### Prerequisites

- Python 3.10 or a compatible version
- Git
- A code editor such as Visual Studio Code
- The required dataset, if running the ML pipeline

### Installation

Clone the repository:

```bash
git clone https://github.com/mukesh0317/Compass-AI.git
cd Compass-AI
```

Create and activate a virtual environment:

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies after creating `requirements.txt`:

```bash
pip install -r requirements.txt
```

Follow the project-specific instructions as the ML engine, backend, and frontend are implemented.

## Expected Impact

COMPASS AI aims to:

- Help students understand their individual learning strengths and weaknesses.
- Support earlier identification of knowledge gaps.
- Encourage targeted practice instead of repetitive, generic assessments.
- Give educators clearer insights into student competency development.
- Support a shift from marks-focused evaluation toward continuous, competency-based learning.

## Challenges

Key technical challenges include mapping assessment questions to the correct skills, estimating mastery from repeated responses, distinguishing mistakes from genuine knowledge gaps, and generating meaningful recommendations.

The project addresses these challenges through structured data preprocessing, a knowledge-tracing baseline, model evaluation, and a modular application architecture.

## Future Enhancements

- Adaptive question selection based on competency estimates.
- Student and faculty dashboards.
- Integration with Learning Management Systems (LMS).
- Comparison of knowledge tracing and supervised ML models.
- Personalized learning paths and progress reports.
- Deployment as a web-based educational application.

## Demo and Screenshots

- **Live Demo:** Coming soon
- **Demo Video:** Coming soon
- **Architecture Diagram:** To be added
- **Application Screenshots:** To be added

Links will be updated when the working application and public demo are available.

## Project Information

- **Project:** COMPASS AI
- **Hackathon:** ForgeHacks Online 2026
- **Track:** AI + Education
- **Category:** Educational Technology / Machine Learning

## Vision

**Move beyond marks. Understand mastery. Personalize every student's learning journey.**

COMPASS AI aims to make learning more transparent, personalized, and actionable by helping students understand what they know, what they need to improve, and what they should learn next.
