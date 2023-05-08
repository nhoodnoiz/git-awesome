import argparse
from openthaigpt_pretraining_model.lightning.utils import (
    seed_everything,
    Trainer,
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--accelerator", type=str, default="cuda", help="cpu | cuda")
    parser.add_argument(
        "--strategy",
        type=str,
        default="auto",
        help="dp | ddp | ddp_spawn | xla | deepspeed | fsdp",
    )
    parser.add_argument("--devices", type=int, default=1, help="number of GPUS")
    parser.add_argument(
        "--precision",
        type=str,
        default="32-true",
        help="32-true | 32 | 16-mixed | bf16-mixed | 64-true",
    )
    parser.add_argument("--seed", type=int, default=42, help="{13|21|42|87|100}")
    parser.add_argument("--batch_size", type=int, default=2)
    parser.add_argument("--grad", type=int, default=4, help="gradient accumulate")
    parser.add_argument("--context_length", type=int, default=256, help="seq")
    parser.add_argument("--optimizer", type=str, default="adamw", help="adamw | lion")
    parser.add_argument("--weight_decay", type=float, default=1e-2, help="weight decay")
    parser.add_argument("--lr", type=float, default=5e-4, help="lr")
    """
        accelerator: Union[str, Accelerator] = "auto",
        strategy: Union[str, Strategy] = "auto",
        devices: Union[List[int], str, int] = "auto",
        precision: Union[str, int] = "32-true",
        seed: int = 42,
        batch_size: int = 8,
        # grad: int = 4,
        context_length: int = 256,
        model_name: str = "decapoda-research/llama-7b-hf",
        optimizer: str = "adamw",
        weight_decay: float = 1e-2,
        lr: float = 1e-4,
    """

    parser.add_argument(
        "--model_name",
        type=str,
        default="llama",
        help="{llama(7B) | gptj}",
    )

    args = parser.parse_args()
    print(args)

    seed_everything(args.seed)
    trainer = Trainer(
        accelerator=args.accelerator,
        strategy=args.strategy,
        devices=args.devices,
        precision=args.precision,
        seed=args.seed,
        batch_size=args.batch_size,
        # grad=args.grad,
        context_length=args.context_length,
        model_name=args.model_name,
        optimizer=args.optimizer,
        weight_decay=args.weight_decay,
        lr=args.lr,
    )
    trainer.train()
