# LLM Mathematical Reasoning via Supervised Fine-Tuning

This project showcases how Large Language Models (LLMs), specifically **Qwen2.5 7B Instruct**, can be fine-tuned using the **GSM8K dataset** to perform **multi-step grade school-level mathematical reasoning**. The model is trained in a supervised setting to break down complex math problems into interpretable and verifiable steps.

---

## Objectives

- Perform chain-of-thought (CoT) mathematical reasoning
- Use supervised fine-tuning (SFT) on GSM8K
- Evaluate zero-shot vs. fine-tuned LLM performance
- Demonstrate the importance of structured reasoning prompts

---

## Dataset: GSM8K

- 7.5K training and 1K test grade school math word problems
- Includes **annotated solutions** with intermediate calculations
- Supports **step-by-step evaluation** using a calculator model

> Source: [GSM8K paper](https://arxiv.org/abs/2110.14168) 

---

## 🏗 Model and Training

- **Base Model**: Qwen2.5 7B Instruct
- **Finetuning**: Supervised, using HuggingFace's Trainer API
- **Input Format**: Prompt with question, step-by-step answer labeled
- **Training Objective**: Minimize token-wise cross-entropy loss on CoT-style solutions

---

##  Inference & Evaluation

- Prompt the base and fine-tuned models with test questions
- Compare reasoning quality using:
  - Correctness of final answer (`#### answer`)
  - Quality of intermediate steps
- Can integrate a `calculator.py` module for runtime evaluation

---

## How to Run

### Install Requirements

```bash
pip install -r requirements.txt
```

```Fine-Tune Model
python train.py
```
```Run Inference / Sample
python sample.py
```
---
### Key Features
- Supervised fine-tuning on structured math reasoning
- Evaluation by step correctness and final solution
- Chain-of-thought traceability
- Easily swappable LLM backends (OpenAI, Hugging Face, Predibase)

### Why This Matters
This project bridges the gap between large language models and human-level mathematical reasoning. It demonstrates how instruction-tuned LLMs, when given structured training data and clear prompts, can generalize complex reasoning tasks such as multi-step arithmetic — a key benchmark for evaluating LLM intelligence.
---
##  Citation
{
@article{cobbe2021gsm8k,
  title={Training Verifiers to Solve Math Word Problems},
  author={Cobbe, Karl et al.},
  journal={arXiv preprint arXiv:2110.14168},
  year={2021}
}
