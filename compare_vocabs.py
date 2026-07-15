import argparse
import sys
import os

def compare_vocabularies(vocab_1_path, vocab_2_path, output_path):
    # 1. Load the original vocabulary (vocab_1) into a set for O(1) lookups
    print(f"Reading original vocabulary from: {vocab_1_path}...")
    try:
        with open(vocab_1_path, 'r', encoding='utf-8') as f:
            # Strip trailing/leading whitespace and filter out empty lines
            vocab_1_set = {line.strip() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"Error: The file '{vocab_1_path}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{vocab_1_path}': {e}")
        sys.exit(1)

    # 2. Compare with the new vocabulary (vocab_2)
    print(f"Comparing with new vocabulary from: {vocab_2_path}...")
    new_tokens = []
    seen_tokens = set()  # To avoid duplicates if vocab_2 contains repetitive tokens

    try:
        with open(vocab_2_path, 'r', encoding='utf-8') as f:
            for line in f:
                token = line.strip()
                # If the token is valid, not in original vocab, and not already added
                if token and token not in vocab_1_set:
                    if token not in seen_tokens:
                        new_tokens.append(token)
                        seen_tokens.add(token)
    except FileNotFoundError:
        print(f"Error: The file '{vocab_2_path}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{vocab_2_path}': {e}")
        sys.exit(1)

    # 3. Save the difference to the output file
    if not new_tokens:
        print("Comparison complete: No new tokens were found in the new vocabulary.")
        # Create an empty file to represent the blank diff
        with open(output_path, 'w', encoding='utf-8') as f:
            pass
        return

    print(f"Found {len(new_tokens)} unique new tokens. Writing to '{output_path}'...")
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for token in new_tokens:
                f.write(token + '\n')
        print("Success! File saved successfully.")
    except Exception as e:
        print(f"Error writing to '{output_path}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(
        description="Compare two vocabulary files and extract tokens unique to the second vocabulary."
    )
    parser.add_argument(
        "vocab_1", 
        help="Path to the original tokenizer vocabulary file (e.g., vocab_1.txt)"
    )
    parser.add_argument(
        "vocab_2", 
        help="Path to the new tokenizer vocabulary file (e.g., vocab_2.txt)"
    )
    parser.add_argument(
        "-o", "--output", 
        default="new_vocab.txt", 
        help="Path to save the unique tokens output file (default: new_vocab.txt)"
    )

    args = parser.parse_args()
    
    compare_vocabularies(args.vocab_1, args.vocab_2, args.output)
