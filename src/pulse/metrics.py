from dataclasses import dataclass
from statistics import mean

from pulse.models import RequestResult


@dataclass(slots=True)
class Metrics:
    total: int
    successful: int
    failed: int
    min_ms: float
    avg_ms: float
    max_ms: float
    p50_ms: float
    p95_ms: float
    p99_ms: float


def calculate_metrics(results: list[RequestResult]) -> Metrics:
    latencies = sorted(result.latency_ms for result in results)

    successful = sum(result.success for result in results)

    return Metrics(
        total=len(results),
        successful=successful,
        failed=len(results) - successful,
        min_ms=min(latencies),
        avg_ms=mean(latencies),
        max_ms=max(latencies),
        p50_ms=percentile(latencies, 50),
        p95_ms=percentile(latencies, 95),
        p99_ms=percentile(latencies, 99),
    )


def percentile(values: list[float], percentile_value: float) -> float:
    index = (percentile_value / 100) * (len(values) - 1)

    lower = int(index)
    upper = min(lower + 1, len(values) - 1)

    weight = index - lower

    return values[lower] + (values[upper] - values[lower]) * weight
