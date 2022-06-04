> A simple Discord bot with beautiful architecture.
### Architecture ###
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
### Libraries to work with ###
- [discord](https://pypi.org/project/discord/)

### Setting ###
Open ``` dispatcher.py ``` find ``` self.__token ``` and insert the bot token.