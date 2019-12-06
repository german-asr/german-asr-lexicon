import os
import random

import click
import pyphony


@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path',  type=click.Path())
@click.option('--glotal-stop', is_flag=True)
@click.option('--stresses', is_flag=True)
def run(input_path, output_path, glotal_stop, stresses):
    print('Remove symobls')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    abc = pyphony.Alphabet.marytts_de()
    lex = pyphony.Lexicon.load(
        input_path,
        word_sep=' ',
        token_sep='',
        alphabet=abc
    )

    new_lex = pyphony.Lexicon()

    for word, transcriptions in lex.entries.items():
        for t in transcriptions:
            new_t = list(t)

            if glotal_stop:
                new_t = list(filter(lambda x: x != '?', new_t))

            if stresses:
                new_t = list(filter(lambda x: x != "'", new_t))

            new_lex.add(word, new_t)

    new_lex.save(output_path, word_sep=' ', token_sep='')


if __name__ == '__main__':
    run()
