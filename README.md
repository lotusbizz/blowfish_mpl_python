# Blowfish Implementation in Python

Реализация алгоритма Blowfish на Python без внешних зависимостей

## Особенности
- Режим CBC с PKCS7 padding
- Поддержка ключей 4-56 байт
- Полная проверка данных

## Установка
```
git clone https://github.com/lotusbizz/blowfish_impl.git
cd blowfish_impl
```

## Использование
```
from blowfish.core import BlowfishCBC
import os

key = b"secret_key"
iv = os.urandom(8)
bf = BlowfishCBC(key, iv)

ciphertext = bf.encrypt(b"Hello World")
plaintext = bf.decrypt(ciphertext)
```

## Запуск демо
```
python demo.py
```

## Ограничения
- Не использовать для защиты реальных данных
- Только для образовательных целей
```

## 5. blowfish/__init__.py
```python
"""
Пакет для реализации алгоритма Blowfish
"""

from .core import Blowfish, BlowfishCBC

__all__ = ['Blowfish', 'BlowfishCBC']
__version__ = '1.0.0'
```

Для завершения проекта:

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите демо:
```bash
python demo.py
```

Это полная структура проекта, включающая:
- Модульную реализацию алгоритма
- Автоматизированные тесты
- Демонстрационную программу
- Документацию
- Поддержку установки зависимостей
