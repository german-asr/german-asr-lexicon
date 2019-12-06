import os
import random

import click
import pyphony


@click.command()
@click.argument('lex_a_path', type=click.Path(exists=True))
@click.argument('lex_b_path', type=click.Path(exists=True))
@click.argument('output_path',  type=click.Path())
def run(lex_a_path, lex_b_path, output_path):
    print('Merge data')
    abc = pyphony.Alphabet.marytts_de()
    lex_a = pyphony.Lexicon.load(
        lex_a_path,
        word_sep=' ',
        token_sep='',
        alphabet=abc
    )
    lex_b = pyphony.Lexicon.load(
        lex_b_path,
        word_sep=' ',
        token_sep='',
        alphabet=abc
    )

    merged = pyphony.Lexicon()

    for word, transcriptions in lex_a.entries.items():
        merged.add(word, transcriptions[0])

    for word, transcriptions in lex_b.entries.items():
        if word not in merged.entries.keys():
            merged.add(word, transcriptions[0])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    merged.save(output_path, word_sep=' ', token_sep='')


if __name__ == '__main__':
    run()
