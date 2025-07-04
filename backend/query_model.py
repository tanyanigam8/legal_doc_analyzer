# backend/query_model.py

import subprocess

def format_prompt(chunks, topic):
    """
    Create a prompt from retrieved document chunks and topic/question.
    """
    formatted_chunks = "\n\n".join(chunks)
    prompt = f"""You are a legal expert AI.
Given the following case content:\n\n{formatted_chunks}\n\n
Please provide the following information about the case:

1. Parties involved
2. Summary of the case
3. Verdict (if mentioned)
4. Relevant laws/acts

Respond in clear and structured format.
"""
    return prompt

def get_mistral_answer(prompt):
    """
    Call Mistral model via Ollama CLI using subprocess.
    Assumes model 'mistral' is available in local Ollama.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60  # avoid infinite wait
        )

        if result.returncode == 0:
            return result.stdout.decode("utf-8").strip()
        else:
            error_msg = result.stderr.decode("utf-8")
            return f"⚠️ Mistral Error: {error_msg}"

    except Exception as e:
        return f"⚠️ Ollama subprocess failed: {e}"
