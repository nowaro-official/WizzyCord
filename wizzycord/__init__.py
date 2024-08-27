# wizzycord/__init__.py

"""
WizzyCord - Eine Python-Bibliothek für einfaches Pycord-Bot-Cog-Management.

Diese Bibliothek bietet Funktionen zum Verwalten von Cogs in Pycord-Bots.
"""

__version__ = "0.2.0"
__author__ = "kainow-code"
__license__ = "MIT"

from .cog_manager import CogManager

__all__ = ['CogManager']
