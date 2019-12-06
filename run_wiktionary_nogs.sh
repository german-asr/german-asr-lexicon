out_path=data/wiktionary_nogs

# Remove glotal stops and primary stresses
python scripts/sequitur/remove.py \
    data/wiktionary/lexicon.txt \
    $out_path/lexicon.txt \
    --glotal-stop \
    --stresses

#
#   Sequitur
#

python scripts/sequitur/split_data.py \
    $out_path/lexicon.txt \
    $out_path/sequitur/splits \
    --train 0.09
    --test 0.01

scripts/sequitur/train.sh \
    $out_path/sequitur/splits/train.txt \
    $out_path/sequitur/splits/test.txt \
    $out_path/sequitur

# Cross testing on marytts_nogs test split
scripts/sequitur/eval.sh \
    $out_path/sequitur/models/model_7 \
    data/marytts_nogs/sequitur/splits/test.txt \
    $out_path/sequitur/eval_logs/eval_model_7_marytts.txt
