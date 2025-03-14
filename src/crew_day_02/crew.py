from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CrewDay02:
    """CrewDay02 crew"""

    ollama_1b = LLM(model="ollama/llama3.2:1b", base_url="http://localhost:11434")

    @agent
    def chuck_norris_joke_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['chuck_norris_joke_generator'],
            verbose=True,
            llm=self.ollama_1b
        )

    @agent
    def chuck_norris_joke_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['chuck_norris_joke_picker'],
            verbose=True
        )

    @task
    def generate_joke_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_joke_task'],
            callback=self.save_output_to_file  # Ajout du callback
        )

    @task
    def generate_joke_picker_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_joke_task'],
            callback=self.save_output_to_file  # Ajout du callback
        )

    def save_output_to_file(self, output: str):
        """Sauvegarde le résultat dans un fichier rapport.md"""
        with open("rapport.md", "a", encoding="utf-8") as file:
            file.write(f"\n### Résultat de la tâche:\n{output}\n\n")

    @crew
    def crew(self) -> Crew:
        """Creates the CrewDay02 crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
