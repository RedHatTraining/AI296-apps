# /// script
# dependencies = []
# ///
import random
import argparse
from pathlib import Path

random.seed(83)


def reduce_samples_from_file(input_file, output_file, num_lines_to_copy: int):
    with (
        open(input_file, "r", encoding="utf-8") as f_in,
        open(output_file, "w", encoding="utf-8") as f_out,
    ):
        lines = f_in.readlines()

        if len(lines) <= num_lines_to_copy:
            sampled_lines = lines
        else:
            sampled_lines = random.sample(lines, num_lines_to_copy)

        f_out.writelines(sampled_lines)


def find_skill_and_knowledge_files(directory):
    dir_path = Path(directory)

    # Find any file(s) that match the patterns
    skills_matches = list(dir_path.glob("skills_train_msgs*.jsonl"))
    knowledge_matches = list(dir_path.glob("knowledge_train_msgs*.jsonl"))

    # Pick the first match if it exists, or None
    skills_file = skills_matches[0] if skills_matches else None
    knowledge_file = knowledge_matches[0] if knowledge_matches else None

    return skills_file, knowledge_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="SDG reducer",
        description=("Reduce a synthetic dataset generated with RHEL AI"),
    )
    parser.add_argument("dataset_dir")
    parser.add_argument(
        "-n",
        "--num_lines",
        help="Extract this number of samples from the original files",
        default=500,
    )
    args = parser.parse_args()

    skills_file, knowledge_file = find_skill_and_knowledge_files(args.dataset_dir)

    skills_out_file = (
        Path(args.dataset_dir) / f"skills_train_reduced_{args.num_lines}_samples.jsonl"
    )
    knowledge_out_file = (
        Path(args.dataset_dir)
        / f"knowledge_train_reduced_{args.num_lines}_samples.jsonl"
    )

    reduce_samples_from_file(skills_file, skills_out_file, int(args.num_lines))
    reduce_samples_from_file(knowledge_file, knowledge_out_file, int(args.num_lines))

    print("Generated reduced files:")
    print(" ", skills_out_file)
    print(" ", knowledge_out_file)
