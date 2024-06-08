from pegasus.pegasus import Pegasus

pegasus = Pegasus(
    base_url="https://docs.eraser.io/docs/what-is-eraser",
    output_dir="eraser_docs",
    exclude_selectors=['header', 'footer', 'nav', 'aside', '.sidebar', '.header', '.footer', '.navigation', '.breadcrumbs'],
    include_domain="docs.eraser.io",
    exclude_keywords=["login"]
)
pegasus.run()