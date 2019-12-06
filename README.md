# Phonetic Lexicon for German ASR
This repository contains scripts to create a phonetic lexicon for german words. Furthermore scripts for training a sequitur G2P model are available. If you want to use the lexicon or g2p model, please check licenses of the datasources in the table below.

## Lexicon
For the lexicon data from two sources are used.

| Name 		| Num. Words | URL 											      |
| ------------- | ---------- | ---------------------------------------------------------------------------------------------- |
| MaryTTS 	| 26199      | [https://github.com/marytts/marytts-lexicon-de](https://github.com/marytts/marytts-lexicon-de) |
| Wiktionary  	| 501179     | [https://dumps.wikimedia.org/dewiktionary](https://dumps.wikimedia.org/dewiktionary)  	      |

The final lexicon is based on both MaryTTS and Wiktionary.
The phone-set (SAMPA) of MaryTTS is used.
But since stress and glotal stops differ highly between both datasources, they were ignored.
The final lexicon is available in the releases.

## G2P
The G2P models are trained using [sequitur](https://github.com/sequitur-g2p/sequitur-g2p).
Training was done using the lexicon mentioned above for 8 iterations.
Models are available in the releases.
