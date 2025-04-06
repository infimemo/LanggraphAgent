from typing import List, Dict, Any, Optional

__version__ = "0.1.0"

from .graphSetup import graph
from .mytools import tools
from .functions.charts import *
from .functions.compare_companies import *
from .functions.data_standarization import *
from .functions.economics import *
from .functions.fetch_data import *
from .functions.find_companies import *
from .functions.market_analysis_tools import *
from .functions.metrics_tables import *
from .functions.persona_agents import *
from .functions.portfolio_tools import *
from .functions.prompts import *
from .functions.single_stock_analysis import *
from .functions.single_country_analysis import *
from .functions.single_stock_analysis import *

__all__ = [
    "graph",
    "tools",
    ##CHARTS.PY
    'chart_standarized_price_evo',
    'portfolio_exposure_to_external_factors_chart',
    'portfolio_investment_style_exposure_chart',
    'portfolio_sector_chart',
    'portfolio_pnl_chart',

    ## COMPARE_COMPANIES.PY
    'table_metrics_of_companies'
    'compare_stocks_main_characteristics',

    ##DATA STANDARIZATION.PY
    'standardize_prices_to_compare_stock_prices',

    ## ECONOMICS.PY
    'get_economic_calendar',

    ## FETCH_DATA.PY
    'fetch_etf_price_correlations',
    'fetch_etf_data',
    'fetch_data_from_csv',
    'fetch_data_portfolio_optimization',
    'fetch_data_portfolio_report',

    ## FIND_COMPANIES.PY
    'get_symbol_by_description',
    'select_companies_with_metadata',
    'find_suitable_stock',
    '_get_signal_scores',

    ## MARKET_ANALYSIS_TOOLS
    'make_market_brief',
    'get_last_week_movers',
    'get_etf_performance_and_narratives',

    ##METRIC_TABLES
    'moving_avg_days',
    'sortino_ratio',
    'sterling_ratio',
    
    ##PERSONA_AGENTS.PY
    'persona_portfolio_manager',
    'persona_strategist',
    'persona_analyst',
    'persona_special_topic_analyst'
    
    ##PORTFOLIO_TOOLS.PY
    'optimize_portfolio',
    'orthogonalize',
    'portbuilder',
    'calculate_portfolio_stats',
    'analyze_portfolio_and_append_charts'
    
    ##PROMPTS.PY
    'prompt_with_instructions_to_build_portfolio',
    'prompt_for_interpretation_of_financial_metrics',
    
    ##SINGLE COUNTRY ANALYSIS
    'scrape_vti_data_for_pe_ratios',
    'max_drawdown',
    'briefing_on_country_sector_commodity_or_crypto',
    
    ##SINGLE_STOCK_ANALYSIS.PY
    'get_company_summary',
    'company_factor_chart',
    'company_chart_of_price_vs_fundamentals'
]


