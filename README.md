# AI296-apps
Applications and resources for the exercises in RHEL AI training (AI296)


## Tools

### Synthetic Data Inspector

Inspect generated training skill messages containing the "breakfast" and "hours" terms.

```
uv run utils/inspect_sdg.py ~/.local/share/instructlab/datasets/datetime/skills_train_msgs_....jsonl -s breakfast -s hours
```

Same for the generated sythetic knowledge:

```
uv run utils/inspect_sdg.py ~/.local/share/instructlab/datasets/datetime/knowledge_train_msgs_....jsonl -s breakfast -s hours
```

### Synthetic Data Reducer

Reducing the generated synthetic dataset by extracting a subset is useful for reducing the duration of the subsequent training process.
This is useful for debugging, experimentation, and learning.

```
uv run utils/reduce_synthetic_data.py ~/.local/share/instructlab/datasets/datetime
```