# recipe-06: pip install

# Run pip-install.sh
# Then, pip install beautifulsoup4

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# Package upgrade: pip install --upgrade beautifulsoup4
# Package remove: pip uninstall beautifulsoup4