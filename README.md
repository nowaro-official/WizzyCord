
![Wizzycord banner](https://github.com/user-attachments/assets/7aafe5ed-f52b-4d69-b69e-92c0fd22e351)





# WizzyCord

**WizzyCord** ist eine Python-Bibliothek, die für die Verwendung mit [Pycord](https://docs.pycord.dev/en/stable/) optimiert ist. Sie bietet eine Sammlung von nützlichen Funktionen zur Verwaltung von Discord-Bots, einschließlich Embed-Templates, automatischer Fehlerbehandlung und einfacher Datenbankverwaltung.

## Funktionen

- **Embed-Templates**: Erstellen und Verwenden von benutzerdefinierten Embed-Nachrichten.
- **Automatischer Hilfe-Befehl**: Automatisch generierter Hilfe-Befehl für deinen Bot.
- **Status-Wechsler**: Regelmäßige Statusänderungen des Bots.
- **Blacklist-Management**: Verwaltung von Benutzern, die den Bot nicht verwenden dürfen.
- **Datenbank-Wrapper**: Asynchroner Wrapper für `aiosqlite` zur Verwaltung von SQLite-Datenbanken.
- **Cog-Management**: Einfaches Laden, Entladen und Verwalten von Cogs.
- **Fehlerbehandlung**: Automatische Fehlerbehandlung für Slash-Befehle und Fehler-Webhook-Berichte.
- **Benutzerdefiniertes Logging**: Anpassbares Logging für Bot-Aktivitäten.
- **Datetime- und Datei-Utilities**: Hilfsfunktionen für Datums- und Zeitoperationen sowie Dateioperationen.
- **Slash-Befehl-Übersetzung**: Unterstützung für Gruppen, Optionen und Auswahlmöglichkeiten von Slash-Befehlen.
- **Nachrichtentranslation**: Übersetzung von Nachrichten, Embeds, Views, Modals und mehr.

## Installation

Um **WizzyCord** zu installieren, verwende `pip`:

```bash
pip install wizzycord
```

## Nutzung

Hier sind einige grundlegende Beispiele zur Nutzung der Bibliothek:

### Embed-Templates

```python
from wizzycord.embed import CustomEmbed

embed = CustomEmbed(title="Mein Titel", description="Meine Beschreibung")
```

### Automatischer Hilfe-Befehl

```python
from wizzycord.help import generate_help_command

help_command = generate_help_command(bot)
```

### Status-Wechsler

```python
from wizzycord.status import StatusChanger

status_changer = StatusChanger(bot, interval=60)
status_changer.start()
```

### Blacklist-Management

```python
from wizzycord.blacklist import BlacklistManager

blacklist_manager = BlacklistManager()
blacklist_manager.add_user(user_id)
```

### Datenbank-Wrapper

```python
from wizzycord.db import DatabaseWrapper

db = DatabaseWrapper('database.db')
await db.create_table('users', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT'})
await db.insert('users', {'name': 'Alice'})
```

### Cog-Management

```python
from wizzycord.cog_manager import CogManager

cog_manager = CogManager(bot)
cog_manager.load_cog('my_cog')
```

### Fehlerbehandlung

```python
from wizzycord.error_handling import ErrorHandler

error_handler = ErrorHandler(bot)
error_handler.setup()
```

### Benutzerdefiniertes Logging

```python
from wizzycord.logging import CustomLogger

logger = CustomLogger()
logger.info('Bot gestartet')
```

### Datetime- und Datei-Utilities

```python
from wizzycord.utils import get_current_datetime

current_datetime = get_current_datetime()
```

### Slash-Befehl-Übersetzung

```python
from wizzycord.translation import translate_slash_command

translated_command = translate_slash_command('example_command', 'de')
```

### Nachrichtentranslation

```python
from wizzycord.translation import translate_message

translated_message = translate_message('Hello, world!', 'es')
```

## Lizenz

**WizzyCord** ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE) Datei für Details.

## Beiträge

Beiträge sind willkommen! Bitte öffne ein Issue oder einen Pull Request, wenn du Verbesserungen vorschlagen oder Fehler melden möchtest.

## Kontakt

Bei Fragen oder Anregungen kannst du uns unter [example@example.com](mailto:example@example.com) erreichen.

---

Danke, dass du **WizzyCord** verwendest!

```
