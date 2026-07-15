import argparse
from huggingface_hub import hf_hub_download

parser = argparse.ArgumentParser(
    description="Download the vocabulary file of a specific tokenizer"
)
parser.add_argument(
    "repo_id", 
    help="Path to the original tokenizer vocabulary file (e.g., microsoft/MiniLM-L12-H384-uncased)"
)
parser.add_argument(
    "output_file", 
    help="Path to the downloaded tokenizer vocabulary file (e.g., vocab_1.txt)"
)

args = parser.parse_args()

repo_id = args.repo_id
output_file = args.output_file



local_path = hf_hub_download(
    repo_id=repo_id, 
    filename="vocab.txt",
    local_dir=output_file
)
print(f"File downloaded to: {local_path}")

