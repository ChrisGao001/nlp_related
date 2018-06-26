#!/bin/bash
set -x

tool_path=$(cd `dirname $0`;pwd)
cd $tool_path

CRF_TRAIN=${tool_path}/tool/bin/crf_learn
CRF_TEST=${tool_path}/tool/bin/crf_test
TEMPLATE=${tool_path}/conf/template

train_org_file=${tool_path}/data/pku_training.utf8
test_org_file=${tool_path}/data/pku_test.utf8

train_file=${tool_path}/data/pku_train.txt
test_file=${tool_path}/data/pku_test.txt
test_out=${tool_path}/pku_test.out

#python gen_train_sample.py $train_org_file ${train_file}
#python gen_train_sample.py $test_org_file ${test_file}

$CRF_TRAIN -f 3 -c 4.0 -m 200 $TEMPLATE $train_file model -t
$CRF_TEST -m model $test_file > $test_out




