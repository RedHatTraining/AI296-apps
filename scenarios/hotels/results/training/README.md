# RHEL AI Model Training Scenario: A Fictional Hotel Group -- Trained Model

The trained model for this scenario is available at https://huggingface.co/RedHatTraining/AI296-m3diterraneo-hotels.

The model is available in two formats:
    - The Hugging Face `safetensors` format that results from training a model with RHEL AI.
    - A quantized version in GGUF (`samples_89973_Q4_K_M.gguf`), created for serving the model on the CPU-only lab environment of Red Hat Training.

> NOTE: This model has been trained using a reduced version of the RHEL AI default training process.
> It is only meant to be used for learning purposes.
> In this reduced version, the model has been trained only during four hours, instead of four to six days.
> Additionally, the number of training samples has been reduced from ~330,000 to only 10,000.
>
> As a result, the model, although useful for learning purposes, is far from being optimally tuned.
