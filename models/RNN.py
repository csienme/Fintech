import torch
import torch.nn as nn

class RNNForecastModel(nn.Module):
    def __init__(self, args):
        super().__init__()

        self.input_norm = nn.LayerNorm(args.enc_in)

        self.lstm = nn.LSTM(
            input_size=args.enc_in,
            hidden_size=128,
            num_layers=2,
            dropout=0.3,
            batch_first=True
        )

        self.dropout = nn.Dropout(0.3)

        self.res_fc = nn.Linear(args.enc_in, 128)
        self.norm = nn.LayerNorm(128)

        self.proj = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 1)
        )

    def forward(self, x_enc, x_mark_enc=None, dec_inp=None, x_mark_dec=None):
        # x_enc: [B, T, C]
        x = self.input_norm(x_enc)

        rnn_out, _ = self.lstm(x)           # [B, T, 128]
        rnn_out = self.dropout(rnn_out)

        last_hidden = rnn_out[:, -1, :]     # 取最後一個時間步
        res = self.res_fc(x[:, -1, :])      # residual shortcut
        out = last_hidden + res
        out = self.norm(out)

        out = self.proj(out)                # 最終輸出 return 預測
        return out
    
Model = RNNForecastModel
