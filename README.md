# Custom_Python_Logging

My preferred setup for logging in Python. This is just a customer formatter/config for the Python logging module.  It's quicker to put it on GitHub and pull it into my projects than it is to google how logging formats work every time I need to log something.

![image](https://user-images.githubusercontent.com/31708500/149706107-6277b08d-e805-4c24-927e-e6079563780b.png)

To make use of this, place `logging_setup.py` in your project.
For each script where you want to use this, place the line `log = logging_setup.init_logging(__name__, complex=True)` somewhere at the top.  From there you use it like you would normally use the logging module.

If you do not have the `colorama` library installed, then set `complex=False`, otherwise the formatting will break.  Without colorama, this format will still work, just without all the pretty colors.

| SEVERITY  | COLOR |
| ------------- | ------------- |
| DEBUG  | BLUE  |
| INFO | GREEN  |
| WARNING  | YELLOW  |
| ERROR  | RED  |
| CRITICAL  | MAGENTA  |

As always, license blah blah blah.  I slapped an MIT license on this, which I think I'm allowed to do?  Something about Python Software Foundation license?  Do I have to mention that?  I used Python.  Because it's a Python module.  And I used the Logging module.  Because, you know, logging.  Anyways, see the logging module and Python itself for their licenses, this is just ~70 lines of code.

Do what you want with my code.  Be free.  Live your life.  Log to your heart's content, and now with colors.  May your existence be prosperous.
