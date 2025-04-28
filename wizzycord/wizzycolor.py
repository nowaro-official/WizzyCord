"""
WizzyColor - Ein Modul für farbige Konsolenausgaben und Bot-Interface-Darstellung
"""

import os
import platform
from datetime import datetime

# ANSI-Farbcodes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    # Vordergrundfarben
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Helle Vordergrundfarben
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Hintergrundfarben
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Globale Variablen
_color_enabled = False
_system = platform.system()

def init():
    """
    Initialisiert die Farbunterstützung für die Konsole.
    
    Unter Windows wird die ANSI-Farbunterstützung aktiviert, 
    falls notwendig und verfügbar.
    """
    global _color_enabled
    
    # Windows-spezifische Konfiguration
    if _system == 'Windows':
        try:
            # ANSI-Farbcodes für Windows-Konsole aktivieren
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            _color_enabled = True
        except:
            _color_enabled = False
    else:
        # Auf Unix-basierten Systemen generell Farbunterstützung aktivieren
        _color_enabled = True
    
    return _color_enabled

def colored_text(text, color=None, style=None, bg_color=None):
    """
    Formatiert Text mit Farben und Stilen.
    
    Args:
        text (str): Der zu formatierende Text
        color (str, optional): Vordergrundfarbe aus Colors-Klasse
        style (str, optional): Textstil aus Colors-Klasse
        bg_color (str, optional): Hintergrundfarbe aus Colors-Klasse
        
    Returns:
        str: Der formatierte Text mit Farb-Codes
    """
    if not _color_enabled:
        return text
    
    format_str = ""
    if style:
        format_str += style
    if color:
        format_str += color
    if bg_color:
        format_str += bg_color
    
    return f"{format_str}{text}{Colors.RESET}"

def display_bot_interface(bot_name, owner_name, ping=0, commands=0, servers=0, cogs=None):
    """
    Zeigt eine schöne Konsolenanzeige für den Bot-Start an.
    
    Args:
        bot_name (str): Name des Bots
        owner_name (str): Name des Bot-Besitzers
        ping (float, optional): Latenz des Bots in ms
        commands (int, optional): Anzahl der geladenen Befehle
        servers (int, optional): Anzahl der Server, auf denen der Bot läuft
        cogs (list, optional): Liste der geladenen Cogs/Module
    """
    if not _color_enabled:
        init()
    
    # Aktuelles Datum und Uhrzeit
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    # ASCII-Art Banner erstellen
    banner = [
        "╔═══════════════════════════════════════════════════════════╗",
        "║                                                           ║",
        f"║  {colored_text('WIZZY', Colors.BRIGHT_CYAN, Colors.BOLD)}{colored_text('CORD', Colors.BRIGHT_MAGENTA, Colors.BOLD)}                                             ║",
        "║                                                           ║",
        "╚═══════════════════════════════════════════════════════════╝"
    ]
    
    # Informationen
    info = [
        f"Bot: {colored_text(bot_name, Colors.BRIGHT_GREEN, Colors.BOLD)}",
        f"Besitzer: {colored_text(owner_name, Colors.BRIGHT_YELLOW)}",
        f"Startzeit: {colored_text(now, Colors.BRIGHT_BLUE)}",
        f"Ping: {colored_text(f'{ping:.2f}ms', Colors.BRIGHT_MAGENTA)}",
        f"Befehle: {colored_text(str(commands), Colors.BRIGHT_CYAN)}",
        f"Server: {colored_text(str(servers), Colors.BRIGHT_GREEN)}"
    ]
    
    # Cogs/Module Informationen
    if cogs:
        cogs_info = f"Geladene Module: {colored_text(str(len(cogs)), Colors.BRIGHT_YELLOW)}"
        cogs_list = ", ".join([colored_text(cog.split('.')[-1], Colors.BRIGHT_BLUE) for cog in cogs])
    else:
        cogs_info = f"Geladene Module: {colored_text('0', Colors.BRIGHT_RED)}"
        cogs_list = ""
    
    # Ausgabe
    print("\n" + "\n".join(banner))
    print("\n" + "\n".join(info))
    print(cogs_info)
    if cogs_list:
        print(f"Module: {cogs_list}")
    print("\n" + colored_text("Bot ist jetzt online und bereit!", Colors.BRIGHT_GREEN, Colors.BOLD))
    print("=" * 60 + "\n")

# Einfache Logging-Funktionen
def log_info(message):
    """Gibt eine Info-Meldung aus"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = colored_text("[INFO]", Colors.BRIGHT_BLUE, Colors.BOLD)
    time = colored_text(f"[{timestamp}]", Colors.BRIGHT_BLACK)
    print(f"{time} {prefix} {message}")

def log_success(message):
    """Gibt eine Erfolgs-Meldung aus"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = colored_text("[SUCCESS]", Colors.BRIGHT_GREEN, Colors.BOLD)
    time = colored_text(f"[{timestamp}]", Colors.BRIGHT_BLACK)
    print(f"{time} {prefix} {message}")

def log_warning(message):
    """Gibt eine Warnmeldung aus"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = colored_text("[WARNING]", Colors.BRIGHT_YELLOW, Colors.BOLD)
    time = colored_text(f"[{timestamp}]", Colors.BRIGHT_BLACK)
    print(f"{time} {prefix} {message}")

def log_error(message):
    """Gibt eine Fehlermeldung aus"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = colored_text("[ERROR]", Colors.BRIGHT_RED, Colors.BOLD)
    time = colored_text(f"[{timestamp}]", Colors.BRIGHT_BLACK)
    print(f"{time} {prefix} {message}")
