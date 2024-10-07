# tests/test_news_scraper.py

import pytest
from app.news_summarizer import scrape_news

def test_scrape_news(monkeypatch):
    """Test the scrape_news function."""

    # Mock the URL for testing
    url = 'http://example.com/news'

    # Sample HTML content to mimic the response from the website
    sample_html = """
    <html>
        <body>
            <h2>Breaking News: Test News 1</h2>
            <h2>Latest Updates: Test News 2</h2>
            <h2>Insights: Test News 3</h2>
        </body>
    </html>
    """

    # Mock the requests.get method to return the sample HTML
    class MockResponse:
        @staticmethod
        def get(url):
            return type('obj', (object,), {'text': sample_html})

    monkeypatch.setattr('requests.get', MockResponse.get)

    # Call the scrape_news function
    headlines = scrape_news(url)

    # Expected headlines based on the sample HTML
    expected_headlines = [
        'Breaking News: Test News 1',
        'Latest Updates: Test News 2',
        'Insights: Test News 3',
    ]

    # Assert that the scraped headlines match the expected headlines
    assert headlines == expected_headlines
