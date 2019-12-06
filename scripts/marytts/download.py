import os

import click
import requests
import spoteno

URL = ('https://raw.githubusercontent.com/marytts/'
       'marytts-lexicon-de/master/modules/de/lexicon/de.txt')

normalizer = spoteno.Normalizer.de()


@click.command()
@click.argument('output_path', type=click.Path())
def run(output_path):
    if not os.path.isfile(output_path):
        print('Download and clean MaryTTS lexicon')
        res = requests.get(URL)
        content = res.content.decode('utf-8')
        lines = [l.strip() for l in content.split('\n')]
        cleaned = []

        for l in lines:
            if l.startswith('#'):
                cleaned.append(l)
            else:
                parts = l.split(' ', maxsplit=1)
                if len(parts) > 1 and len(parts[1]) > 0:
                    word = normalize_and_filter(parts[0])

                    if word is not None:
                        cleaned.append('{} {}'.format(word, parts[1]))

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(cleaned))
    else:
        print('MaryTTS Lexicon already downloaded')


def normalize_and_filter(word):
    result = normalizer.normalize(word)

    if len(result) >= len(word) and ' ' not in result:
        return result

    return None


if __name__ == '__main__':
    run()
