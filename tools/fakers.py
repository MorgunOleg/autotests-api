import time
from typing import cast
from pydantic import EmailStr


def get_random_email() -> EmailStr:
    return cast(EmailStr, f"test.{time.time()}@example.com")
