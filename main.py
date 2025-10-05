from rich.console import Console
from rich.table import Table
from rich import print as rprint
import js_detector
from version_checker import get_latest_version
from vulnerability_finder import find_cves_for_library
import argparse
from web_scraper import scrape_js_libraries
from utils import print_library_table
import os


# Créez une instance de la classe Console pour afficher un texte riche.
console = Console()


def print_banner():
    banner = """
_______________________________________________________________



       _    _____      _____    _____              _   _ 
      | |  / ____|    / ____|  / ____|     /\     | \ | |
      | | | (___     | (___   | |         /  \    |  \| |
  _   | |  \___ \     \___ \  | |        / /\ \   | . ` |
 | |__| |  ____) |    ____) | | |____   / ____ \  | |\  |
  \____/  |_____/    |_____/   \_____| /_/    \_\ |_| \_|
                                                         
         JS Library Security Scanner by Amel Sid                
                 Version 1.0.0                        
_______________________________________________________________
"""
    print(banner)
def print_header():
    # Affiche l'en-tête du scanner
    rprint("[bold blue]JS Library Scanner[/bold blue] by CyberTeam")
    rprint("[bold green]Version: 1.0.0[/bold green] Sponsored by Visiativ - https://visiativ.com")
    console.rule("[bold red]Scan Report[/bold red]")

def print_library_info(library_name, current_version, latest_version, vulnerabilities):
    # Affiche les informations de la bibliothèque avec la coloration appropriée pour le statut de la version
    version_status = "[green]up to date[/green]" if current_version == latest_version else "[red]outdated[/red]"
    console.print(f"[bold]{library_name}[/bold]: {current_version} (Latest: {latest_version}) - {version_status}")

    # S'il y a des vulnérabilités, les afficher
    if vulnerabilities:
        console.print("[bold red]Vulnerabilities found:[/bold red]")
        for vuln in vulnerabilities:
            console.print(f"[red]- {vuln}[/red]")

def print_library(library_name, current_version, latest_version, vulnerabilities):
    # Crée une table pour afficher les informations sur la bibliothèque
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Library", style="dim", width=12)
    table.add_column("Current Version", style="dim", width=15)
    table.add_column("Latest Version", style="dim", width=15)
    table.add_column("Vulnerabilities", style="dim")

    vulnerabilities_str = "\n".join(vulnerabilities) if vulnerabilities else "None"
    table.add_row(library_name, current_version, latest_version, vulnerabilities_str)

    # Affiche la table à l'aide de la console riche
    console.print(table)


def main():
    print_banner()
    print_header()
    print(os.environ.get('SNYK_API_KEY', 'Variable SNYK_API_KEY non définie'))

    parser = argparse.ArgumentParser(description="Scan a website for JavaScript libraries and their versions.")
    parser.add_argument("-u", "--url", required=True, help="URL of the website to scan.")
    parser.add_argument("-p", "--path", help="Specific path to JavaScript libraries.", default="")
    snyk_api_key = os.environ['SNYK_API_KEY']

    if not snyk_api_key:
        print("La clé API SNYK n'est pas définie.")
        return
    args = parser.parse_args()
    js_libraries = scrape_js_libraries(args.url)

    if js_libraries:
        for lib in js_libraries:
            lib['latest_version'] = get_latest_version(lib['library_name'])
            if lib['latest_version'] != "Inconnu":
                lib['cve'] = find_cves_for_library(lib['library_name'], lib['current_version'], snyk_api_key)
            else:
                lib['cve'] = "N/A"

        print_library_table(js_libraries)
    else:
        print("Aucune bibliothèque JavaScript trouvée.")

if __name__ == "__main__":
    main()

