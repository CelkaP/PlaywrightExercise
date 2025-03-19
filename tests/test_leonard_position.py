import pytest


@pytest.mark.parametrize(
    "text_to_find",
    ["board of directors since 2006", "chief executive officer of grid dynamics"],
)
def test_leonard_bio(cached_leonard_info, text_to_find):
    print(f"--------------------\n{cached_leonard_info}\n--------------------")
    bio = cached_leonard_info[0]
    assert (
        text_to_find.lower() in bio.lower()
    ), f"{text_to_find} not found in bio: \n {cached_leonard_info}"


def test_is_leonard_position_correct(cached_leonard_info):
    position = cached_leonard_info[1].upper()
    position_to_find = "CHIEF EXECUTIVE OFFICER AND DIRECTOR"
    print(f"--------------------\n{position}\n--------------------")

    assert (
        position == position_to_find
    ), f' "{position_to_find}" not found in {cached_leonard_info[1]}'
