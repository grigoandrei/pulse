from dataclasses import dataclass

@dataclass(slots=True)
class RequestResult:
    success: bool
    status_code: int | None
    latency_ms: float
    error: str | None = None
