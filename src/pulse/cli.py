import typer

from pulse.runner import run_load_test
from pulse.metrics import calculate_metrics
from pulse.output import print_metrics

app = typer.Typer()

@app.command()
def run(url: str, requests: int = 100):
    results = run_load_test(url, requests)
    metrics = calculate_metrics(results)

    print_metrics(url, metrics)

@app.command()
def hello(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    app()
