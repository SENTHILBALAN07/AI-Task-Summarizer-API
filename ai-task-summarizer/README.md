# AI Task Summarizer API

## Problem Understanding & Assumptions
The service connects a PostgreSQL database with an external public API to enrich stored task data.
Assumptions:
- No authentication required
- External API may occasionally fail
- Single-user system

## Design Decisions
- Clean layered architecture
- SQLAlchemy ORM
- Dependency Injection for DB sessions
- Async external API calls

## Solution Approach
1. Client sends request
2. Request validated with Pydantic
3. External API generates summary
4. Data persisted in PostgreSQL
5. Response returned

## Error Handling Strategy
- 404 for missing resources
- 422 for validation errors
- External API failures handled via timeouts

## How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
