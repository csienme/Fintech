#export CUDA_VISIBLE_DEVICES=0

model_name=TimeMixer

seq_len=32
pred_len=1
e_layers=4
down_sampling_layers=2
down_sampling_window=2
learning_rate=0.01
d_model=16
d_ff=16
batch_size=64 #0208 is 32
train_epochs=25
patience=10



python -u run.py \
  --enable_DRIP 1 \
  --num_stock  168 \
  --comment future_return_0212\
  --task_name stock_forecast_DRIP\
  --is_training 1 \
  --root_path ../NASDAQ_split_dataset \
  --data_path ''\
  --model_id morning \
  --model $model_name \
  --data MultipleStockDRIP\
  --features MS \
  --target future_return\
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
