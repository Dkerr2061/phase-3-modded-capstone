import math
import time
from rich.progress import Progress
from rich.console import Console

console = Console()

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '■' * int(percent) + '-' * (100 - int(percent))
    console.print(f"\r[{bar}] {percent:.2f}%", end="\r", style="yellow")
    if progress == total:
        console.print(f"\r[{bar}] {percent:.2f}%", end="\r", style="bright_green")

numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

def experimental_loadbar():
  with Progress() as progress:
    task1 = progress.add_task("[red]Creating...", total=100)
    task2 = progress.add_task("[green]Processing...", total=100)
    task3 = progress.add_task("[cyan]Updating...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.9)
        progress.update(task2, advance=0.6)
        progress.update(task3, advance=0.3)
        time.sleep(0.02)