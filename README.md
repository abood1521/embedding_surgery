# embedding_surgery
## embedding_surgery

This project provides tools for vocabulary analysis and tokenizer comparison. Key features include:
- Comparing vocabularies between different tokenizers
- Downloading pre-trained tokenizer vocabularies
- Identifying unique tokens between vocabularies

## Usage

### 1. Setup Environment

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Download a tokenizer vocabulary
```bash
python download_vocab.py microsoft/MiniLM-L12-H384-uncased vocab_1.txt
```

### 3. Compare vocabularies
```bash
python compare_vocabs.py vocab_1.txt new_vocab.txt new_tokens.txt
```

## Scripts
- `compare_vocabs.py`: Identifies unique tokens between two vocabularies
- `download_vocab.py`: Downloads tokenizer vocab files from Hugging Face
- `main.py`: The "surgery" implementation

## Files
- `vocab_1.txt`: Original vocabulary file
- `new_vocab.txt`: New vocabulary file
- `n_vocab1.txt`: Normalized vocabulary file
- `cs_vocabulary.txt`: Custom vocabulary file
- `compare_vocabs.py`: Main comparison script
- `download_vocab.py`: Vocabulary download script

For more information on vocabulary analysis techniques, refer to the project documentation.
