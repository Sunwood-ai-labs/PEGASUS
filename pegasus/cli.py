# pegasus/cli.py
import argparse
from .Pegasus import Pegasus

def main():
    parser = argparse.ArgumentParser(description='Pegasus')
    parser.add_argument('base_url', help='Base URL to start scraping')
    parser.add_argument('output_dir', help='Output directory for markdown files')
    parser.add_argument('--exclude-selectors', nargs='+', help='CSS selectors to exclude')
    parser.add_argument('--include-domain', help='Domain to include in URL matching')
    parser.add_argument('--exclude-keywords', nargs='+', help='Keywords to exclude in URL matching')
    parser.add_argument('--output-extension', default='.md', help='Output file extension (default: .md)')
    parser.add_argument('--dust-size', type=int, default=1000, help='File size threshold for moving to dust folder (default: 1000 bytes)')

    args = parser.parse_args()

    pegasus = Pegasus(
        base_url=args.base_url,
        output_dir=args.output_dir,
        exclude_selectors=args.exclude_selectors,
        include_domain=args.include_domain,
        exclude_keywords=args.exclude_keywords,
        output_extension=args.output_extension,
        dust_size=args.dust_size
    )
    pegasus.run()

if __name__ == '__main__':
    main()