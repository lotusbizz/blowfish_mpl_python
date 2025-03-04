"""
Пакет blowfish - Реализация алгоритма Blowfish на Python

Основные компоненты:
- Blowfish: Базовый класс для шифрования/дешифрования блоков
- BlowfishCBC: Реализация режима CBC с PKCS7-дополнением

Пример использования:
>>> from blowfish import BlowfishCBC
>>> cipher = BlowfishCBC(key=b'secret', iv=b'12345678')
>>> encrypted = cipher.encrypt(b'Hello World')
"""

from .core import (
    Blowfish,
    BlowfishCBC,
)

__all__ = [
    "Blowfish",
    "BlowfishCBC",
]

__version__ = "1.0.0"
__author__ = "lotusbizz"
__license__ = "MIT"

# Инициализация логгера при импорте пакета
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
