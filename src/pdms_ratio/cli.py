import typer
from pdms_ratio import calculate_ratio

app = typer.Typer()
app.command()(calculate_ratio)

if __name__ == "__main__":
    app()
