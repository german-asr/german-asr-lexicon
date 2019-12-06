import os
import json

import click
import pyphony


@click.group()
def run():
    pass


@run.command('convert')
@click.argument('ipa_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
def convert(ipa_path, output_path):
    """
    Convert ipa to marytts.

    Ignore symbols are defined using the error list (find_errors).
    The ones that have no influence are ignored.
    For errors with only a few occurences, the words are deleted.
    """
    if not os.path.isfile(output_path):
        print('Convert Wiktionary IPA to MaryTTS alphabet')
        ipa = pyphony.Alphabet.ipa()
        in_lex = pyphony.Lexicon.load(
            ipa_path,
            word_sep=' ',
            token_sep='',
            alphabet=ipa
        )

        ipa_to_mtts = pyphony.Converter.ipa_to_marytts_de()
        out_lex = ipa_to_mtts.convert_lexicon(
            in_lex,
            strict=True,
            ignore_symbols=[
                chr(int('0329', 16)),  # "̩"
                chr(int('032f', 16)),  # "̯",
                chr(int('02cc', 16)),  # "ˌ",
            ],
            ignore_unmappable_words=True,
            return_errors=False
        )

        out_lex.save(output_path, word_sep=' ', token_sep='')
    else:
        print('Wiktionary already converted to MaryTTS alphabet')


@run.command('find-errors')
@click.argument('ipa_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
def find_errors(ipa_path, output_path):
    if not os.path.isfile(output_path):
        print('Convert Wiktionary IPA to MaryTTS alphabet to find errors')
        ipa = pyphony.Alphabet.ipa()
        in_lex = pyphony.Lexicon.load(
            ipa_path,
            word_sep=' ',
            token_sep='',
            alphabet=ipa
        )

        ipa_to_mtts = pyphony.Converter.ipa_to_marytts_de()
        out_lex, errors = ipa_to_mtts.convert_lexicon(
            in_lex,
            strict=False,
            return_errors=True
        )

        with open(output_path, 'w') as f:
            json.dump(errors, f, ensure_ascii=False)
    else:
        print('Errors of converion already extracted')


if __name__ == '__main__':
    run()
