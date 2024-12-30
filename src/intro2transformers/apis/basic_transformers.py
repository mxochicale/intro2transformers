from math import sqrt

import torch
import torch.nn as nn
import torch.nn.functional as F
from loguru import logger

from transformers import AutoTokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
vocab_size = tokenizer.vocab_size  # will also denote as V
seq_length = 16  # will also denote sequence length as T i.e. "time dimension"
embed_dim = 64  # will also denote as C i.e. "channel dimension"
num_heads = 8
head_dim = embed_dim // num_heads  # will also denote as H

texts = [
    "I love summer",
    "I love tacos",
]
inputs = tokenizer(
    texts,
    return_tensors="pt",
    padding="max_length",
    max_length=seq_length,
    truncation=True,
).input_ids


logger.info(f"Using device: {device}")
logger.info(f"inputs: {inputs}" )
logger.info(f"inputs.shape:  # (B, T) {inputs.shape}" ) 
logger.info(f"vocab_size # V {vocab_size}" ) 

for row in inputs:
    logger.info(tokenizer.convert_ids_to_tokens(row))

token_emb = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embed_dim)
logger.info(f"token_emb.weight.shape # (V, C) {token_emb.weight.shape}")

token_embeddings = token_emb(inputs)
logger.info(f"token_embeddings.shape # (B, T, C) {token_embeddings.shape}")


positional_emb = nn.Embedding(num_embeddings=seq_length, embedding_dim=embed_dim)  # (T, C)
positional_embeddings = positional_emb(torch.arange(start=0, end=seq_length, step=1))
logger.info(f"positional_embeddings.shape # (T, C) {positional_embeddings.shape}")

embeddings = token_embeddings + positional_embeddings
logger.info(f"embeddings.shape # (B, T, C) {embeddings.shape}")

query = nn.Linear(in_features=embed_dim, out_features=head_dim, bias=False)
key = nn.Linear(in_features=embed_dim, out_features=head_dim, bias=False)
value = nn.Linear(in_features=embed_dim, out_features=head_dim, bias=False)

# projections of the original embeddings
q = query(embeddings)  # (B, T, head_dim)
k = key(embeddings)  # (B, T, head_dim)
v = value(embeddings)  # (B, T, head_dim)

logger.info(f"q.shape, k.shape, v.shape: {q.shape, k.shape, v.shape}")

w = (q @ k.transpose(-2, -1)) / sqrt(head_dim)  # (B, T, T) gives the scores between all the token embeddings within each batch
# optional mask
tril = torch.tril(torch.ones(seq_length, seq_length))
w = w.masked_fill(tril == 0, float("-inf"))
# normalize weights
w = F.softmax(w, dim=-1)  # (B, T, T)

logger.info(f"w.shape: {w.shape}")


# weighted average (linear combination) of the projected input embeddings
out = w @ v

logger.info(f"out.shape: {out.shape}")
