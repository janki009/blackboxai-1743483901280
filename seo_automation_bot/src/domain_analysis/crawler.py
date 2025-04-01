import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

class DomainCrawler:
    def __init__(self, config):
        self.config = config
        self.base_url = config['TARGET_URL']
        self.timeout = config['REQUEST_TIMEOUT']
        self.logger = logging.getLogger(__name__)

    def analyze(self, url):
        """Analyze a domain URL and return structured SEO data"""
        try:
            self.logger.info(f"Analyzing URL: {url}")
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            return {
                'url': url,
                'title': self._get_title(soup),
                'meta_description': self._get_meta_description(soup),
                'headers': self._get_headers(soup),
                'links': self._get_links(soup),
                'status_code': response.status_code,
                'content_length': len(response.content)
            }
            
        except requests.RequestException as e:
            self.logger.error(f"Failed to analyze {url}: {str(e)}")
            raise

    def _get_title(self, soup):
        """Extract page title"""
        title = soup.find('title')
        return title.text if title else None

    def _get_meta_description(self, soup):
        """Extract meta description"""
        meta = soup.find('meta', attrs={'name': 'description'})
        return meta['content'] if meta else None

    def _get_headers(self, soup):
        """Extract all header tags (h1-h6)"""
        headers = {}
        for i in range(1, 7):
            headers[f'h{i}'] = [h.text for h in soup.find_all(f'h{i}')]
        return headers

    def _get_links(self, soup):
        """Extract and normalize all links"""
        links = set()
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(self.base_url, link['href'])
            if absolute_url.startswith(self.base_url):
                links.add(absolute_url)
        return list(links)