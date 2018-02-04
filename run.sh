python -m nmt.nmt.nmt \
    --src=en --tgt=sh \
    --vocab_prefix=data/vocab  \
    --train_prefix=data/train \
    --dev_prefix=data/dev  \
    --test_prefix=data/tst \
    --out_dir=model \
    --num_train_steps=200000 \
    --steps_per_stats=100 \
    --num_layers=1 \
    --num_units=1024 \/
    --dropout=0.2 \
    --metrics=bleu \
    --learning_rate=0.01 \
    override_loaded_hparams
