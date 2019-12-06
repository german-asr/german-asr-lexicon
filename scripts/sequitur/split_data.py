import os
import random

import click
import pyphony


@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path',  type=click.Path())
@click.option('--train', type=float, default=0.9)
@click.option('--test', type=float, default=None)
def run(input_path, output_path, train, test):
    train_path = os.path.join(output_path, 'train.txt')
    test_path = os.path.join(output_path, 'test.txt')

    if not os.path.isfile(train_path) or not os.path.isfile(test_path):
        print('Split data')
        os.makedirs(output_path, exist_ok=True)
        abc = pyphony.Alphabet.marytts_de()
        lex = pyphony.Lexicon.load(
            input_path,
            word_sep=' ',
            token_sep='',
            alphabet=abc
        )

        full = list(lex.entries.keys())
        random.shuffle(full)

        train_size = int(len(full) * train)
        train = full[:train_size]

        if test is None:
            test = full[train_size:]
        else:
            test_size = int(len(full) * test)
            test = full[train_size:train_size+test_size]

        train_entries = {k: lex.entries[k] for k in train}
        train_lex = pyphony.Lexicon(train_entries)
        train_lex.save(train_path)

        test_entries = {k: lex.entries[k] for k in test}
        test_lex = pyphony.Lexicon(test_entries)
        test_lex.save(test_path)
    else:
        print('Data already splitted')


if __name__ == '__main__':
    run()
