"""
=============================================================================
Project: Global Fuel Analytics — Flask Web Application
Title: Global Fuel Prices and Taxation Trends: A Comprehensive Analysis
Author: Mahima / Data Analytics Team
Description: A responsive Flask web application integrating Tableau Public
             Dashboards and Tableau Stories for exploring global fuel prices,
             taxation patterns, regional variations, and economic indicators.
=============================================================================
"""

import os
from flask import Flask, render_template, request, flash, redirect, url_for

# Initialize Flask application
app = Flask(__name__)
# Secret key for session/flash messages (configurable via environment variable)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fuel-analytics-secret-key-2026')

# =============================================================================
# TABLEAU PUBLIC CONFIGURATION
# =============================================================================
# Connected with Mahima's official published Tableau Public visualization:
# Link: https://public.tableau.com/shared/BWMJZ7N7Z?:display_count=n&:origin=viz_share_link
# =============================================================================

TABLEAU_CONFIG = {
    # Tableau Public Shared URL provided by user
    "DASHBOARD_URL": os.environ.get(
        "TABLEAU_DASHBOARD_URL",
        "https://public.tableau.com/shared/BWMJZ7N7Z?:display_count=n&:origin=viz_share_link"
    ),
    "STORY_URL": os.environ.get(
        "TABLEAU_STORY_URL",
        "https://public.tableau.com/shared/BWMJZ7N7Z?:display_count=n&:origin=viz_share_link"
    ),
    "PROJECT_TITLE": "Global Fuel Prices and Taxation Trends",
    "SUBTITLE": "A Comprehensive Visual Analytics Platform"
}


def get_tableau_embed_url(url: str) -> str:
    """
    Format any Tableau Public URL (standard /views/ or /shared/) into
    a clean embeddable URL with proper query parameters without duplicates.
    """
    if not url:
        return ""
    # Strip existing query string
    base_url = url.split('?')[0].rstrip('/')
    return f"{base_url}?:embed=yes&:showVizHome=no&:toolbar=yes"


@app.context_processor
def inject_global_config():
    """Make tableau config, embed URLs and project metadata available across all Jinja2 templates."""
    dashboard_raw = TABLEAU_CONFIG["DASHBOARD_URL"]
    story_raw = TABLEAU_CONFIG["STORY_URL"]
    return dict(
        config=TABLEAU_CONFIG,
        dashboard_url=dashboard_raw,
        dashboard_embed_url=get_tableau_embed_url(dashboard_raw),
        story_url=story_raw,
        story_embed_url=get_tableau_embed_url(story_raw)
    )


# =============================================================================
# FLASK APPLICATION ROUTES
# =============================================================================

@app.route('/')
def home():
    """Home Page: Hero section, project objectives, fuel summary cards, and quick links."""
    return render_template('index.html', active_page='home')


@app.route('/dashboard')
def dashboard():
    """Interactive Dashboard Page: Embeds the Tableau Public dashboard."""
    raw_url = TABLEAU_CONFIG["DASHBOARD_URL"]
    embed_url = get_tableau_embed_url(raw_url)
    return render_template(
        'dashboard.html',
        active_page='dashboard',
        dashboard_url=raw_url,
        dashboard_embed_url=embed_url
    )


@app.route('/story')
def story():
    """Tableau Story Page: Embeds the Tableau Story with narrative insights and structure."""
    raw_url = TABLEAU_CONFIG["STORY_URL"]
    embed_url = get_tableau_embed_url(raw_url)
    return render_template(
        'story.html',
        active_page='story',
        story_url=raw_url,
        story_embed_url=embed_url
    )


@app.route('/about')
def about():
    """About Page: Methodology, dataset fields, visualization details, tools, and limitations."""
    # Complete list of 10 dataset fields for transparent display
    dataset_fields = [
        {"name": "Country", "type": "Categorical / Dimension", "desc": "Name of the sovereign nation analyzed"},
        {"name": "Date", "type": "Date / Temporal", "desc": "Observation period / timestamp for historical tracking"},
        {"name": "Income Level", "type": "Categorical / Dimension", "desc": "World Bank classification (High, Upper Middle, Lower Middle, Low)"},
        {"name": "Region", "type": "Categorical / Geographic", "desc": "Geographic grouping (Europe, Americas, Asia-Pacific, Africa, etc.)"},
        {"name": "Subsidy Level", "type": "Categorical / Policy", "desc": "Extent of government retail subsidy support"},
        {"name": "Brent Crude USD", "type": "Numeric / Measure ($)", "desc": "International crude oil benchmark price per barrel in USD"},
        {"name": "Diesel USD Liter", "type": "Numeric / Measure ($)", "desc": "Retail price of automotive diesel per liter in USD"},
        {"name": "LPG USD Liter", "type": "Numeric / Measure ($)", "desc": "Retail price of Liquefied Petroleum Gas per liter in USD"},
        {"name": "Petrol USD Liter", "type": "Numeric / Measure ($)", "desc": "Retail price of motor petrol (gasoline) per liter in USD"},
        {"name": "Tax Percentage", "type": "Numeric / Measure (%)", "desc": "Effective fiscal tax share or duty percentage levied"}
    ]
    return render_template('about.html', active_page='about', dataset_fields=dataset_fields)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact / Feedback Page: Form handling and project inquiries."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash("Please complete all required fields.", "danger")
            return redirect(url_for('contact'))

        # In production, message can be logged, emailed, or stored in a service.
        flash(f"Thank you, {name}! Your message has been received.", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html', active_page='contact')


# =============================================================================
# ERROR HANDLING
# =============================================================================

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 handler for missing routes."""
    return render_template('404.html', active_page='404'), 404


@app.errorhandler(500)
def internal_server_error(error):
    """Custom 500 handler for application runtime errors."""
    return render_template('500.html', active_page='500'), 500


# =============================================================================
# LOCAL DEVELOPMENT ENTRY POINT
# =============================================================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
