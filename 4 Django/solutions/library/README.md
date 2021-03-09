





## Templates

- index
  - search tab
    - search box + button
    - list of search results (title, image, summary, etc)
  - favorites tab
    - list of favorites (title, image, summary, etc)

## Views

- index
  - renders the index template
- save_favorite_book
  - receives json data and saves it to the database
- get_favorite_books
  - gets all the saved books out of the database and show it in the page


## Models

- Book
  - title (CharField)
  - author (CharField)
  - image_url (CharField)


