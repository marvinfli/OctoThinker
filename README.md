# OctoThinker: Revisiting Mid-training in the Era of RL Scaling

<div align="center">

[![Notion](https://img.shields.io/badge/Notion_Blog-4d8cd8?style=for-the-badge&logo=notion&logoColor=white)](https://tinyurl.com/OctoThinker)
[![Model](https://img.shields.io/badge/Model_Weights-5f16a8?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/collections/GAIR/octothinker-68035e416813f9833a8060f3)
</div>

This repository contains the code for OctoThinker project. 


## 🔥 News
[2025-04] 🎉🎉🎉 We release our progress blog on [**Notion**](https://tinyurl.com/OctoThinker), together with the first version of OctoThinker models on [**HuggingFace**](https://huggingface.co/collections/GAIR/octothinker-68035e416813f9833a8060f3).

## 📖 Introduction


## Usage
Currently, our repo contains 3 main parts:
- Pre-training code based on [Nanotron](https://github.com/huggingface/nanotron)
- RL code based on [verl](https://github.com/volcengine/verl)
- Evaluation code which is refined from [DeepSeekMath](https://github.com/deepseek-ai/deepseek-math) and [MegaMath](https://github.com/LLM360/MegaMath)

### Pre-training


### RL


### Evaluation


### Visualization
We also provide the visualization code for the pre-training and RL process. All visualizations are in [plot](./plot/) directory to ensure the reproducibility.


## Acknowledgements

For training framework and inference engine, we use [**verl**](https://github.com/volcengine/verl) and  [**vLLM**](https://github.com/vllm-project/vllm). We thank huggingface **[open-r1 team](https://huggingface.co/open-r1)**, [**a-m-team**](https://huggingface.co/a-m-team), and also [**SimpleRL**](https://github.com/hkust-nlp/simpleRL-reason) Project, to open source their dataset and training recipes. In fact, we are deeply grateful to the entire open‑source community for their tireless efforts in making our exploration possible.

If you find this work useful, please cite
```
@misc{xxxx,
  title={xxx},
  author={xxxx},
  year={2025},
  howpublished={\url{https://tinyurl.com/OctoThinker}},
  note={Notion Blog}
  year={2025}
}
```