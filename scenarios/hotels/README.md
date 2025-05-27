# RHEL AI Model Training Scenario: A Fictional Hotel Group

A fictional example for the _Training Large Language Models with Red{nbsp}Hat Enterprise Linux AI (AI0005L)_ and _Deploying Models with Red Hat Enterprise Linux AI (AI0006L)_ [lessons](https://rol.redhat.com/).

These lessons present students with a scenario where a hotel group owning three hotels must train their own LLM, aligned with their business needs.

* The taxonomy with skills and knowledge is at https://github.com/RedHatTraining/AI296-taxonomy-hotels.
We cannot store the the taxonomy in a monorepo because InstructLab/RHEL AI needs each taxonomy to live in its own dedicated repository.

* The knowledge documents that support the knowledge contributed to the taxonomy are stored in the `business_docs` directory.

* The `results` directory contains the intermediate outputs of the SDG phase to save time to the student.
With the provided taxonomy, the SDG phase takes ~ 2 hours in a `g6e.12xlarge` AWS instance.

* The trained model is available at https://huggingface.co/RedHatTraining/AI296-m3diterraneo-hotels
This model has been trained with RHEL AI using a small subset of the complete synthetic dataset and a limited number of epochs, so its performance is limited.
The model is available in two formats:
    - The Hugging Face `safetensors` format that results from training a model with RHEL AI.
    - A quantized version in GGUF (`samples_89973_Q4_K_M.gguf`), created for serving the model on the CPU-only lab environment of Red Hat Training.