


<img width="800" height="800" alt="CLISIPY" src="https://github.com/user-attachments/assets/d3d621d7-0a8b-42af-8872-c9411d4ccdb4" />



# CLISIPY 
##* __(Command-Line Interface Smart Interpreter by Python)__*

Convert pseudocode into actual code across 25+ *__(and more in future!)__* programming languages using AI.

## Overview

CLISIPY is a command-line tool that leverages the Groq API and the Llama 3.3 70B model to automatically convert pseudocode into production-ready code. Simply write your pseudocode logic, and let AI handle the implementation in your chosen programming language.

## Features

- **Multi-language support**: Convert pseudocode to Python, JavaScript, Java, C++, Rust, Go, and 20+ other languages
- **AI-powered conversion**: Uses Groq's Llama 3.3 70B model for accurate and modern code generation
- **Clean output**: Generates code without markdown formatting or unnecessary additions
- **Best practices**: Produces code following current language standards and practices
- **Memory-aware**: Special handling for low-level languages without garbage collection

## Supported Languages

Python, C++, C, Java, Ruby, C#, PHP, Rust, Go, Lua, Swift, Kotlin, Dart, GDScript, JavaScript, Zig, Julia, F#, Cython, and more.

## Download

### Option 1: Clone the Repository (Recommended)

If you have Git installed, clone the repository:

```bash
git clone https://github.com/Anas-AbdelRaoof/CLISIPY.git
```

### Option 2: Download as ZIP

1. Go to [github.com/Anas-AbdelRaoof/CLISIPY](https://github.com/Anas-AbdelRaoof/CLISIPY)
2. Click the green **Code** button
3. Select **Download ZIP**
4. Extract the downloaded file

## Installation

1. Navigate to the project directory:
```bash
cd CLISIPY 
```

2. Install dependencies:
```bash
pip install -r requirements.txt --break-system-packages
```

```bash
cd src
```

3. Set up your Groq API key:
   - Create a `.env` file in the project root
   - Add your API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```
   - Get your free API key from [groq.com](https://groq.com)

## Usage

Create a `.txt` file with your pseudocode, then run:

```bash
python app.py <pseudocode_file.txt> <language> <output_file>
```

### Example

1. Create `algorithm.txt`:
```
Read a number n
Initialize sum to 0
For i from 1 to n
  Add i to sum
Print sum
```

2. Run:
```bash
python app.py algorithm.txt python sum.py
```

3. The AI generates the code and saves it to `sum.py`

## Requirements

- Python 3.x
- Groq API key (get it from [groq.com](https://groq.com))
- Dependencies listed in `requirements.txt`:
  - `groq` - Groq API client
  - `python-dotenv` - Environment variable management
  - `rich` - Terminal formatting

## How It Works

1. **Input validation**: Verifies the pseudocode file is a non-empty `.txt` file
2. **Language verification**: Ensures the output file extension matches the chosen language
3. **AI conversion**: Sends the pseudocode and language specifications to Groq's API
4. **Code output**: Writes the generated code to your specified file

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.
