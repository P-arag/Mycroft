from utils.banner import get_banner
from utils.load_url_blueprints import load_urls
import click
import colorama

@click.command("--username", "-u", help="Specify username for the target to be hunted")
banner = get_banner()
print(banner)

print(load_urls())

