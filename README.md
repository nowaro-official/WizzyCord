# WizzyCord

WizzyCord ist eine Python-Bibliothek, die für die Verwendung mit [Pycord](https://docs.pycord.dev/en/stable/) optimiert ist. Sie bietet nützliche Funktionen und Module, um die Entwicklung von Discord-Bots zu vereinfachen.

## Installation

Sie können WizzyCord mit pip installieren:

```
pip install wizzycord
```

## Funktionen

WizzyCord bietet die folgenden Hauptfunktionen:

1. **Embed-Templates**: Einfache Erstellung von benutzerdefinierten Embed-Nachrichten.
2. **Automatischer Hilfe-Befehl**: Generiert automatisch einen Hilfe-Befehl für Ihren Bot.
3. **Status-Wechsler**: Ändert den Status Ihres Bots in regelmäßigen Intervallen.
4. **Blacklist-System**: Verwaltet eine Blacklist von Benutzern, die Ihren Bot nicht verwenden dürfen.
5. **Datenbank-Wrapper**: Ein asynchroner Wrapper für SQLite-Datenbankoperationen.

## Verwendung

Hier sind einige Beispiele, wie Sie WizzyCord in Ihrem Pycord-Bot verwenden können:

### Embed-Templates

```python
from wizzycord.embed import EmbedTemplate

# In einem Bot-Befehl
@bot.command()
async def example(ctx):
    embed = EmbedTemplate.create_embed(
        title="Beispiel Embed",
        description="Dies ist ein Beispiel-Embed",
        color=discord.Color.green(),
        fields=[
            {"name": "Feld 1", "value": "Wert 1"},
            {"name": "Feld 2", "value": "Wert 2"}
        ]
    )
    await ctx.send(embed=embed)
```

### Automatischer Hilfe-Befehl

```python
from wizzycord.help import setup as setup_help

# In Ihrer Bot-Initialisierung
setup_help(bot)
```

### Status-Wechsler

```python
from wizzycord.status import setup as setup_status

# In Ihrer Bot-Initialisierung
status_changer = setup_status(bot)

# Um den Status-Wechsler zu stoppen
# status_changer.stop()
```

### Blacklist-System

```python
from wizzycord.blacklist import BlacklistCog

# In Ihrer Bot-Initialisierung
