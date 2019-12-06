out_path=data/marytts

#
# Download / Clean
#

python scripts/marytts/download.py $out_path/lexicon.txt

#
#   Sequitur
#

python scripts/sequitur/split_data.py \
    $out_path/lexicon.txt \
    $out_path/sequitur/splits \
    --train 0.9

scripts/sequitur/train.sh \
    $out_path/sequitur/splits/train.txt \
    $out_path/sequitur/splits/test.txt \
    $out_path/sequitur

# Cross testing on wiktionary test split
scripts/sequitur/eval.sh \
    $out_path/sequitur/models/model_7 \
    data/wiktionary/sequitur/splits/test.txt \
    $out_path/sequitur/eval_logs/eval_model_7_wiktionary.txt
