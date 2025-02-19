from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from dotenv import load_dotenv
import os
import shutil
from pathlib import Path

load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class JobTrendJournalist:
    """JobTrendJournalist crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    ollama = LLM(model="ollama/phi4", api_base="http://localhost:11434")

    def __init__(self):
        articles_dir = Path("articles")

        if articles_dir.exists():
            shutil.rmtree(articles_dir)
            print("Deleted existing articles directory")

        articles_dir.mkdir(parents=True, exist_ok=True)
        print("Created articles directory")

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool()],
            verbose=True,
            llm=self.ollama,
        )

    @agent
    def web_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config["web_scraper"],
            tools=[ScrapeWebsiteTool()],
            verbose=True,
            llm=self.ollama,
        )

    @agent
    def analyst_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["analyst_writer"],
            tools=[ScrapeWebsiteTool()],
            verbose=True,
            llm=self.ollama,
        )

    @agent
    def file_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["file_manager"],
            tools=[FileWriterTool(base_path=Path("articles"))],
            verbose=True,
            llm=self.ollama,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def web_scraping_task(self) -> Task:
        return Task(
            config=self.tasks_config["web_scraping_task"],
        )

    @task
    def analysis_writing_task(self) -> Task:
        return Task(config=self.tasks_config["analysis_writing_task"])

    @task
    def file_saving_task(self) -> Task:
        return Task(config=self.tasks_config["file_saving_task"])

    @crew
    def crew(self) -> Crew:
        """Creates the JobTrendJournalist crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
