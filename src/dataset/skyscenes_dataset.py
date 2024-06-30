# Last modified: 2024-02-08
#
# Copyright 2023 Bingxin Ke, ETH Zurich. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
# If you find this code useful, we kindly ask you to cite our paper in your work.
# Please find bibtex at: https://github.com/prs-eth/Marigold#-citation
# If you use or adapt this code, please attribute to https://github.com/prs-eth/marigold.
# More information about the method can be found at https://marigoldmonodepth.github.io
# --------------------------------------------------------------------------

import torch
import io
import numpy as np
from PIL import Image
import tarfile
import os

from .base_depth_dataset import BaseDepthDataset, DepthFileNameMode

class SkyScenesDataset(BaseDepthDataset):
    def __init__(
        self,
        **kwargs,
    ) -> None:
        super().__init__(
            # SkyScenes dataset parameter
            min_depth=0,
            max_depth=255.0,
            has_filled_depth=False,
            name_mode=DepthFileNameMode.id,
            **kwargs,
        )
    def _read_image(self, img_rel_path) -> np.ndarray:
        if self.is_tar:
            if self.tar_obj is None:
                self.tar_obj = tarfile.open(self.dataset_dir)
            image_to_read = self.tar_obj.extractfile("./" + img_rel_path)
            image_to_read = image_to_read.read()
            image_to_read = io.BytesIO(image_to_read)
        else:
            image_to_read = os.path.join(self.dataset_dir, img_rel_path)
        image = Image.open(image_to_read) # [H, W, rgb] ???.convert('RGB') 
        image = np.asarray(image)
        return image
    def _read_depth_file(self, rel_path):
        depth_in = self._read_image(rel_path)
        # print(depth_in.shape)
        # Decode SkyScene depth  (/ 255.0 * 2.0 - 1.0 ko dùng đc khi đánh giá)
        # depth_decoded = depth_in #/ 1000.0
        depth_decoded = depth_in #/ 255.0 * 2.0 - 1.0 
        return depth_decoded