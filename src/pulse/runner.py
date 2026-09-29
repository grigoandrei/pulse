import time
import httpx

from pulse.models import RequestResult

def execute_request(client: httpx.Client, url: str) -> RequestResult:
    start = time.perf_counter()

    try:
        response = client.get(url)
        latency_ms = (time.perf_counter() - start) * 1000

        return RequestResult(
            success = response.is_success,
            status_code = response.status_code,
            latency_ms = latency_ms,
        )
    except httpx.HTTPError as exc:
        latency_ms = (time.perf_counter() - start) * 1000

        return RequestResult(
            success=False,
            status_code=None,
            latency_ms=latency_ms,
            error=str(exc),
        )

def run_load_test(url: str, requests: int) -> list[RequestResult]:
    results = []

    with httpx.Client() as client:
        for _ in range(requests):
            result = execute_request(client, url)
            results.append(result)

    return results

