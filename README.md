![img.png](img.png)
# bbc_scraper
## Selenium scraping implementation
Scrapses the BBC website taking all the articles in the main page save the title, body and link for each article into a json file.

## Classes

Scraper is written with OOP in mind so:

- [article] Object- Article object have a title, body and a link, and a web drive object also have some methods for finding string in article object.
- [data_collection_manager] Object - The article collection manager, initiate all the scraping process also initiate search in all the article objtects available. 
- [file_manager] - A file manager that saves article objects and loads json files into article objects. (Not an object!)
- [linkscraperobject] Object - Object that scrapes the article links on the main site of the BBC.

### A things I would change is to create a article factory object that creates article objects, instead of initiating the webdriver inside the article object also have a print overrding method __repr__ in article object
