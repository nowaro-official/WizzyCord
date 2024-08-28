
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
- aiosqlite 0.19.0

## Funktionen

WizzyCord bietet die folgenden Hauptfunktionen:

1. **Embed-Templates**: Einfache Erstellung von benutzerdefinierten Embed-Nachrichten.
2. **Automatischer Hilfe-Befehl**: Generiert automatisch einen Hilfe-Befehl für Ihren Bot.
3. **Status-Wechsler**: Ändert den Status Ihres Bots in regelmäßigen Intervallen.
4. **Blacklist-System**: Verwaltet eine Blacklist von Benutzern, die Ihren Bot nicht verwenden dürfen.
5. **Datenbank-Wrapper**: Ein asynchroner Wrapper für SQLite-Datenbankoperationen, optimiert für die neueste aiosqlite-Version.

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
bot.add_cog(BlacklistCog(bot))
```

### Datenbank-Wrapper

```python
from wizzycord.db import Database

# In Ihrer Bot-Initialisierung oder in einem Cog
db = Database("your_database.db")

# Beispiel für eine Datenbankoperation
async def add_user(user_id: int, username: str):
    await db.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user_id, username))

# Beispiel für eine Massen-Datenbankoperation
async def add_multiple_users(user_data: List[Tuple[int, str]]):
    await db.executemany("INSERT INTO users (id, name) VALUES (?, ?)", user_data)
```

## Beitragen

Beiträge zur WizzyCord-Bibliothek sind willkommen! Bitte erstellen Sie ein Issue oder einen Pull Request auf GitHub, wenn Sie Verbesserungen oder Fehlerkorrekturen vorschlagen möchten.

## Lizenz

WizzyCord ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der LICENSE-Datei.
