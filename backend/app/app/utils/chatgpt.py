from uuid import UUID
import openai
import tiktoken


def num_tokens_from_messages(
    messages: list[dict[str, str]], model: str = "gpt-3.5-turbo-0301"
):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
        num_tokens = 0
        for message in messages:
            num_tokens += (
                4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
            )
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":  # if there's a name, the role is omitted
                    num_tokens += -1  # role is always required and always 1 token
        num_tokens += 2  # every reply is primed with <im_start>assistant
        return num_tokens
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )


def get_embedding(text, model="text-embedding-ada-002", user_id: str | UUID = "001"):
    text = text.replace("\n", " ")
    user_id = str(user_id) if isinstance(user_id, UUID) else user_id
    return openai.Embedding.create(input=[text], model=model, user=user_id)["data"][0]["embedding"]
