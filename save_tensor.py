import torch
from safetensors.torch import save_file
from marigold import MarigoldPipeline
import argparse

parser = argparse.ArgumentParser(
        description="Run single-image depth estimation using Marigold."
    )
parser.add_argument(
        "--checkpoint",
        type=str,
        default="prs-eth/marigold-v1-0",
        help="Checkpoint path or hub name.",
    )
dtype = torch.float32
variant = None
args = parser.parse_args()
checkpoint_path = args.checkpoint
pipe = MarigoldPipeline.from_pretrained(
        checkpoint_path, variant=variant, torch_dtype=dtype, cache_dir="/mnt/data/bientd/Marigold/cache/" 
    )

save_file(pipe, f"{checkpoint_path}/model.safetensors")