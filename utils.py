# utils.py
from rich.console import Console
from rich.table import Table

#  la console est initialisée dans ce fichier si elle n'est utilisée que localement.
console = Console()

def print_library_table(libraries_info):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Lib", style="dim", width=12)
    table.add_column("Version", style="dim", width=8)
    table.add_column("CVE", style="dim", width=20)
    table.add_column("New Version", style="dim", width=12)
    table.add_column("Reco", style="dim", width=20)

    for lib_info in libraries_info:
        # Les valeurs 'N/A' sont utilisées comme placeholders pour les colonnes qui seront remplies plus tard
        table.add_row(
            lib_info["library_name"],
            lib_info["current_version"],
            "N/A",  # Placeholder pour la colonne CVE
            lib_info["latest_version"],
            "N/A"  # Placeholder pour la colonne Reco
        )

    console.print(table)
