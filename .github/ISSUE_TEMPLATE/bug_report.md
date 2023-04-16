---
name: Bug report
about: Create a report to help us improve
title: "[BUG]"
labels: Bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Enter a string of code that has raised an error, like:
```py
import weatherly
client = weatherly.WeatherAPIClient("api key")
client.get_current_weather("London") # <<< this caused an error
```

**Expected behavior**
A clear and concise description of what you expected to happen.

**Environment (please complete the following information):**
 - OS: [e.g. Linux, Ubuntu]
 - Version [e.g. 22.1]
 - Python version [e.g. 3.10]
 - Package version [e.g. 1.0.3]

**Additional context**
Add any other context about the problem here.
