# crewAI for Joking

Bienvenue dans le projet **crewAI for Joking**, propulsé par [crewAI](https://crewai.com) pour des projets d'IA collaborative. Ce projet est basé sur le modèle **LLaMA 3.2:1B**, un modèle de langage avancé, conçu pour vous permettre de créer un système multi-agent où vos agents collaborent de manière efficace pour résoudre des tâches complexes. Grâce à **crewAI**, vous maximisez l'intelligence collective et les capacités de vos agents.

## Installation

Assurez-vous d'avoir **Python >=3.10 <3.13** installé sur votre système. Ce projet utilise [UV](https://docs.astral.sh/uv/) pour la gestion des dépendances et le traitement des packages, vous offrant ainsi une expérience de configuration et d'exécution fluide.

### Étapes d'installation :

1. Installez `uv` si ce n'est pas déjà fait :

    ```bash
    pip install uv
    ```

2. Ensuite, naviguez dans le répertoire de votre projet et installez les dépendances :

   (Optionnel) Vous pouvez verrouiller les dépendances et les installer en utilisant la commande CLI :

    ```bash
    crewai install
    ```

### Installer Ollama

**Ollama** est une plateforme pour exécuter des modèles LLaMA localement. Voici comment l'installer et l'utiliser dans ce projet.

1. **Téléchargez et installez Ollama :**

   - Allez sur le site officiel d'Ollama pour télécharger et installer l'application : [Télécharger Ollama](https://ollama.com/download)
   - Suivez les instructions d'installation pour votre système d'exploitation (Windows, macOS ou Linux).

2. **Vérifiez l'installation d'Ollama :**

   Une fois installé, ouvrez un terminal ou une invite de commande et exécutez la commande suivante pour vérifier que l'installation a réussi :

    ```bash
    ollama --version
    ```

   Cela devrait afficher la version d'Ollama installée.

3. **Configurer Ollama avec votre projet :**

   - Après l'installation, vous pouvez utiliser Ollama pour charger et exécuter le modèle **LLaMA 3.2:1B** dans votre projet. 
   - Assurez-vous que l'environnement Ollama est prêt à être utilisé avec **crewAI for Joking** en définissant les bonnes configurations dans votre projet.

### Personnalisation

1. **Ajoutez votre `OPENAI_API_KEY` dans le fichier `.env`**
2. Modifiez `src/crew_day_02/config/agents.yaml` pour définir vos agents
3. Modifiez `src/crew_day_02/config/tasks.yaml` pour définir vos tâches
4. Modifiez `src/crew_day_02/crew.py` pour ajouter votre propre logique, outils et arguments spécifiques
5. Modifiez `src/crew_day_02/main.py` pour ajouter des entrées personnalisées pour vos agents et tâches

### Commandes principales :

- **Créer un agent :**  
    ```bash
    crewai create agent <nom_de_l_agent>
    ```

- **Créer une tâche :**  
    ```bash
    crewai create task <nom_de_la_tâche>
    ```

- **Démarrer le projet :**  
    ```bash
    crewai start
    ```

- **Vérifier les agents et tâches :**  
    ```bash
    crewai status
    ```

- **Exécuter le fichier `main.py` :**  
    Pour démarrer le projet, vous pouvez exécuter directement le fichier `main.py` :

    ```bash
    python src/crew_day_02/main.py
    ```


