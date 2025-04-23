# Data Analyser

Ce projet est un outil d'analyse de données avec des fonctionnalités de visualisation. Il permet de charger des données, d'effectuer des analyses statistiques et de générer des graphiques pour visualiser les résultats.

## Structure du projet

### Fichiers principaux

- **`main.py`** : Point d'entrée principal du projet. Fournit une interface en ligne de commande pour charger des données, effectuer des analyses et générer des visualisations.
- **`README.md`** : Documentation du projet.
- **`.gitignore`** : Liste des fichiers et dossiers à ignorer par Git.

### Dossiers

- **`src/`** : Contient les modules principaux du projet.

  - **`data_loader.py`** : Classe `DataLoader` pour charger et valider les données à partir de fichiers CSV.
  - **`analyzer.py`** : Classe `DataAnalyzer` pour effectuer des analyses statistiques et des segmentations.
  - **`visualizer.py`** : Classe `DataVisualizer` pour générer des graphiques (barres, lignes, camemberts, heatmaps).
  - **`__init__.py`** : Fichier d'initialisation du module `src`.

- **`tests/`** : Contient les tests unitaires pour les modules du projet.

  - **`test_data_loader.py`** : Tests pour la classe `DataLoader`.
  - **`test_analyzer.py`** : Tests pour la classe `DataAnalyzer`.
  - **`test_visualizer.py`** : Tests pour la classe `DataVisualizer`.
  - **`__init__.py`** : Fichier d'initialisation du module `tests`.

- **`data/`** : Contient les fichiers de données d'entrée (ex. `sample_data.csv`).
- **`results/`** : Contient les résultats générés (ex. graphiques sauvegardés).

- **`.pytest_cache/`** : Cache généré par Pytest pour optimiser les tests.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/loziamina/data_analyser/tree/main
   cd data_analyser
   ```

```bash
python -m venv venv
venv\Scripts\activate
```

```bash
pip install
pip install pandas matplotlib seaborn scikit-learn pytest
```

```
Run Tests
```

pytest

```
Example Commands
1. Show summary statistics
```

python main.py data/sample_data.csv --analysis summary

```
2. Show time-series analysis (no plot)
```

python main.py data/sample_data.csv --analysis time-series

```
3. Show top spending categories + bar chart (display only)
```

python main.py data/sample_data.csv --analysis top-categories --plot bar

```
4. Generate and save a bar chart
```

python main.py data/sample_data.csv --analysis top-categories --plot bar --output results/top_categories.png

```
5. Show pie chart (for top spending)
```

python main.py data/sample_data.csv --analysis top-categories --plot pie

```
6. Generate a heatmap of numeric correlations
```

python main.py data/sample_data.csv --plot heatmap --analysis summary
