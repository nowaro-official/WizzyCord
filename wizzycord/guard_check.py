"""
Guard Check - Eine Klasse zum Überprüfen der Benutzer-Berechtigungen für Discord-Befehle
"""

import json
from pathlib import Path
import discord
from discord.ext import commands

from .guard_list import GuardList

class GuardCheck:
    """
    Ein Hilfsmodul zum Überprüfen der Benutzerliste.
    Bietet einen Guard zur Integration in Discord-Befehle.
    
    Attributes:
        db_path (Path): Pfad zur JSON-Datei mit der Benutzerliste
        error_message (str): Standardmeldung bei fehlenden Berechtigungen
        _guard_list (GuardList): Instanz der GuardList-Klasse
    """
    _instance = None
    _command_error_messages = {}  # Speichert Fehlermeldungen nach Befehlsnamen
    _handler_registered = False   # Verfolgt, ob der Handler bereits registriert ist
    
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
            db_path = db_path or "db/guardlist.json"  # Geändert auf guardlist
            cls._instance.db_path = Path(db_path)
            cls._instance.error_message = "Du hast keine Berechtigung, diesen Befehl zu verwenden."
            cls._instance._guard_list = GuardList(cls._instance.db_path)
        return cls._instance
    
    def setup_handler(self, bot):
        """
        Richtet den globalen Fehlerhandler ein.
        
        Args:
            bot: Die Bot-Instanz
        """
        if not self.__class__._handler_registered:
            @bot.event
            async def on_application_command_error(ctx, error):
                if isinstance(error, commands.CheckFailure):
                    if ctx.command:
                        # Holen der individuellen Fehlermeldung für diesen Befehl, falls vorhanden
                        command_key = f"{ctx.command.qualified_name}"
                        error_msg = self.__class__._command_error_messages.get(command_key, self.error_message)
                        
                        try:
                            await ctx.respond(error_msg, ephemeral=True)
                        except:
                            # Falls bereits geantwortet wurde
                            try:
                                await ctx.send(error_msg, ephemeral=True)
                            except:
                                pass  # Im Notfall ignorieren
            
            self.__class__._handler_registered = True
            print("GuardCheck-Fehlerhandler erfolgreich eingerichtet")
    
    def set_guard_list(self, path):
        """
        Setzt den Pfad zur Benutzerlisten-Datei.
        
        Args:
            path (str or Path): Neuer Pfad zur JSON-Datei
        """
        self.db_path = Path(path)
        self._guard_list = GuardList(self.db_path)
    
    def reload(self):
        """Lädt die Benutzerliste aus der Datei neu."""
        self._guard_list.reload()
    
    def get_users(self):
        """
        Gibt die aktuelle Benutzerliste zurück.
        
        Returns:
            list: Liste aller Benutzer-IDs
        """
        self._guard_list.reload()  # Stellt sicher, dass wir immer die neuesten Daten haben
        return self._guard_list.get_all()
    
    def is_listed(self, user_id):
        """
        Überprüft, ob ein Benutzer in der Liste ist.
        
        Args:
            user_id: Die zu überprüfende Benutzer-ID
            
        Returns:
            bool: True wenn in Liste, sonst False
        """
        self._guard_list.reload()  # Stellt sicher, dass wir immer die neuesten Daten haben
        return self._guard_list.is_listed(user_id)
    
    def add_user(self, user_id):
        """
        Fügt einen Benutzer zur Liste hinzu.
        
        Args:
            user_id: Die hinzuzufügende Benutzer-ID
            
        Returns:
            bool: True bei Erfolg, False bei Fehler
        """
        return self._guard_list.add(user_id)
    
    def remove_user(self, user_id):
        """
        Entfernt einen Benutzer aus der Liste.
        
        Args:
            user_id: Die zu entfernende Benutzer-ID
            
        Returns:
            bool: True bei Erfolg, False bei Fehler
        """
        return self._guard_list.remove(user_id)
    
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
        def decorator(func):
            # Speichern der benutzerdefinierten Fehlermeldung für diesen Befehl
            if hasattr(func, "qualified_name"):
                command_key = func.qualified_name
            else:
                command_key = func.__qualname__
            
            if custom_message:
                self.__class__._command_error_messages[command_key] = custom_message
            
            # Der eigentliche Check ohne Antwortzustellung
            @commands.check
            async def predicate(ctx):
                return self.is_listed(ctx.author.id)
            
            return predicate(func)
        return decorator
