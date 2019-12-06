trainlex=$1
testlex=$2
outpath=$3

model_path=$outpath/models
train_log_path=$outpath/train_logs
eval_log_path=$outpath/eval_logs

mkdir -p $model_path
mkdir -p $train_log_path
mkdir -p $eval_log_path

if [[ ! -f $model_path/model_1 ]]; then
    g2p.py \
        --train $trainlex \
        --devel 5% \
        --write-model $model_path/model_1 | tee $train_log_path/model_1.txt

    g2p.py \
        --model $model_path/model_1 \
        --test $testlex | tee $eval_log_path/model_1.txt
fi

for i in 2 3 4 5 6 7 8; do
    if [[ ! -f $model_path/model_${i} ]]; then
        g2p.py \
            --model $model_path/model_$((i-1)) \
            --ramp-up \
            --train $trainlex \
            --devel 5% \
            --write-model $model_path/model_${i} | tee $train_log_path/model_${i}.txt

        g2p.py \
            --model $model_path/model_${i} \
            --test $testlex | tee $eval_log_path/model_${i}.txt
    fi
done
