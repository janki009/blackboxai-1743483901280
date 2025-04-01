import logging
from src.domain_analysis.crawler import DomainCrawler
from src.strategy_decision.strategy import SEOStrategy
from src.execution.selenium_executor import SEOExecutor
from config.config import load_config

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='seo_automation_bot.log'
    )
    return logging.getLogger(__name__)

def main():
    logger = setup_logging()
    config = load_config()
    
    try:
        # Domain Analysis
        crawler = DomainCrawler(config)
        domain_data = crawler.analyze(config['TARGET_URL'])
        
        # Strategy Decision
        strategy = SEOStrategy()
        recommendations = strategy.generate(domain_data)
        
        # Execution
        executor = SEOExecutor(config)
        executor.implement(recommendations)
        
    except Exception as e:
        logger.error(f"SEO Automation failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()