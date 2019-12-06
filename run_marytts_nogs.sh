out_path=data/marytts_nogs

# Remove glotal stops and primary stresses
python scripts/sequitur/remove.py \
    data/marytts/lexicon.txt \
    $out_path/lexicon.txt \
    --glotal-stop \
    --stresses

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

# Cross testing on wiktionary_nogs test split
scripts/sequitur/eval.sh \
    $out_path/sequitur/models/model_7 \
    data/wiktionary_nogs/sequitur/splits/test.txt \
    $out_path/sequitur/eval_logs/eval_model_7_wiktionary.txt
