import typer #here it is used to build this cli tool and rich gives us colorfull texts
from rich.console import Console #typer alos helps for the commanf line interactions
from rich.table import Table

Console = Console () # console object 

app = typer.Typer() # app object from typer library

@app.command(short_help="adds an item") # app.command helps to decorate and short_help parameter provides a brief description of what the command does
def add (task: str, category: str):
    typer.echo(f"adding{task}, {category}")

@app.command()
def delete (position: int):
    typer.echo(f"deleting {position}")

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")

if __name__ == "__main__":
    app()