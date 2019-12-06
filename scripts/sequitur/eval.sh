model_path=$1
test_path=$2
log_path=$3

g2p.py \
    --model $model_path \
    --test $test_path | tee $log_path
