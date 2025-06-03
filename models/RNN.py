import torch
import torch.nn as nn

class Model(nn.Module):
    def __init__(self, args):
        super(Model, self).__init__()
        self.rnn = nn.RNN(
            input_size=args.enc_in,
            hidden_size=64,
            num_layers=1,
            batch_first=True
        )
        self.proj = nn.Linear(64, args.c_out)

    def forward(self, x_enc, x_mark_enc, dec_inp=None, x_mark_dec=None):
        # x_enc: [B, T, C]
        rnn_out, _ = self.rnn(x_enc)  # [B, T, 64]
        out = self.proj(rnn_out)      # [B, T, c_out]
        return out
