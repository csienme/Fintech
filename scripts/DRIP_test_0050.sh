#export CUDA_VISIBLE_DEVICES=0

model_name=TimeMixer

seq_len=32
pred_len=1
e_layers=4
down_sampling_layers=2
down_sampling_window=2
learning_rate=0.01
d_model=32
d_ff=64
batch_size=32
train_epochs=30
patience=10


TimeMixer/checkpoints/stock_forecast_DRIP_afternoon_future_return_TimeMixer_MultipleStockDRIP_dsl2_lr0.001_sl32_pl1_dm16_nh8_el4_dl1_df16_fc3_ebtimeF_dtTrue_Exp_0/checkpoint.pth

python -u run.py \
  --enable_DRIP 1 \
  --num_stock  104 \
  --comment future_return\
  --task_name stock_forecast_DRIP\
  --is_training 0 \
  --root_path ../分別0050 \
  --data_path ''\
  --model_id afternoon \
  --model $model_name \
  --data TestingData\
  --features MS \
  --target future_return\
  --seq_len $seq_len \
  --label_len 0 \
  --pred_len $pred_len \
  --e_layers $e_layers \
  --d_layers 1 \
  --factor 3 \
  --enc_in 15 \
  --dec_in 15 \
  --c_out 15 \
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
  --down_sampling_window $down_sampling_window\
