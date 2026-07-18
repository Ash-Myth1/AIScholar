"""
Reusable UI components.
"""

def get_hero_html() -> str:
    """Returns the raw HTML for the hero landing section."""
    return """
    <div class="hero-container">
        <div style="font-size: 56px; margin-bottom: 1rem;">🔍</div>
        <h1 class="hero-title">AIScholar</h1>
        <p class="hero-subtitle">Offline AI Research Assistant. Private. Fast. Runs on your machine.</p>
        <div class="badge-container">
            <div class="badge">🔒 Private</div>
            <div class="badge">⚡ Fast</div>
            <div class="badge">📄 Research Ready</div>
        </div>
        <div style="width: 100%; max-width: 800px; text-align: center; margin-bottom: 2.5rem;">
            <p style="color: var(--text-secondary); font-size: 15px;">Upload your first research paper from the sidebar to start asking intelligent questions.</p>
        </div>
        <div class="suggestions-container">
            <div class="suggestion-card">
                <div class="suggestion-title">Summarize this paper</div>
                <div class="suggestion-desc">Get a high-level overview of the main findings and abstract.</div>
            </div>
            <div class="suggestion-card">
                <div class="suggestion-title">Explain methodology</div>
                <div class="suggestion-desc">Dive deep into the experimental setup and procedures.</div>
            </div>
            <div class="suggestion-card">
                <div class="suggestion-title">Compare findings</div>
                <div class="suggestion-desc">Analyze results across different sections of the document.</div>
            </div>
        </div>
    </div>
    """

def get_success_card_html() -> str:
    """Returns the raw HTML for the library ready success card."""
    return """
    <div class="success-card">
        <p class="success-title">✓ Knowledge Base Ready</p>
        <p style="font-size: 12px;">Your research documents are successfully indexed and ready for querying.</p>
    </div>
    """

def get_library_card_html(filename: str, pages: int, chunks: int) -> str:
    """Returns the raw HTML for a single document library card."""
    return f"""
    <div class="library-card">
        <div class="library-card-icon">📄</div>
        <div>
            <div style="font-size: 13px; font-weight: 500; color: var(--text-primary);">{filename}</div>
            <div style="font-size: 12px; color: var(--text-secondary); margin-top: 2px;">{pages} Pages • {chunks} Chunks</div>
        </div>
    </div>
    """

def get_source_details_html(index: int, source_file: str, page: str, safe_content: str) -> str:
    """Returns the raw HTML for a citation details block."""
    return f"""
    <details class="custom-source-details">
        <summary class="custom-source-summary">
            <div class="source-summary-left">
                <span class="source-icon">📑</span> Source {index}: {source_file}
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
                <span class="page-badge">Page {page}</span>
                <svg class="chevron-icon" viewBox="0 0 24 24">
                    <path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z"></path>
                </svg>
            </div>
        </summary>
        <div class="source-card">{safe_content}</div>
    </details>
    """
