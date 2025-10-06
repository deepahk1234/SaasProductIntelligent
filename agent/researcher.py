import json

def run_research(prompt):
    """
    This function simulates the entire research process.
    """
    # Phase 1: Discovery & Data Collection (Simulated)
    # In a real implementation, this would involve API calls to X, Google, etc.
    # For now, we use a static list of simulated "found" products.
    simulated_products = [
        {
            "productName": "DevTools AI",
            "url": "https://devtools.ai",
            "founder": "@dev_founder",
            "source": "https://twitter.com/dev_founder/status/12345",
            "description": "An AI-powered code completion tool that integrates with VS Code.",
            "revenue_mrr": 5000,
            "date_reported": "2025-10-01",
            "founder_statements": ["organic growth", "no paid ads", "built in a weekend"],
            "team_size": 1,
            "tech_stack": "Next.js, Python",
            "profitability_claim": "profitable"
        },
        {
            "productName": "ContentGenius",
            "url": "https://contentgenius.io",
            "founder": "jane_doe_content",
            "source": "https://indiehackers.com/product/contentgenius/milestone/123",
            "description": "A tool to automatically generate blog posts from a simple prompt.",
            "revenue_mrr": 12000,
            "date_reported": "2025-09-15",
            "founder_statements": ["word of mouth", "viral on X"],
            "team_size": 2,
            "tech_stack": "Rails, Vue.js",
            "profitability_claim": "bootstrapped and profitable"
        },
        {
            "productName": "DataViz Pro",
            "url": "https://dataviz.pro",
            "founder": "dataviz_corp",
            "source": "https://techcrunch.com/dataviz-funding",
            "description": "Enterprise-grade data visualization platform.",
            "revenue_mrr": 150000,
            "date_reported": "2025-08-20",
            "founder_statements": ["spent $50k on ads", "marketing team of 5"],
            "team_size": 25,
            "tech_stack": "Java, k8s, 15 microservices",
            "profitability_claim": "burning runway, need funding"
        },
        {
            "productName": "QuickNotes",
            "url": "https://quicknotes.app",
            "founder": "@quicknoter",
            "source": "https://twitter.com/quicknoter/status/54321",
            "description": "A simple note-taking app.",
            "revenue_mrr": 800,
            "date_reported": "2025-09-30",
            "founder_statements": ["organic growth"],
            "team_size": 1,
            "tech_stack": "Django",
            "profitability_claim": "profitable"
        },
        {
            "productName": "FutureSaaS",
            "url": "https://futuresaas.com",
            "founder": "visionary_founder",
            "source": "https://futuresaas.com/blog/announcement",
            "description": "A revolutionary new platform.",
            "revenue_mrr": 0, # Fails proven demand
            "date_reported": "2025-10-05",
            "founder_statements": ["about to launch"],
            "team_size": 3,
            "tech_stack": "Elixir",
            "profitability_claim": "pre-revenue"
        }
    ]

    # Phase 2: Validation Through Four Filters
    validated_opportunities = []
    near_misses = []
    red_flags_observed = []

    for product in simulated_products:
        passes, reasons = apply_filters(product)
        if passes:
            validated_opportunities.append(product)
        else:
            if len(reasons) == 1: # Met 3/4 filters
                near_misses.append(f"Product '{product['productName']}' failed the '{reasons[0]}' filter.")
            else: # Failed multiple filters
                 red_flags_observed.append(f"Product '{product['productName']}' failed validation on: {', '.join(reasons)}.")


    # Phase 3: Data Extraction (will be part of report generation)
    # Phase 4: Report Generation
    report = generate_report(validated_opportunities, near_misses, red_flags_observed)

    return report

def apply_filters(product):
    reasons_failed = []

    # Filter 1: Low Marketing Spend
    if not (any(s in product["founder_statements"] for s in ["organic growth", "no paid ads", "word of mouth", "viral on X"])):
        reasons_failed.append("Low Marketing Spend")
    if any(s in product["founder_statements"] for s in ["spent $", "marketing team"]):
        reasons_failed.append("Low Marketing Spend")

    # Filter 2: Proven Demand
    if product["revenue_mrr"] < 1000:
        reasons_failed.append("Proven Demand")

    # Filter 3: Simple to Maintain
    if product["team_size"] > 2 or "microservices" in product["tech_stack"]:
        reasons_failed.append("Simple to Maintain")

    # Filter 4: Profitability
    if not any(s in product["profitability_claim"] for s in ["profitable", "default alive"]):
         reasons_failed.append("Profitability")

    # Using set to remove duplicate reasons if a product fails a filter in multiple ways
    unique_reasons = sorted(list(set(reasons_failed)))
    return len(unique_reasons) == 0, unique_reasons


def generate_report(validated_opportunities, near_misses, red_flags_observed):
    """
    Generates the final JSON report from the validated data.
    """

    def format_opportunity(product):
        return {
            "productName": product["productName"],
            "mrr": product["revenue_mrr"],
            "description": product["description"],
            "revenue": {
                "metrics": f"${product['revenue_mrr']:,} MRR",
                "sourceLink": product["source"]
            },
            "marketing": ", ".join([s for s in product["founder_statements"] if s in ["organic growth", "no paid ads", "word of mouth", "viral on X"]]),
            "techTeam": f"{product['team_size']}-person team, Tech: {product['tech_stack']}",
            "whyItWorks": "Inferred from description and simplicity.", # Placeholder
            "source": product["source"]
        }

    report = {
        "reportTitle": "SaaS Product Intelligence Report",
        "weekOf": "October 6, 2025 - October 12, 2025",
        "executiveSummary": "This week's research uncovered several promising SaaS products with strong organic growth, particularly in the developer tools and AI-powered content creation niches.",
        "validatedOpportunities": [format_opportunity(p) for p in validated_opportunities],
        "emergingPatterns": [
            "AI-wrappers for existing APIs continue to be a strong trend.",
            "Developer tools with a focus on productivity are finding paying customers quickly.",
            "Products with a strong community-led growth model are succeeding without ad spend."
        ],
        "nearMisses": near_misses,
        "redFlagsObserved": red_flags_observed,
        "deepDives": [
            "The niche of 'AI-powered documentation generators' seems promising and warrants further investigation."
        ],
        "marketIntelligence": {
            "trendingHashtags": ["#buildinpublic", "#ai", "#saas"],
            "activeCommunities": ["Indie Hackers", "r/SaaS"],
            "keyVoices": ["@levelsio", "@dvassallo"]
        }
    }
    return report