out_path=data/mary_wiki_nogs

# Merge marytts and wiki lexica
python scripts/sequitur/merge_data.py \
    data/marytts_nogs/lexicon.txt \
    data/wiktionary_nogs/lexicon.txt \
    $out_path/lexicon.txt

#
# Sequitur
#

python scripts/sequitur/split_data.py \
    $out_path/lexicon.txt \
    $out_path/sequitur/splits \
    --train 0.7 \
    --test 0.05

scripts/sequitur/train.sh \
    $out_path/sequitur/splits/train.txt \
    $out_path/sequitur/splits/test.txt \
    $out_path/sequitur

# Test wiktionary and marytts
scripts/sequitur/eval.sh \
    $out_path/sequitur/models/model_8 \
    data/wiktionary_nogs/sequitur/splits/test.txt \
    $out_path/sequitur/eval_logs/eval_model_8_wiktionary.txt

scripts/sequitur/eval.sh \
    $out_path/sequitur/models/model_8 \
    data/marytts_nogs/sequitur/splits/test.txt \
    $out_path/sequitur/eval_logs/eval_model_8_marytts.txt
