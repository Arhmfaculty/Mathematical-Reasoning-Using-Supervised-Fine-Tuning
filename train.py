import torch as th
from dataset import get_examples, GSMDataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import GPT2Config
from torch.optim import AdamW  
from transformers import get_scheduler
from tqdm.auto import tqdm
from torch.utils.data import DataLoader


def main():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    train_examples = get_examples("train")
    train_dset = GSMDataset(tokenizer, train_examples)

    device = th.device("cuda" if th.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    config = GPT2Config.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2", config=config)
    model.to(device)
    model.train()

    train_loader = DataLoader(train_dset, batch_size=4, shuffle=True)  # Reduced batch size
    optim = AdamW(model.parameters(), lr=1e-5)

    num_epochs = 1 # Reduced number of epochs for demonstration
    num_training_steps = num_epochs * len(train_loader)
    lr_scheduler = get_scheduler(
        "linear",
        optimizer=optim,
        num_warmup_steps=0,
        num_training_steps=num_training_steps,
    )

    pbar = tqdm(range(num_training_steps))
    for epoch in range(num_epochs):
        for batch in train_loader:
            optim.zero_grad()
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch, labels=batch["input_ids"])
            loss = outputs[0]
            loss.backward()
            optim.step()
            lr_scheduler.step()
            pbar.update(1)
            pbar.set_description(f"train_loss: {loss.item():.5f}")

    model.save_pretrained("model_ckpts/")


if __name__ == "__main__":
    main()
