# ================================================
# run_click_cli.py – Professional CLI built with Click
# This is the official entry point for running the AI Agent
# via a structured and extensible Command Line Interface.
# Always use this file for professional execution and external integration.
# ================================================

import click
import json
from agent.base import Agent
from agent.analyzer import SimpleAnalyzer

@click.group()
def cli():
    """Universal Agent CLI"""
    pass

@cli.command()
@click.argument('task')
@click.option('--status', default=None, help='Optional task status (completed, failed, processing)')
def send_task(task, status):
    """Send a new task to the agent."""
    if not status:
        status = click.prompt("Please enter status", type=click.Choice(['completed', 'failed', 'processing']), default='completed')

    analyzer = SimpleAnalyzer()
    agent = Agent("UniversalAgent", analyzer)
    agent.receive_task(task, status)

@cli.command()
def show_memory():
    """Display stored tasks from memory."""
    analyzer = SimpleAnalyzer()
    agent = Agent("UniversalAgent", analyzer)
    agent.show_memory()

@cli.command()
def reset_memory():
    """Reset the memory database."""
    analyzer = SimpleAnalyzer()
    agent = Agent("UniversalAgent", analyzer)
    if click.confirm("Are you sure you want to reset memory?"):
        agent.memory.reset_memory()

@cli.command()
@click.option('--output', default='memory.json', help='Output file name')
def export_memory(output):
    """Export memory to JSON file."""
    analyzer = SimpleAnalyzer()
    agent = Agent("UniversalAgent", analyzer)
    memory_data = agent.memory.get_all_tasks()
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(memory_data, f, ensure_ascii=False, indent=2)
    click.echo(f"Memory exported to {output}")

if __name__ == '__main__':
    cli()
