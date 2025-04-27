"""
Guard List - Eine Klasse zum Verwalten von Benutzer-IDs in einer JSON-Datei
"""

import json
import os
from pathlib import Path

class GuardList:
    """
    Verwaltet eine Liste von Benutzer-IDs in einer JSON-Datei.
    
    Attributes:
        file (str or Path): Pfad zur JSON-Datei
        users (list): Liste der Benutzer-IDs
    """
    
    def __init__(self, file):
        """
        Initialisiert die GuardList mit einem Dateipfad.
        
        Args:
            file (str or Path): Pfad zur JSON-Datei
        """
        self.file = Path(file)
        self.users = []
        self._load()
    
    def _load(self):
        """Lädt die Benutzerliste aus der Datei oder erstellt eine neue."""
        # Verzeichnis erstellen, falls nicht vorhanden
        self.file.parent.mkdir(parents=True, exist_ok=True)
        
        # Datei laden oder neue erstellen
        if self.file.exists():
            try:
                with open(self.file, 'r') as f:
                    self.users = json.load(f)
            except Exception as e:
                print(f"Fehler beim Laden der Benutzerliste: {e}")
                self.users = []
        else:
            self._save()
    
    def _save(self):
        """Speichert die Benutzerliste in der Datei."""
        try:
            with open(self.file, 'w') as f:
                json.dump(self.users, f, indent=2)
            return True
        except Exception as e:
            print(f"Fehler beim Speichern der Benutzerliste: {e}")
            return False
    
    def add(self, user_id):
        """
        Fügt einen Benutzer zur Liste hinzu, wenn nicht bereits vorhanden.
        
        Args:
            user_id: Die hinzuzufügende Benutzer-ID
            
        Returns:
            bool: True bei Erfolg, False bei Fehler
        """
        # Benutzer-ID als Integer sicherstellen
        user_id = int(user_id)
        
        # Benutzer hinzufügen, wenn noch nicht in Liste
        if user_id not in self.users:
            self.users.append(user_id)
            return self._save()
        return False
    
    def remove(self, user_id):
        """
        Entfernt einen Benutzer aus der Liste, wenn vorhanden.
        
        Args:
            user_id: Die zu entfernende Benutzer-ID
            
        Returns:
            bool: True bei Erfolg, False bei Fehler oder wenn ID nicht in Liste
        """
        # Benutzer-ID als Integer sicherstellen
        user_id = int(user_id)
        
        # Benutzer entfernen, wenn in Liste
        if user_id in self.users:
            self.users.remove(user_id)
            return self._save()
        return False
    
    def get_all(self):
        """
        Gibt alle Benutzer-IDs zurück.
        
        Returns:
            list: Liste aller Benutzer-IDs
        """
        return self.users
    
    def is_listed(self, user_id):
        """
        Überprüft, ob ein Benutzer in der Liste ist.
        
        Args:
            user_id: Die zu überprüfende Benutzer-ID
            
        Returns:
            bool: True wenn in Liste, sonst False
        """
        return int(user_id) in self.users
    
    def reload(self):
        """Lädt die Benutzerliste aus der Datei neu."""
        self._load()
