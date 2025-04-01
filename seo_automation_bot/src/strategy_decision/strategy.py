import logging
import pandas as pd
from typing import Dict, List

class SEOStrategy:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate(self, domain_data: Dict) -> List[Dict]:
        """Generate SEO recommendations based on crawled data"""
        try:
            self.logger.info("Generating SEO strategy recommendations")
            
            recommendations = []
            
            # Check for missing title
            if not domain_data.get('title'):
                recommendations.append({
                    'type': 'critical',
                    'message': 'Missing page title',
                    'action': 'Add a descriptive title tag (50-60 characters)'
                })
            
            # Check for missing meta description
            if not domain_data.get('meta_description'):
                recommendations.append({
                    'type': 'important',
                    'message': 'Missing meta description',
                    'action': 'Add a compelling meta description (150-160 chars)'
                })
            
            # Analyze headers structure
            headers = domain_data.get('headers', {})
            if not headers.get('h1'):
                recommendations.append({
                    'type': 'critical',
                    'message': 'Missing H1 tag',
                    'action': 'Add a single, descriptive H1 tag'
                })
            
            # Check for multiple H1 tags
            if headers.get('h1') and len(headers['h1']) > 1:
                recommendations.append({
                    'type': 'warning',
                    'message': 'Multiple H1 tags found',
                    'action': 'Consolidate to a single H1 tag per page'
                })
            
            # Analyze internal links
            links = domain_data.get('links', [])
            if not links:
                recommendations.append({
                    'type': 'warning',
                    'message': 'No internal links found',
                    'action': 'Add relevant internal links to improve site structure'
                })
            
            return recommendations
            
        except Exception as e:
            self.logger.error(f"Strategy generation failed: {str(e)}")
            raise