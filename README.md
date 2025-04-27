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

1. **Benutzerlisten-Verwaltung**: Verwaltet Listen von Benutzer-IDs in JSON-Dateien
2. **Berechtigungssystem**: Stellt Mechanismen bereit, um Befehle nur für bestimmte Benutzer verfügbar zu machen
3. **Discord-Integration**: Optimiert für Pycord mit einfachen Guards für slash commands

## Verwendung

Hier sind einige Beispiele, wie Sie WizzyCord in Ihrem Pycord-Bot verwenden können:

### Benutzerliste verwalten

```python
from wizzycord import UserList

# Benutzerliste erstellen oder laden
users = UserList("data/users.json")

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
checker = GuardCheck("data/admins.json")

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
checker = GuardCheck("data/admins.json")

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

## Technische Details

- Die `UserList`-Klasse speichert Benutzer-IDs in einer JSON-Datei
- Die `GuardCheck`-Klasse verwendet das Singleton-Pattern für einfache Verwendung
- Beide Klassen unterstützen das Nachladen der Benutzerliste zur Laufzeit

## Beitragen

Beiträge zur WizzyCord-Bibliothek sind willkommen! Bitte erstellen Sie ein Issue oder einen Pull Request auf GitHub, wenn Sie Verbesserungen oder Fehlerkorrekturen vorschlagen möchten.

## Lizenz

WizzyCord ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der LICENSE-Datei.
