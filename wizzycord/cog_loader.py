"""
Flexibles Modul zum Laden von Discord-Bot-Cogs
"""
import os
from typing import List, Tuple, Optional
from discord import Bot

def load_all_cogs(bot: Bot, cogs_directory: str = "cogs") -> Tuple[List[str], int]:
    """
    Lädt alle Cogs aus dem angegebenen Verzeichnis.
    
    Args:
        bot: Das Discord Bot-Objekt
        cogs_directory: Verzeichnis, in dem die Cogs gespeichert sind (Standard: "cogs")
        
    Returns:
        Tuple mit Liste der geladenen Cogs und Anzahl der Befehle
    """
    loaded_cogs = []
    command_count = 0
    
    # Prüfen, ob das Verzeichnis existiert
    if not os.path.exists(cogs_directory):
        print(f"Warnung: Verzeichnis '{cogs_directory}' existiert nicht.")
        return loaded_cogs, command_count
    
    for filename in os.listdir(cogs_directory):
        if filename.endswith(".py"):
            # Modulpfad konstruieren
            cog_name = f"{cogs_directory}.{filename[:-3]}"
            try:
                bot.load_extension(cog_name)
                loaded_cogs.append(cog_name)
                command_count += 1
            except Exception as e:
                print(f"Fehler beim Laden von {cog_name}: {e}")
    
    return loaded_cogs, command_count

def load_specific_cog(bot: Bot, cog_name: str, cogs_directory: str = "cogs") -> bool:
    """
    Lädt ein spezifisches Cog.
    
    Args:
        bot: Das Discord Bot-Objekt
        cog_name: Name des zu ladenden Cogs (ohne .py)
        cogs_directory: Verzeichnis, in dem die Cogs gespeichert sind (Standard: "cogs")
        
    Returns:
        True, wenn das Cog erfolgreich geladen wurde, sonst False
    """
    full_cog_name = f"{cogs_directory}.{cog_name}"
    try:
        bot.load_extension(full_cog_name)
        return True
    except Exception as e:
        print(f"Fehler beim Laden von {full_cog_name}: {e}")
        return False
