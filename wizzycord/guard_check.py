"""
Guard Check - Eine Klasse zum Überprüfen der Benutzer-Berechtigungen für Discord-Befehle
"""

import json
from pathlib import Path
import discord
from discord.ext import commands

from .user_list import UserList

class GuardCheck:
    """
    Ein Hilfsmodul zum Überprüfen der Benutzerliste.
    Bietet einen Guard zur Integration in Discord-Befehle.
    
    Attributes:
        db_path (Path): Pfad zur JSON-Datei mit der Benutzerliste
        error_message (str): Standardmeldung bei fehlenden Berechtigungen
        _user_list (UserList): Instanz der UserList-Klasse
    """
    _instance = None
    
    def __new__(cls, db_path=None):
        """
        Stellt sicher, dass nur eine Instanz dieser Klasse existiert (Singleton-Pattern).
        
        Args:
            db_path (str or Path, optional): Pfad zur JSON-Datei mit der Benutzerliste.
                                             Default: "db/userlist.json"
        
        Returns:
            GuardCheck: Eine Singleton-Instanz der GuardCheck-Klasse
        """
        if cls._instance is None:
            cls._instance = super(GuardCheck, cls).__new__(cls)
            db_path = db_path or "db/userlist.json"
            cls._instance.db_path = Path(db_path)
            cls._instance.error_message = "Du hast keine Berechtigung, diesen Befehl zu verwenden."
            cls._instance._user_list = UserList(cls._instance.db_path)
        return cls._instance
    
    def set_guard_list(self, path):
        """
        Setzt den Pfad zur Benutzerlisten-Datei.
        
        Args:
            path (str or Path): Neuer Pfad zur JSON-Datei
        """
        self.db_path = Path(path)
        self._user_list = UserList(self.db_path)
    
    def reload(self):
        """Lädt die Benutzerliste aus der Datei neu."""
        self._user_list.reload()
    
    def get_users(self):
        """
        Gibt die aktuelle Benutzerliste zurück.
        
        Returns:
            list: Liste aller Benutzer-IDs
        """
        self._user_list.reload()  # Stellt sicher, dass wir immer die neuesten Daten haben
        return self._user_list.get_all()
    
    def is_listed(self, user_id):
        """
        Überprüft, ob ein Benutzer in der Liste ist.
        
        Args:
            user_id: Die zu überprüfende Benutzer-ID
            
        Returns:
            bool: True wenn in Liste, sonst False
        """
        self._user_list.reload()  # Stellt sicher, dass wir immer die neuesten Daten haben
        return self._user_list.is_listed(user_id)
    
    def add_user(self, user_id):
        """
        Fügt einen Benutzer zur Liste hinzu.
        
        Args:
            user_id: Die hinzuzufügende Benutzer-ID
            
        Returns:
            bool: True bei Erfolg, False bei Fehler
        """
        return self._user_list.add(user_id)
    
    def remove_user(self, user_id):
        """
        Entfernt einen Benutzer aus der Liste.
        
        Args:
            user_id: Die zu entfernende Benutzer-ID
            
        Returns:
            bool: True bei Erfolg, False bei Fehler
        """
        return self._user_list.remove(user_id)
    
    def set_error_message(self, message):
        """
        Setzt die benutzerdefinierte Fehlermeldung.
        
        Args:
            message (str): Neue Fehlermeldung
        """
        self.error_message = message
    
    def guard(self, custom_message=None):
        """
        Erstellt einen Guard für Befehle, der überprüft, ob der Benutzer in der Liste ist.
        
        Args:
            custom_message (str, optional): Eine optionale benutzerdefinierte Fehlermeldung
            
        Returns:
            function: Ein commands.check Decorator
        """
        async def predicate(ctx):
            if not self.is_listed(ctx.author.id):
                message = custom_message if custom_message else self.error_message
                await ctx.respond(message, ephemeral=True)
                return False
            return True
        return commands.check(predicate)
