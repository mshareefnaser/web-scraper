import requests
from bs4 import BeautifulSoup


# return number of citations needed on page
def get_citations_needed_count(url_variable):
    """
    Takes a Wikipedia URL and returns the number of passages that require citations.
    """
    # Take in a url string and return an integer
    req = requests.get(url_variable)
    markup = req.text
    soup = BeautifulSoup(markup, 'html.parser')
    # find all paragraph elements that contain [citation needed]
    citation_tags = soup.find_all('sup', {'class': 'noprint Inline-Template Template-Fact'})
    return len(citation_tags)


# return those cases and include the relevant passage (parent element)
def get_citations_needed_report(url_variable):
    """
    Takes a Wikipedia URL and returns the parent passages that require citations.
    """
    # Take in a url string and return report string containing each citation listed in the order found
    # Make request to the url
    req = requests.get(url_variable)
    # assign variable for req content
    markup = req.text
    # parse the content on the page
    soup = BeautifulSoup(markup, 'html.parser')
    # find all paragraph elements that contain [citation needed]
    citation_tags = soup.find_all('sup', {'class': 'noprint Inline-Template Template-Fact'})
    # Assign empty string
    report = ''
    # extract relevant passage and format the report string
    for tag in citation_tags:
        # Extract parent element and its contents
        parent_tag = tag.find_parent()
        passage = parent_tag.get_text().strip()
        report += f'Citation needed for: {passage} [citation needed]\n\n'
    return report


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))