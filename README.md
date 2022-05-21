# template to make streamlit apps

To make a streamlit apps, we may want 

- use multiple pages(so we can have many functions without execute all codes etc.)
- change application urls for each page and selected fields
  - so we can pass a url to guide users to a specific page
  - so we can add links in the apps to guide user to another view(to recommendation of items in a recommendation list)
- pack pre-process together
- use a front(index) page
- etc.

this is a template to make these easily

### how to add a new page

implement a page class, write the code in a `run` method

add the page class to `page_class` in `app.py`

## Note

Source code changes in `AppData` and `AppURL` will not reflect until restart apps.

You cannot empty the field after select(only to reset to another value).

### apps make from this template

- https://github.com/lightondust/token-analysis
- https://github.com/lightondust/top2vec-apps