import os

import click
from pyphony.parser import wiktionary


@click.command()
@click.argument('dump_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
def run(dump_path, output_path):
    if not os.path.isfile(output_path):
        print('Extract Lexicon from wiktionary dump')
        wp = wiktionary.DeWiktionaryParser()
        lex = wp.parse_xml_dump(dump_path)
        lex.save(output_path)
    else:
        print('Wiktionary Lexicon already extracted')


if __name__ == '__main__':
    run()
