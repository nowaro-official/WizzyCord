"""
WizzyColor - Ein einfaches Modul für farbige Ausgaben in Discord-Bots
"""
import os
import time

# Konsolenfarben
class Fore:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

# Konsolenstile
class Style:
    RESET_ALL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Box-Zeichen für Tabellen
BOX_CHARS = {
    'h_line': '─',
    'v_line': '│',
    'top_left': '┌',
    'top_right': '┐',
    'bottom_left': '└',
    'bottom_right': '┘',
    'middle_left': '├',
    'middle_right': '┤',
    'cross': '┼'
}

# Discord-Farben für Embeds
class Color:
    DEFAULT = 0x000000      # Schwarz
    RED = 0xFF0000          # Rot
    GREEN = 0x00FF00        # Grün
    BLUE = 0x0000FF         # Blau
    YELLOW = 0xFFFF00       # Gelb
    CYAN = 0x00FFFF         # Cyan
    MAGENTA = 0xFF00FF      # Magenta
    WHITE = 0xFFFFFF        # Weiß
    
    # Discord-Farbpalette
    BLURPLE = 0x5865F2      # Discord Blau/Lila
    SUCCESS = 0x57F287      # Erfolg (Grün)
    WARNING = 0xFEE75C      # Warnung (Gelb)
    ERROR = 0xED4245        # Fehler (Rot)

# Initialisierung für Windows-Farbunterstützung
def init():
    """Aktiviert ANSI-Farben in der Windows-Konsole"""
    import os
    if os.name == 'nt':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except:
            pass
    return True

def create_exact_table(bot_name="", owner_name="", ping="", commands=0, servers=0):
    """
    Erstellt eine Tabelle nach dem Beispiel
    
    Parameters:
    - bot_name: Name des Bots (optional)
    - owner_name: Name des Besitzers (optional)
    - ping: Ping in ms (optional)
    - commands: Anzahl der Befehle (optional)
    - servers: Anzahl der Server (optional)
    
    Returns:
    - Formatierte Tabelle als String
    """
    # Exakte Spaltenbreiten
    bot_width = 25
    owner_width = 25
    ping_width = 12
    commands_width = 9
    server_width = 8
    
    # Ping als String formatieren, falls es eine Zahl ist
    ping_str = f"{ping:.2f}ms" if isinstance(ping, float) else ping
    
    # Gesamtbreite berechnen
    total_width = bot_width + owner_width + ping_width + commands_width + server_width + 6  # +6 für die Trennlinien
    
    # Tabelle erstellen
    lines = []
    
    # Oberer Rahmen
    lines.append(f"{Fore.WHITE}{BOX_CHARS['top_left']}{BOX_CHARS['h_line'] * (total_width - 2)}{BOX_CHARS['top_right']}")
    
    # Überschriftenzeile
    header_line = f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    header_line += f"{Fore.RED}Bot{' ' * (bot_width - 3)}"
    header_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    header_line += f"{Fore.YELLOW}Owner{' ' * (owner_width - 5)}"
    header_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    header_line += f"{Fore.BLUE}Ping{' ' * (ping_width - 4)}"
    header_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    header_line += f"{Fore.GREEN}Befehle{' ' * (commands_width - 7)}"
    header_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    header_line += f"{Fore.MAGENTA}Server{' ' * (server_width - 6)}"
    header_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    lines.append(header_line)
    
    # Trennlinie
    separator = f"{Fore.WHITE}{BOX_CHARS['middle_left']}"
    separator += f"{BOX_CHARS['h_line'] * bot_width}{BOX_CHARS['cross']}"
    separator += f"{BOX_CHARS['h_line'] * owner_width}{BOX_CHARS['cross']}"
    separator += f"{BOX_CHARS['h_line'] * ping_width}{BOX_CHARS['cross']}"
    separator += f"{BOX_CHARS['h_line'] * commands_width}{BOX_CHARS['cross']}"
    separator += f"{BOX_CHARS['h_line'] * server_width}{BOX_CHARS['middle_right']}"
    lines.append(separator)
    
    # Datenzeile
    data_line = f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    data_line += f"{Fore.RED}{bot_name}{' ' * (bot_width - len(str(bot_name)))}"
    data_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    data_line += f"{Fore.YELLOW}{owner_name}{' ' * (owner_width - len(str(owner_name)))}"
    data_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    data_line += f"{Fore.BLUE}{ping_str}{' ' * (ping_width - len(str(ping_str)))}"
    data_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    data_line += f"{Fore.GREEN}{commands}{' ' * (commands_width - len(str(commands)))}"
    data_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    data_line += f"{Fore.MAGENTA}{servers}{' ' * (server_width - len(str(servers)))}"
    data_line += f"{Fore.WHITE}{BOX_CHARS['v_line']}"
    lines.append(data_line)
    
    # Unterer Rahmen
    lines.append(f"{Fore.WHITE}{BOX_CHARS['bottom_left']}{BOX_CHARS['h_line'] * (total_width - 2)}{BOX_CHARS['bottom_right']}")
    
    return "\n".join(lines)

def create_exact_status_box(title, content, width=36, title_color=None, content_color=None):
    """
    Erstellt eine Status-Box exakt wie im Screenshot
    
    Parameters:
    - title: Titel der Box (z.B. "Bot-Status")
    - content: Inhalt (z.B. "Ich bin online")
    - width: Breite der Box
    - title_color: Farbe des Titels (optional)
    - content_color: Farbe des Inhalts (optional)
    
    Returns:
    - Formatierte Status-Box als String
    """
    # Standardfarben, falls nicht angegeben
    if title_color is None:
        title_color = Fore.WHITE
    if content_color is None:
        content_color = Fore.GREEN if title == "Bot-Status" else Fore.WHITE
    
    # Box erstellen
    lines = []
    
    # Oberer Rahmen
    lines.append(f"{Fore.WHITE}{BOX_CHARS['top_left']}{BOX_CHARS['h_line'] * (width - 2)}{BOX_CHARS['top_right']}")
    
    # Inhaltszeile
    # Genau wie im Screenshot: Text direkt nach dem Rahmen ohne Leerzeichen
    padding = width - len(title) - len(content) - 2 - 2  # -2 für Rahmen und -2 für ": "
    lines.append(f"{Fore.WHITE}{BOX_CHARS['v_line']}{title_color}{title}: {content_color}{content}{Fore.WHITE}{' ' * padding}{BOX_CHARS['v_line']}")
    
    # Unterer Rahmen
    lines.append(f"{Fore.WHITE}{BOX_CHARS['bottom_left']}{BOX_CHARS['h_line'] * (width - 2)}{BOX_CHARS['bottom_right']}")
    
    return "\n".join(lines)

def display_cogs(cogs):
    """
    Zeigt die geladenen Cogs an
    
    Parameters:
    - cogs: Liste der geladenen Cogs
    
    Returns:
    - Formatierte Liste der Cogs als String
    """
    if not cogs:
        return f"{Fore.WHITE}Keine Cogs geladen."
    
    lines = [f"{Fore.WHITE}Geladene Cogs:"]
    
    for i, cog in enumerate(cogs, 1):
        lines.append(f"{Fore.GREEN}{i}. {Fore.WHITE}{cog}")
    
    return "\n".join(lines)

def display_bot_interface(bot_name="", owner_name="", ping="", commands=0, servers=0, cogs=None, timestamp=None, 
                         show_table=True, show_status=True, show_cogs=True):
    """
    Zeigt das vollständige Bot-Interface an
    
    Parameters:
    - bot_name: Name des Bots (optional)
    - owner_name: Name des Besitzers (optional)
    - ping: Ping in ms (optional)
    - commands: Anzahl der Befehle (optional)
    - servers: Anzahl der Server (optional)
    - cogs: Liste der geladenen Cogs (optional)
    - timestamp: Zeitstempel (optional)
    - show_table: Tabelle anzeigen (optional, Standard: True)
    - show_status: Status-Boxen anzeigen (optional, Standard: True)
    - show_cogs: Cog-Liste anzeigen (optional, Standard: True)
    """
    # Konsole löschen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Standardzeitstempel, falls keiner angegeben wurde
    if timestamp is None:
        timestamp = time.strftime('%d.%m.%Y %H:%M:%S')
    
    # Tabelle anzeigen, falls gewünscht
    if show_table:
        table = create_exact_table(bot_name, owner_name, ping, commands, servers)
        print(table)
        print()  # Leerzeile
    
    # Statusboxen anzeigen, falls gewünscht
    if show_status:
        status_box = create_exact_status_box("Bot-Status", "Ich bin online")
        print(status_box)
        time_box = create_exact_status_box("Gestartet am", timestamp)
        print(time_box)
    
    # Cogs anzeigen, falls gewünscht und vorhanden
    if show_cogs and cogs:
        print()  # Leerzeile
        print(display_cogs(cogs))

def create_message_line(message, width=60, color=Fore.CYAN):
    """
    Erstellt eine einfache Mitteilungszeile mit farbigem Text
    
    Parameters:
    - message: Die Mitteilung, die angezeigt werden soll
    - width: Die Breite der Zeile (Standard: 60)
    - color: Die Farbe der Mitteilung (Standard: Cyan)
    
    Returns:
    - Formatierte Mitteilungszeile als String
    """
    # Rahmen erstellen
    top_border = f"{Fore.WHITE}{BOX_CHARS['top_left']}{BOX_CHARS['h_line'] * (width - 2)}{BOX_CHARS['top_right']}"
    bottom_border = f"{Fore.WHITE}{BOX_CHARS['bottom_left']}{BOX_CHARS['h_line'] * (width - 2)}{BOX_CHARS['bottom_right']}"
    
    # Mitteilung formatieren
    # Wenn die Mitteilung zu lang ist, kürzen
    if len(message) > width - 4:
        message = message[:width - 7] + "..."
    
    # Zeile mit Mitteilung erstellen
    message_line = f"{Fore.WHITE}{BOX_CHARS['v_line']} {color}{message}{Fore.WHITE}{' ' * (width - len(message) - 3)}{BOX_CHARS['v_line']}"
    
    # Alles zusammenfügen
    return f"{top_border}\n{message_line}\n{bottom_border}"

def display_status_line(message, status="info"):
    """
    Zeigt eine Statuszeile mit farbcodiertem Status an
    
    Parameters:
    - message: Die Statusmeldung
    - status: Status-Typ (info, success, warning, error)
    
    Returns:
    - Formatierte Statuszeile
    """
    # Farbe basierend auf Status wählen
    color = Fore.CYAN  # Standard: Info (Cyan)
    prefix = "INFO"
    
    if status.lower() == "success":
        color = Fore.GREEN
        prefix = "ERFOLG"
    elif status.lower() == "warning":
        color = Fore.YELLOW
        prefix = "WARNUNG"
    elif status.lower() == "error":
        color = Fore.RED
        prefix = "FEHLER"
    
    # Mitteilung mit Präfix
    full_message = f"[{prefix}] {message}"
    
    # Mitteilungszeile erstellen und zurückgeben
    return create_message_line(full_message, color=color)
