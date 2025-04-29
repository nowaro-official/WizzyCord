![Wizzycord banner](https://github.com/user-attachments/assets/38ff9059-f360-4535-8eab-127b94ff8339)

# WizzyCord

WizzyCord ist eine Python-Bibliothek, die für die Verwendung mit [Pycord](https://docs.pycord.dev/en/stable/) 2.6.0 optimiert ist. Sie bietet nützliche Funktionen und Module, um die Entwicklung von Discord-Bots zu vereinfachen. WizzyCord ist kompatibel mit Python 3.9 und höher, einschließlich Python 3.12.

## Installation

Sie können WizzyCord mit pip installieren:

```
pip install wizzycord
```

## Anforderungen

- Python 3.9 oder höher (getestet bis Python 3.12)
- Pycord 2.6.0

## Funktionen

WizzyCord bietet die folgenden Hauptfunktionen:

1. **Berechtigungslisten-Verwaltung**: Verwaltet Listen von Benutzer-IDs in JSON-Dateien
2. **Berechtigungssystem**: Stellt Mechanismen bereit, um Befehle nur für bestimmte Benutzer verfügbar zu machen
3. **Discord-Integration**: Optimiert für Pycord mit einfachen Guards für slash commands
4. **Farbige Konsolenausgabe**: Ermöglicht ansprechende farbige Ausgaben im Terminal
5. **Bot-Interface**: Zeigt eine gut formatierte Startanzeige für Ihren Bot an
6. **Cog-Verwaltung**: Vereinfacht das Laden von Cogs/Modulen in Ihrem Discord-Bot

## Verwendung

Hier sind einige Beispiele, wie Sie WizzyCord in Ihrem Pycord-Bot verwenden können:

### Berechtigungsliste verwalten

```python
from wizzycord import GuardList

# Berechtigungsliste erstellen oder laden
users = GuardList("data/admins.json")

# Benutzer hinzufügen
users.add(123456789)

# Alle Benutzer abrufen
all_users = users.get_all()
print(all_users)  # [123456789]

# Benutzer entfernen
users.remove(123456789)
```

### Berechtigungssystem für Discord-Befehle

```python
from discord.ext import commands
from discord import option
from wizzycord import GuardCheck

# Bot erstellen
bot = discord.Bot(intents=discord.Intents.all())

# GuardCheck initialisieren
checker = GuardCheck("db/admins.json")

# Optionale benutzerdefinierte Fehlermeldung setzen
checker.set_error_message("Du hast keine Admin-Rechte für diesen Befehl!")

# Befehl mit Berechtigungsprüfung
@bot.slash_command(name="admin", description="Ein Admin-Befehl")
@checker.guard()
async def admin_command(ctx):
    await ctx.respond("Du hast Admin-Rechte!", ephemeral=True)

# Befehl mit benutzerdefinierter Fehlermeldung
@bot.slash_command(name="special", description="Ein spezieller Befehl")
@checker.guard("Dieser Befehl ist nur für spezielle Benutzer!")
async def special_command(ctx):
    await ctx.respond("Du bist ein spezieller Benutzer!", ephemeral=True)
```

### Admin-Verwaltung

```python
from discord import option
from wizzycord import GuardCheck

# GuardCheck initialisieren
checker = GuardCheck("db/admins.json")

# Admin-Befehle Gruppe
@bot.slash_command(name="admin", description="Admin-Befehle")
async def admin(ctx):
    pass

# Fügt einen Benutzer zur Admin-Liste hinzu
@admin.command(name="add", description="Fügt einen Benutzer zur Admin-Liste hinzu")
@checker.guard()  # Nur vorhandene Admins können andere hinzufügen
@option("user", discord.User, description="Der hinzuzufügende Benutzer")
async def admin_add(ctx, user: discord.User):
    if checker.add_user(user.id):
        await ctx.respond(f"Benutzer {user.name} wurde zur Admin-Liste hinzugefügt!", ephemeral=True)
    else:
        await ctx.respond(f"Benutzer {user.name} ist bereits in der Admin-Liste!", ephemeral=True)

# Zeigt alle Benutzer in der Admin-Liste an
@admin.command(name="list", description="Zeigt alle Benutzer in der Admin-Liste an")
@checker.guard()  # Nur Admins können die Liste sehen
async def admin_list(ctx):
    users = checker.get_users()
    if not users:
        await ctx.respond("Die Admin-Liste ist leer!", ephemeral=True)
        return
    
    # Benutzernamen auflösen
    user_strings = []
    for user_id in users:
        try:
            user = await bot.fetch_user(user_id)
            user_strings.append(f"{user.name} (ID: {user_id})")
        except:
            user_strings.append(f"Unbekannter Benutzer (ID: {user_id})")
    
    # Antwort formatieren
    response = "**Admin-Liste:**\n" + "\n".join(user_strings)
    await ctx.respond(response, ephemeral=True)
```

### Farbige Konsolenausgabe

```python
from wizzycord import init, Fore, Style, create_message_line, display_status_line

# Farbunterstützung aktivieren
init()

# Basisbeispiele für farbigen Text
print(f"{Fore.RED}Das ist rot!{Fore.RESET}")
print(f"{Style.BOLD}{Fore.GREEN}Das ist fett und grün!{Style.RESET_ALL}")
print(f"{Style.UNDERLINE}{Fore.BLUE}Das ist unterstrichen und blau{Style.RESET_ALL}")

# Statuszeilen anzeigen
print(display_status_line("Der Bot wird gestartet...", "info"))
print(display_status_line("Der Bot wurde erfolgreich gestartet!", "success"))
print(display_status_line("Ein Befehl konnte nicht geladen werden.", "warning"))
print(display_status_line("Verbindung zum Discord-Server fehlgeschlagen!", "error"))

# Einfache Nachrichtenboxen
print(create_message_line("Willkommen zurück!"))
```

### Bot-Interface anzeigen

```python
import discord
from wizzycord import init, display_bot_interface

# Bot-Konfiguration
bot = discord.Bot(intents=discord.Intents.default())

@bot.event
async def on_ready():
    """Wird ausgelöst, wenn der Bot bereit ist"""
    # Besitzer abrufen (Optional)
    owner = await bot.fetch_user(OWNER_ID)
    
    # Farbunterstützung aktivieren
    init()
    
    # Bot-Interface anzeigen
    display_bot_interface(
        bot_name=bot.user.name,
        owner_name=owner.name,
        ping=bot.latency * 1000,
        commands=10,  # Anzahl der geladenen Befehle
        servers=len(bot.guilds),
        cogs=["cogs.admin", "cogs.utils"]  # Liste der geladenen Cogs/Module
    )
```

### Discord-Embed-Farben verwenden

```python
from discord import Embed
from wizzycord import Color

# Einen schönen Embed mit vordefinierten Farben erstellen
embed = Embed(
    title="Willkommens-Nachricht",
    description="Herzlich willkommen auf unserem Server!",
    color=Color.BLURPLE  # Discord's Blau/Lila Farbe
)

# Weitere Beispiele für Embed-Farben
success_embed = Embed(title="Erfolg", color=Color.SUCCESS)
warning_embed = Embed(title="Warnung", color=Color.WARNING)
error_embed = Embed(title="Fehler", color=Color.ERROR)
```

### Cogs verwalten

```python
import discord
from wizzycord import load_all_cogs, load_specific_cog

# Bot erstellen
bot = discord.Bot(intents=discord.Intents.default())

# Alle Cogs aus dem Standard-Verzeichnis laden
loaded_cogs, command_count = load_all_cogs(bot)
print(f"{len(loaded_cogs)} Cogs geladen mit insgesamt {command_count} Befehlen.")

# ODER: Alle Cogs aus einem benutzerdefinierten Verzeichnis laden
loaded_cogs, command_count = load_all_cogs(bot, "modules")

# Ein einzelnes Cog laden
success = load_specific_cog(bot, "musik")
if success:
    print("Musik-Cog erfolgreich geladen!")
else:
    print("Fehler beim Laden des Musik-Cogs.")
```

### Komplettes Bot-Setup

```python
import discord
import os
from dotenv import load_dotenv
from wizzycord import (
    init, 
    display_bot_interface,
    load_all_cogs,
    GuardCheck
)

# .env-Datei laden
load_dotenv()
TOKEN = os.getenv("TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Bot initialisieren
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)

# GuardCheck initialisieren
checker = GuardCheck("db/admins.json")

@bot.event
async def on_ready():
    # Besitzer abrufen
    owner = await bot.fetch_user(OWNER_ID)
    
    # Konsolenfarben aktivieren
    init()
    
    # Interface anzeigen
    display_bot_interface(
        bot_name=bot.user.name,
        owner_name=owner.name,
        ping=bot.latency * 1000,
        commands=command_count,
        servers=len(bot.guilds),
        cogs=loaded_cogs
    )
    
    # Bot-Status setzen
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, 
        name="den Server"
    ))

# Hauptprogramm
if __name__ == "__main__":
    # Cogs laden
    loaded_cogs, command_count = load_all_cogs(bot)
    
    # Bot starten
    bot.run(TOKEN)
```

## Technische Details

- Die `GuardList`-Klasse speichert Benutzer-IDs in einer JSON-Datei
- Die `GuardCheck`-Klasse verwendet das Singleton-Pattern für einfache Verwendung
- Beide Klassen unterstützen das Nachladen der Benutzerliste zur Laufzeit
- Die `wizzycolor`-Funktionen bieten plattformübergreifende Unterstützung für farbige Konsolenausgaben
- Die Farbunterstützung wird automatisch für Windows und Unix-basierte Systeme konfiguriert
- Die `cog_loader`-Funktionen vereinfachen das dynamische Laden von Bot-Modulen

## Beitragen

Beiträge zur WizzyCord-Bibliothek sind willkommen! Bitte erstellen Sie ein Issue oder einen Pull Request auf GitHub, wenn Sie Verbesserungen oder Fehlerkorrekturen vorschlagen möchten.

## Lizenz

WizzyCord ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der LICENSE-Datei.
