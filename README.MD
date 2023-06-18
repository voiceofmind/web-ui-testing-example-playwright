# Example of the web UI automation framework

### Summary

_Using Python, Playwright_

**Task description:**<br>
https://github.com/lunin-vadim/qa-web

**Web site under test:**<br>
https://enotes.pointschool.ru/login

### Preparations

First install plugins from requirements.txt (better to create a new venv for this project in the project interpreter settings)

### Useful additional parameters for launching tests:

```bash
$ python3 -m pytest tests --headed --slowmo 1000 --screenshot only-on-failure --video retain-on-failure
```

```bash
$ python3 -m pytest tests --browser chromium
$ python3 -m pytest tests --browser firefox
$ python3 -m pytest tests --browser webkit
```

```bash
$ python3 -m pytest tests --browser-channel chrome
$ python3 -m pytest tests --browser-channel msedge
```

```bash
$ python3 -m pytest tests --browser chromium --browser firefox --browser webkit --verbose
```

The tests currently work in chrome (default) and edge (--browser-channel msedge)

From here:<br>
https://github.com/AutomationPanda/playwright-python-tutorial/blob/main/tutorial/5-playwright-tricks.md

### UI tool for checking locators for Playwright

```bash
$ playwright codegen enotes.pointschool.ru/login
```

From here:<br>
https://playwright.dev/python/docs/codegen

### Useful reading:

* https://playwright.dev/python/docs/intro
* https://github.com/AutomationPanda/playwright-python-tutorial