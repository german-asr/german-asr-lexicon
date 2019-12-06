out_path=data/wiktionary

#
# Download / Clean
#

# Wiktionary
dump_path=$out_path/dump
raw_path=$out_path/raw.txt
ipa_path=$out_path/ipa.txt
errors_path=$out_path/conversion_errors.txt
marytts_path=$out_path/lexicon.txt

scripts/wiktionary/download_dump.sh $dump_path
python scripts/wiktionary/extract_lexicon.py $dump_path $raw_path
python scripts/wiktionary/parse_to_ipa.py $raw_path $ipa_path
python scripts/wiktionary/to_marytts.py find-errors $ipa_path $errors_path
python scripts/wiktionary/to_marytts.py convert $ipa_path $marytts_path

#
#   Sequitur
#

python scripts/sequitur/split_data.py \
    $out_path/lexicon.txt \
    $out_path/sequitur/splits \
    --train 0.8

scripts/sequitur/train.sh \
    $out_path/sequitur/splits/train.txt \
    $out_path/sequitur/splits/test.txt \
    $out_path/sequitur

# Cross testing on marytts test split
scripts/sequitur/eval.sh \
    $out_path/sequitur/models/model_8 \
    data/marytts/sequitur/splits/test.txt \
    $out_path/sequitur/eval_logs/eval_model_8_marytts.txt
