from pulse.metrics import Metrics


def print_metrics(url: str, metrics: Metrics) -> None:
    print("\nPulse Load Test")
    print("────────────────────────────")
    print(f"Target:       {url}")
    print(f"Requests:     {metrics.total}")
    print(f"Successful:   {metrics.successful}")
    print(f"Failed:       {metrics.failed}")

    print("\nLatency:")
    print(f"  Min:        {metrics.min_ms:8.2f} ms")
    print(f"  Avg:        {metrics.avg_ms:8.2f} ms")
    print(f"  Max:        {metrics.max_ms:8.2f} ms")
    print(f"  P50:        {metrics.p50_ms:8.2f} ms")
    print(f"  P95:        {metrics.p95_ms:8.2f} ms")
    print(f"  P99:        {metrics.p99_ms:8.2f} ms")

    print("────────────────────────────")
