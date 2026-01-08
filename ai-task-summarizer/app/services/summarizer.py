import httpx
from app.core.config import settings

async def generate_summary(text: str) -> str:
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(settings.SUMMARY_API_URL)
            response.raise_for_status()
            data = response.json()
            return data.get("content", "Auto-generated summary")
    except Exception:
        return "Summary unavailable due to external service issue."
