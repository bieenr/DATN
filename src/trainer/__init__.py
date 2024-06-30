# Author: Bingxin Ke
# Last modified: 2024-05-17

from .marigold_trainer import MarigoldTrainer
from .lora_trainer import LoraMarigoldTrainer

trainer_cls_name_dict = {
    "MarigoldTrainer": MarigoldTrainer,
    'LoraMarigoldTrainer': LoraMarigoldTrainer
}


def get_trainer_cls(trainer_name):
    return trainer_cls_name_dict[trainer_name]
