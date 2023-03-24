import typer #here it is used to build this cli tool and rich gives us colorfull texts
from rich.console import Console #typer alos helps for the commanf line interactions
from rich.table import Table
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo
from model import Todo

console = Console () # console object 

app = typer.Typer() # app object from typer library

@app.command(short_help="adds an item") # app.command helps to decorate and short_help parameter provides a brief description of what the command does
def add (task: str, category: str):
    typer.echo(f"adding{task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)

    show()

@app.command()
def delete (position: int):
    typer.echo(f"deleting {position}")
    #herer indices in ui starts at 1, but in the database at 0
    delete_todo(position-1)

    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_todo(position-1, task, category)

    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete{position}")
    complete_todo(position-1)

    show()

@app.command()
def show():
    tasks = get_all_todos()
    console.print("[bold magenta]Todos[/bold magenta]!", "📝")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {"Learn": "cyan", "Youtube": "red", "sports": "cyan", "study":"green"}
        if category in COLORS:
            return COLORS[category]
        return "white"


    for index, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 2 else '❌'
        table.add_row(str(index), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()