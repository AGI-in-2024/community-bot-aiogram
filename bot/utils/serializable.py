from typing import Any, Final, Callable

from msgspec.json import Decoder, Encoder

__all__ = ("encode", "decode")

encode_bytes: Final[Callable[..., bytes]] = Encoder().encode
decode: Final[Callable[..., Any]] = Decoder[dict[str, Any]]().decode


def encode(obj: Any) -> str:
    data: bytes = encode_bytes(obj)
    return data.decode()
