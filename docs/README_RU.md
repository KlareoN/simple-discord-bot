> Простой Discord bot с красивой архитектурой.
### Архитектура ###
```
- core
    - commands
        - ___init___.py
        - main.py
    - events
        - ___init___.py
        - main.py
    - ___init___.py
- dispatcher.py
- start.py
```

### Функционал ###
- Commands ( !hello )
- Events ( on_ready, on_message )

### Библиотеки для работы ###
- [discord](https://pypi.org/project/discord/)

### Настройка ###
Откройте ``` dispatcher.py ``` найдите ``` self.__token ``` и вставьте токен бота.
