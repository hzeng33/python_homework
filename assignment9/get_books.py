# Task 2: Understanding HTML and the DOM for the Durham Library Site
# The HTML element for a single entry in the search results list. It's <li> tag, with 
# class="row cp-search-result-item".  
# The title is <h2 class="cp-title"><a href="/item/show/18011361981" target="_parent" lang="en" rel="noopener" data-test-id="bib-title-S981C18011361" data-key="bib-title"><span aria-hidden="true" class="title-content">Real-World Spanish: The Conversation Learning System</span><span class="cp-screen-reader-message">Real-World Spanish: The Conversation Learning System, eAudiobook</span></a></h2>
# The author is <span class="cp-author-link"><span><a target="_parent" rel="noopener noreferrer" class="author-link" data-key="author-link" href="/v2/search?origin=core-catalog-explore&amp;query=Camila%20Vega%20Rivera&amp;searchType=author">Camila Vega Rivera</a></span></span>
# The format of the book and the published year in the same <span> tag, <div class="cp-format-info"><span aria-hidden="true" class="display-info"><span class="display-info-primary">eAudiobook<!-- --> - 2025</span><span class="call-number"></span></span><span class="cp-screen-reader-message">eAudiobook, 2025</span></div>


# Task 3: Write a Program to Extract this Data
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
   
    books_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    results = []
    
    print("Load the page ...\n")
    driver.get(books_url)
    
    #Find all the li elements in that page for the search list results.
    li_elements = driver.find_elements(By.CSS_SELECTOR, 'li.row.cp-search-result-item')
    print(f"Found {len(li_elements)} li elements")
    
    for item in li_elements:
        title = ""
        author_str = ""
        format_year = ""
        
        try:
            title_element = item.find_element(By.CLASS_NAME, 'title-content')
            title = title_element.text.strip()
        except Exception as e:
            print(f"Error extracting title: {e}")
        
        try:
            authors = []
            author_elements = item.find_elements(By.CLASS_NAME, 'author-link')
            for author in author_elements:
                authors.append(author.text.strip())
            author_str = '; '.join(authors) if authors else "N/A"
        except Exception as e:
            print(f"Error extracting author: {e}")
        
        # Extract format and published year.
        try:
            format_year_element = item.find_element(By.CSS_SELECTOR, 'div.cp-format-info span.display-info-primary')
            formate_year = format_year_element.text.strip()
        except Exception as e:
            print(f"Error extracting format/year: {e}")
        
        results.append({
            'Book title': title,
            'Author': author_str,
            'Book format & published year': formate_year
        })
    
    if results:
        df = pd.DataFrame(results)
        
        # Task 4: Write out the Data
        # Save to CSV
        df.to_csv('get_books.csv', index=False)
        print("Data saved to get_books.csv")
        
        # Save to JSON
        with open('get_books.json', 'w') as f:
            json.dump(results, f, indent=4)
        print("Data saved to get_books.json")
        
        print("Extracted data: \n")
        print(df)
    else:
        print("No data extracted.")
        
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")
    
finally:
    driver.quit()

