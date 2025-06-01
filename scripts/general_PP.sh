#export CUDA_VISIBLE_DEVICES=0

model_name=TimeMixerPP

seq_len=32
pred_len=1
e_layers=3
down_sampling_layers=3
down_sampling_window=2
learning_rate=0.01
d_model=16
d_ff=32
batch_size=32
train_epochs=50
patience=10




python -u run_PP.py \
  --comment clamp_loss=10\
  --task_name stock_forecast \
  --is_training 1 \
  --root_path ../NASDAQ_split \
  --data_path ''\
  --model_id $seq_len'_'$pred_len \
  --model $model_name \
  --data MultipleStock \
  --features MS \
  --target close\
  --seq_len $seq_len \
  --label_len 0 \
  --pred_len $pred_len \
  --e_layers $e_layers \
  --d_layers 1 \
  --factor 3 \
  --enc_in 6 \
  --dec_in 6 \
  --c_out 6 \
  --des 'Exp' \
  --itr 1 \
  --d_model $d_model \
  --d_ff $d_ff \
  --batch_size $batch_size \
  --learning_rate $learning_rate \
  --train_epochs $train_epochs \
  --patience $patience \
  --down_sampling_layers $down_sampling_layers \
  --down_sampling_method avg \
  --down_sampling_window $down_sampling_window
