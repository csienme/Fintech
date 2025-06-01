#export CUDA_VISIBLE_DEVICES=0

model_name=TimeMixer

seq_len=32
pred_len=1
e_layers=4
down_sampling_layers=2
down_sampling_window=2
learning_rate=0.001
d_model=16
d_ff=32
batch_size=32
train_epochs=20
patience=10





python -u run.py \
  --use_ckpt 1 \
  --ckpt_path checkpoints/stock_forecast_stock_32_1_test1_no_DRIP_TimeMixer_MultipleStock_dsl2_lr0.001_sl32_pl1_dm16_nh8_el4_dl1_df32_fc3_ebtimeF_dtTrue_Exp_0/checkpoint.pth \
  --enable_DRIP 1 \
  --num_stock  168 \
  --comment on_NASDAQ100_for_retrain\
  --task_name stock_forecast_DRIP\
  --is_training 1 \
  --root_path ../NASDAQ_split \
  --data_path ''\
  --model_id stock_$seq_len'_'$pred_len'_'test1 \
  --model $model_name \
  --data MultipleStockDRIP\
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
