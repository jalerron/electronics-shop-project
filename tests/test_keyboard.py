def test_init(kb):
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5


def test_change_lang(kb):
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
