# LinkedIn_And_Indeed_Web_Scraper

This program scrapes LinkedIn and Indeed for a keyword provided by the user. It returns the first page of results from both websites. The results are sorted by posting data, and they are parsed for only key information (e.g., job title, company name, time posted, etc.).

![alt text](https://cdn.pixabay.com/photo/2014/08/12/23/23/keyboard-417090_960_720.jpg)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install beautifulsoup, lxml, and requests.

```bash
pip install beautifulsoup4
pip install lxml
pip install requests
```

## Usage
Be sure the following import statements are included in the main file:

```python
from bs4 import BeautifulSoup
import requests
from functions import *
from classes import *
import re
```

## License
Copyright (c) 2022 Logan Willans

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
