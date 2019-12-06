"""
Reads the raw lexicon from wiktionary dump.
Parses it using IPA Alphabet and ignores the given symbols.

* Ensures that only IPA Symbols are in it
* Fails if there are unknown symbols
* Unknown symbols can be added to the "ignore_symbols",
  if the entries are ok otherwise

"""
import os

import click
import pyphony


@click.command()
@click.argument('raw_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
def run(raw_path, output_path):
    if not os.path.isfile(output_path):
        print('Parse wiktionary raw to ipa')
        # Additional symbols to ignore
        # that are in wiktionary transcriptions
        # but not in IPA
        ignore_symbols = [
            '(',
            ')',
            chr(int('030d', 16)),
            chr(int('0311', 16)),
            chr(int('0342', 16)),
            chr(int('203f', 16)),
            chr(int('0131', 16)),
            chr(int('0323', 16)),
        ]

        abc = pyphony.Alphabet.ipa()
        abc.ignore_symbols.extend(ignore_symbols)
        lex = pyphony.Lexicon.load(
            raw_path,
            word_sep=' ',
            token_sep='',
            alphabet=abc
        )

        lex.save(output_path, word_sep=' ', token_sep='')
    else:
        print('Wiktionary IPA lexicon already exists')


if __name__ == '__main__':
    run()
